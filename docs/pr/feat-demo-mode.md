# PR: Demo Mode

Title: feat: Demo Mode (fixture-backed) + pagination fix + UI banner + health

What changed:
- Demo Mode in LightspeedClient (fixture-backed)
- Pagination fix: limit/offset slicing for fixtures to terminate pagination
- “Demo Mode Active” UI banner on dashboard and inventory templates
- `/health` includes `demo_mode` and `sheets_configured`
- No-network test `tests/test_demo_mode.py`

Why:
- Enables credential-free academic demo (IS344/IS218)
- Deterministic tests without network or sleeps

How to run:

```bash
cp .env.example .env
export DEMO_MODE=true
poetry install --sync
poetry run python app.py
```

Tests:

```bash
DEMO_MODE=true PYTEST_RUNNING=1 poetry run pytest -q
```

Risks:
- Low (Demo-only code paths)

Next:
- Sheets full sync + RestockList mirroring
- Lightspeed endpoints for live data
