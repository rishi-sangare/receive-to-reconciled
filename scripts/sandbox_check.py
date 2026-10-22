"""Airwallex sandbox smoke test for Receive to Reconciled.

Answers the day-1 questions in docs/04-airwallex-integration.md:
  1. Can one account hold several euro Global Accounts (one per customer)?
  2. What does a deposit actually carry (payer name, reference, fee, which account)?

Steps: log in, create (or reuse) two EUR Global Accounts nicknamed per customer,
simulate one messy deposit into each, then read the deposits back.

Keys come from .env in the repo root (see .env.example). They are never printed.
Raw responses are saved to scripts/out/ (git-ignored).

Run:  python scripts/sandbox_check.py            (accounts + deposits)
      python scripts/sandbox_check.py --no-deposit
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
STATE = HERE / ".sandbox_state.json"
OUT = HERE / "out"

# One euro account per problem customer, plus the messy payment from the demo story.
CUSTOMERS = [
    {"key": "acme", "nick_name": "R2R smoke - Acme receivables EUR",
     "deposit": {"amount": 930, "payer_name": "ACME HOLDING BV", "payer_country": "NL",
                 "payer_bankname": "ING Bank", "reference": "MARCH"}},
    {"key": "holz", "nick_name": "R2R smoke - Holz receivables EUR",
     "deposit": {"amount": 4970, "payer_name": "HOLZ UND CO KG", "payer_country": "DE",
                 "payer_bankname": "Commerzbank", "reference": "PO 7781"}},
]


def load_env():
    env = {}
    path = ROOT / ".env"
    if not path.exists():
        sys.exit(f"No .env found at {path}. Copy .env.example to .env and fill in your sandbox keys.")
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("AIRWALLEX_CLIENT_ID", "AIRWALLEX_API_KEY"):
        if not env.get(k):
            sys.exit(f"{k} is missing in .env")
    return env


class Client:
    def __init__(self, base, client_id, api_key):
        self.base = base.rstrip("/")
        self.token = None
        self._id, self._key = client_id, api_key

    def _call(self, method, path, body=None, query=None, headers=None):
        url = self.base + path + ("?" + urllib.parse.urlencode(query) if query else "")
        data = json.dumps(body).encode() if body is not None else None
        h = {"Content-Type": "application/json", "User-Agent": "r2r-smoke-test/0.1"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        h.update(headers or {})
        req = urllib.request.Request(url, data=data, method=method, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, json.loads(r.read() or b"{}")
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                return e.code, json.loads(raw)
            except ValueError:
                return e.code, {"raw": raw.decode(errors="replace")[:500]}

    def login(self):
        # Credentials go in headers only; the body is empty.
        status, res = self._call("POST", "/api/v1/authentication/login",
                                 body={}, headers={"x-client-id": self._id, "x-api-key": self._key})
        if status not in (200, 201) or "token" not in res:
            sys.exit(f"Login failed ({status}): {res.get('message') or res.get('code') or res}\n"
                     "Check: the keys are SANDBOX keys (sandbox.airwallex.com), copied without spaces, and the\n"
                     "sandbox business is not stuck 'In review' (name it 'Sandbox Business' or 'New Business Sandbox').")
        self.token = res["token"]

    def get(self, path, query=None):
        return self._call("GET", path, query=query)

    def post(self, path, body):
        return self._call("POST", path, body=body)


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_state(state):
    STATE.write_text(json.dumps(state, indent=2))


def find_account(api, nick_name):
    status, res = api.get("/api/v1/global_accounts", {"nick_name": nick_name})
    if status == 200:
        for acc in res.get("items", []):
            if acc.get("nick_name") == nick_name and acc.get("status") != "CLOSED":
                return acc
    return None


def ensure_account(api, customer, state, log):
    # The builder guide says: list first, create only if missing; reuse request_id on retry.
    acc = find_account(api, customer["nick_name"])
    if acc:
        print(f"  reused   {customer['nick_name']} ({acc['status']})")
        return acc, "reused"
    rid = state.setdefault("request_ids", {}).setdefault(customer["key"], str(uuid.uuid4()))
    save_state(state)
    body = {"request_id": rid, "country_code": "NL", "nick_name": customer["nick_name"],
            "required_features": [{"currency": "EUR", "transfer_method": "LOCAL"}]}
    status, res = api.post("/api/v1/global_accounts/create", body)
    log.append({"step": f"create_account:{customer['key']}", "status": status, "response": res})
    if status not in (200, 201):
        acc = find_account(api, customer["nick_name"])  # e.g. duplicate_request_id after a timeout
        if acc:
            return acc, "reused"
        print(f"  FAILED   {customer['nick_name']}: {status} {res.get('code')} {res.get('message')}")
        return None, "failed"
    for _ in range(10):  # wait for PROCESSING -> ACTIVE
        if res.get("status") == "ACTIVE":
            break
        time.sleep(3)
        _, res = api.get(f"/api/v1/global_accounts/{res['id']}")
    print(f"  created  {customer['nick_name']} ({res.get('status')}) IBAN {res.get('iban', '-')}")
    return res, "created"


def simulate_deposit(api, account, customer, log):
    body = dict(customer["deposit"], global_account_id=account["id"])
    status, res = api.post("/api/v1/simulation/deposit/create", body)
    log.append({"step": f"simulate_deposit:{customer['key']}", "status": status, "request": body, "response": res})
    if status not in (200, 201):
        print(f"  FAILED   deposit for {customer['key']}: {status} {res.get('code')} {res.get('message')}")
        return None
    print(f"  deposit  EUR {body['amount']} from \"{body['payer_name']}\" ref \"{body['reference']}\" -> {res.get('status')}")
    return res


def read_back(api, account_ids, since):
    # Deposits can take a moment to show in the list.
    for _ in range(10):
        status, res = api.get("/api/v1/deposits", {"from_created_at": since, "page_size": 100})
        mine = [d for d in res.get("items", []) if d.get("global_account_id") in account_ids] if status == 200 else []
        if len(mine) >= len(account_ids):
            return mine
        time.sleep(3)
    return mine


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-deposit", action="store_true", help="only create or reuse the accounts")
    args = ap.parse_args()

    env = load_env()
    api = Client(env.get("AIRWALLEX_BASE_URL", "https://api.sandbox.airwallex.com"),
                 env["AIRWALLEX_CLIENT_ID"], env["AIRWALLEX_API_KEY"])
    if "sandbox" not in api.base:
        sys.exit("Refusing to run: AIRWALLEX_BASE_URL is not a sandbox URL.")

    started = datetime.now(timezone.utc)
    since = (started - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S+0000")
    log, state = [], load_state()

    print("1. Log in")
    api.login()
    print("  ok, token received")

    print("2. One euro Global Account per customer")
    accounts = {}
    for c in CUSTOMERS:
        acc, how = ensure_account(api, c, state, log)
        if acc:
            accounts[c["key"]] = (acc, how)

    deposits = []
    if accounts:
        if not args.no_deposit:
            print("3. Simulate a messy deposit into each")
            for c in CUSTOMERS:
                if c["key"] in accounts:
                    simulate_deposit(api, accounts[c["key"]][0], c, log)
        print("4. Read the deposits back")
        ids = {a["id"] for a, _ in accounts.values()}
        deposits = read_back(api, ids, since)
        log.append({"step": "list_deposits", "items": deposits})

    print("\nWhat this tells us")
    print(f"  Q1 several EUR accounts in one sandbox: {len(accounts)} of {len(CUSTOMERS)} available "
          f"({', '.join(how for _, how in accounts.values()) or 'none'})")
    if deposits:
        by_acc = {a["id"]: k for k, (a, _) in accounts.items()}
        for d in deposits:
            payer = d.get("payer") or {}
            print(f"  Q2 deposit for {by_acc.get(d.get('global_account_id'), '?')}: amount {d.get('currency')} {d.get('amount')}"
                  f" | payer name: {payer.get('name') or (payer.get('bank_account') or {}).get('name') or 'MISSING'}"
                  f" | reference: {d.get('reference') or 'MISSING'}"
                  f" | fee field: {d.get('fee')}"
                  f" | status: {d.get('status')}")
        print("  Every field the deposit record carries:", ", ".join(sorted({k for d in deposits for k in d})))
    else:
        print("  Q2 no deposits came back from GET /deposits yet. Re-run with --no-deposit in a minute to re-read.")

    OUT.mkdir(exist_ok=True)
    out = OUT / f"smoke-{started.strftime('%Y%m%d-%H%M%S')}.json"
    out.write_text(json.dumps({"run_at": started.isoformat(), "base": api.base, "log": log}, indent=2))
    print(f"\nRaw responses saved to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
