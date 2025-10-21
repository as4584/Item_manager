# ⚠️ DEPRECATED - Use Poetry Instead

This project now uses **Poetry** for dependency management.

## Migration Guide

### Old Way (pip):
```bash
pip install -r requirements.txt
python app.py
```

### New Way (Poetry):
```bash
poetry install
poetry run python src/app.py
```

## Why Poetry?

- **Deterministic builds** - `poetry.lock` ensures everyone has exact same dependencies
- **Dependency resolution** - Poetry resolves conflicts automatically
- **Development isolation** - Separate dev dependencies from production
- **Better tooling** - Built-in support for testing, linting, type checking
- **Modern standard** - Poetry is the de facto standard for Python projects

## For CI/CD

Replace:
```yaml
pip install -r requirements.txt
```

With:
```yaml
poetry install --no-root
```

## Generate requirements.txt (if needed)

If you need a requirements.txt for legacy systems:
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

---

See [pyproject.toml](./pyproject.toml) for all dependencies.
