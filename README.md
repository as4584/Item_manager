# Professional Inventory Management System

A production-ready inventory management system for retail operations, featuring Lightspeed X-Series integration and Google Sheets synchronization.

## Overview

This system was designed as a comprehensive solution for modern retail inventory management, showcasing enterprise-level architecture and development practices.

## Key Features

- **POS Integration**: Lightspeed Retail X-Series API
- **Operations Dashboard**: Google Sheets integration for operations teams
- **Automated Synchronization**: Scheduled inventory updates
- **Production Architecture**: Docker containerization with systemd services
- **CI/CD Pipeline**: Automated testing and deployment via GitHub Actions

## Quick Start

### Development
```bash
# Install dependencies
poetry install

# Run development server
poetry run python scripts/run_local.py
```

### Production Deployment
See [DEPLOYMENT.md](DEPLOYMENT.md) for complete production setup instructions.

## Architecture

This project follows enterprise software architecture patterns:
- Modular service-oriented design
- Port 8010 (standardized project port)
- Docker containerization
- systemd service management
- Nginx reverse proxy configuration
- Comprehensive GitHub Actions CI/CD

## Testing & Quality Assurance

```bash
# Run complete test suite
poetry run pytest

# Generate coverage reports
poetry run pytest --cov=src

# Code quality checks
ruff check src/ tests/
```

## Configuration

- `GOOGLE_SHEET_NAME`: Google Sheets spreadsheet name
- `LS_X_API_TOKEN`: Lightspeed X-Series API token  
- `LS_ACCOUNT_DOMAIN`: Lightspeed account domain

## Technology Stack

- **Backend**: Python 3.11, Flask
- **Data Processing**: Pandas, APScheduler
- **APIs**: Lightspeed X-Series, Google Sheets (gspread)
- **Infrastructure**: Docker, Nginx, systemd
- **CI/CD**: GitHub Actions with security scanning

## License

Proprietary - Portfolio Project