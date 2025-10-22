# PR: Sheets Full Sync + RestockList

Title: feat: Sheets full sync (demo) + RestockList mirroring

What changed:
- POST /sync/sheets/full route
  - In Demo Mode: loads fixtures, normalizes to Inventory schema, writes via SheetsRepository
  - Mirrors low stock items to RestockList (SKU, Name, Size, QtyOnHand), sorted Name→Size
- Tests: tests/test_sheets_sync.py stubs repo methods; asserts JSON summary and write calls

Why:
- Enables class demo flow end-to-end (Sheets as source of truth) without credentials

How to run:

```bash
cp .env.example .env
export DEMO_MODE=true
poetry install
poetry run python app.py
```

Run the sync:

```bash
curl -X POST http://localhost:8080/sync/sheets/full
```

Tests:

```bash
DEMO_MODE=true PYTEST_RUNNING=1 poetry run pytest -q -k sheets_sync
```

Risks:
- Low (demo-only paths; uses repo methods behind gspread stubs in tests)

Next:
- Wire real Sheets credentials and expand repo methods for idempotent writes
- Hook hourly job to trigger full sync and nightly backup
