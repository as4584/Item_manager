# Quick Reference Guide

## 🚀 Getting Started

### First Time Setup
```bash
# Clone repository
git clone <repository-url>
cd inventory_manager

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your credentials

# Install pre-commit hooks (after merging PR #1)
make setup-hooks

# Run tests
make test-cov
```

### Running the Application
```bash
# Development mode
python app.py

# Application will be available at:
# http://localhost:8080
```

---

## 📂 Repository Structure

```
inventory_manager/
├── app.py                    # Main Flask application
├── services/                 # External integrations
│   ├── ls_api.py            # Lightspeed API
│   ├── sheets.py            # Google Sheets
│   ├── csv_ingest.py        # CSV processing
│   └── inventory.py         # Business logic
├── utils/                    # Shared utilities (PR #2)
│   ├── http_client.py       # HTTP/API utilities
│   ├── csv_utils.py         # CSV processing
│   └── data_validation.py   # Data validation
├── web/templates/           # HTML templates
├── jobs/                    # Background tasks
├── tests/                   # Test suites
├── .github/                 # CI/CD workflows
└── docs/                    # Documentation
```

---

## 🔧 Common Commands

### Development (requires PR #1 merged)
```bash
make install        # Install production dependencies
make install-dev    # Install dev dependencies
make setup-hooks    # Install pre-commit hooks
```

### Code Quality
```bash
make format         # Auto-format code with Ruff
make lint          # Check code quality
make type-check    # Run mypy type checking
make test          # Run tests
make test-cov      # Run tests with coverage report
```

### Security
```bash
make security       # Run all security checks
make security-json  # Generate security reports
```

### All Checks (CI simulation)
```bash
make ci            # Run lint + type-check + security + test-cov
```

### Application
```bash
make run           # Start Flask application
```

---

## 📋 Pull Requests

### PR #1: Development Tooling
**Branch:** `feature/dev-tooling`
```bash
git checkout feature/dev-tooling
# Review changes, run tests
make ci
```

### PR #2: Code Refactoring  
**Branch:** `feature/refactor-shared-utils`
```bash
git checkout feature/refactor-shared-utils
# Review changes, run tests
make ci
```

### PR #3: Security Scanning
**Branch:** `feature/security-scanning`
```bash
git checkout feature/security-scanning
# Review changes, run tests
make ci
```

---

## 🔑 Environment Variables

Required variables in `.env`:

```bash
# Google Sheets
GOOGLE_SERVICE_ACCOUNT_JSON=./service_account.json
GOOGLE_SHEET_NAME=Live ATS Inventory

# Lightspeed X-Series
LS_X_API_TOKEN=your_api_token_here
LS_ACCOUNT_DOMAIN=your_account.lightspeedapp.com

# Flask
SECRET_KEY=your_secret_key_here
FLASK_ENV=development
```

---

## 📊 Key Routes

### Dashboard
- **URL:** `http://localhost:8080/`
- **Purpose:** Overview tiles, key metrics
- **Features:** Total SKUs, on-hand inventory, low stock count

### Inventory
- **URL:** `http://localhost:8080/inventory`
- **Purpose:** Full inventory table
- **Features:** Search, sort, filter, export CSV

### Low Stock
- **URL:** `http://localhost:8080/low-stock`
- **Purpose:** Items below threshold
- **Features:** Configurable threshold, restock suggestions

### Manual Sync
- **URL:** `POST /sync`
- **Purpose:** Trigger Lightspeed sync
- **Method:** POST

### CSV Upload
- **URL:** `POST /ingest-csv`
- **Purpose:** Bulk import via CSV
- **Method:** POST with file

---

## 🧪 Testing

### Run All Tests
```bash
pytest
```

### Run with Coverage
```bash
pytest --cov=services --cov=jobs --cov=app --cov-report=html
# View coverage report in htmlcov/index.html
```

### Run Specific Test File
```bash
pytest tests/test_inventory.py
```

### Run Specific Test
```bash
pytest tests/test_inventory.py::test_auto_sort
```

---

## 🐛 Troubleshooting

### Google Sheets Authentication Error
```bash
# Ensure service account JSON exists
ls -la service_account.json

# Check environment variable
echo $GOOGLE_SERVICE_ACCOUNT_JSON

# Verify service account has access to the sheet
```

### Lightspeed API Not Working
```bash
# Check API token is set
echo $LS_X_API_TOKEN

# Verify account domain
echo $LS_ACCOUNT_DOMAIN

# Check API connectivity
curl -H "Authorization: Bearer $LS_X_API_TOKEN" \
  https://$LS_ACCOUNT_DOMAIN/api/2.0/products
```

### Pre-commit Hooks Failing
```bash
# Update hooks
pre-commit autoupdate

# Run manually
pre-commit run --all-files

# Skip hooks temporarily (not recommended)
git commit --no-verify
```

### Port Already in Use
```bash
# Find process using port 8080
lsof -i :8080

# Kill process
kill -9 <PID>

# Or run on different port
FLASK_PORT=8081 python app.py
```

---

## 📚 Documentation

### Primary Docs
- **PULL_REQUESTS.md** - Detailed PR documentation with testing instructions
- **PROJECT_STATUS.md** - Complete project overview and metrics
- **README.md** - Application setup and usage guide
- **.github/SECURITY.md** - Security policy and vulnerability reporting

### Code Documentation
- All functions have docstrings
- Type hints throughout codebase
- Inline comments for complex logic

---

## 🔄 Git Workflow

### Creating a Feature Branch
```bash
git checkout feature/scaffold-inventory-manager
git checkout -b feature/my-new-feature
# Make changes
git add .
git commit -m "feat: add new feature"
git push origin feature/my-new-feature
```

### Merging PRs (Recommended Order)
```bash
# 1. Merge dev tooling first
git checkout feature/scaffold-inventory-manager
git merge feature/dev-tooling

# 2. Merge refactoring
git merge feature/refactor-shared-utils

# 3. Merge security
git merge feature/security-scanning

# 4. Push to remote
git push origin feature/scaffold-inventory-manager
```

---

## 📦 Deployment Checklist

### Before Deploying
- [ ] All PRs merged
- [ ] All tests passing (`make ci`)
- [ ] Environment variables configured
- [ ] Google Sheets service account set up
- [ ] Lightspeed API credentials obtained
- [ ] Database initialized (if applicable)
- [ ] Dependencies installed
- [ ] Pre-commit hooks working

### Production Environment
```bash
# Set production environment
export FLASK_ENV=production
export SECRET_KEY=<strong-random-key>

# Run with production WSGI server
pip install gunicorn
gunicorn app:app -b 0.0.0.0:8080
```

---

## 🆘 Getting Help

### Check Documentation
1. Read `PULL_REQUESTS.md` for PR details
2. Read `PROJECT_STATUS.md` for project overview
3. Check inline code documentation
4. Review test files for usage examples

### Debug Mode
```python
# In app.py, enable debug mode
app.run(debug=True)
```

### Logging
```python
# Add logging to troubleshoot
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 🎯 Quick Wins

### After Merging PR #1
```bash
# Use pre-commit hooks
git commit  # Automatically formats and checks code

# Run CI locally before pushing
make ci
```

### After Merging PR #2
```python
# Use shared utilities in new code
from utils.http_client import create_paginated_client
from utils.csv_utils import DataNormalizer
from utils.data_validation import DataValidator
```

### After Merging PR #3
- Automatic dependency updates via Dependabot
- Weekly security scans
- No action needed - automated!

---

*Last Updated: October 10, 2025*