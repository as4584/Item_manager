# Inventory Manager

A self-managing inventory system for sneaker/clothing shops with Lightspeed X-Series integration.

## Features

- **POS Integration**: Lightspeed Retail X-Series API
- **Operations Dashboard**: Google Sheets integration
- **Automated Sync**: Hourly inventory synchronization
- **Demo Mode**: Full functionality without external dependencies
- **Production Ready**: Docker + systemd + Nginx deployment

## Quick Start

### Development
```bash
# Install dependencies
poetry install

# Run in demo mode
DEMO_MODE=true poetry run python scripts/run_local.py
```

### Production Deployment
See [DEPLOYMENT.md](DEPLOYMENT.md) for complete production setup instructions.

## Architecture

This project follows a standardized architecture template with:
- Port 8010 (inventory manager project)
- Docker containerization
- systemd service management
- Nginx reverse proxy
- GitHub Actions CI/CD

## Testing

```bash
# Run tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=src

# Lint code
ruff check src/ tests/
```

## Environment Variables

- `DEMO_MODE`: Enable demo mode (true/false)
- `GOOGLE_SHEET_NAME`: Google Sheets spreadsheet name
- `LS_X_API_TOKEN`: Lightspeed X-Series API token
- `LS_ACCOUNT_DOMAIN`: Lightspeed account domain

## License

Proprietary - DonXEra Team