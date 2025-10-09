# Self-Managing Inventory Manager

A **Self-Managing Inventory Manager** for sneaker/clothing shops that automatically syncs with Lightspeed Retail X-Series POS and manages inventory data in Google Sheets.

## 🎯 Project Purpose

This application provides automated inventory management with:
- **Real-time sync** with Lightspeed Retail X-Series API
- **Google Sheets** as the source of truth for daily operations
- **Automated scheduling** for hourly sync and nightly maintenance
- **Web dashboard** for inventory monitoring and management
- **Low stock alerts** and restock recommendations
- **CSV import/export** capabilities for manual data management

## 🏗️ Architecture

- **Backend**: Python 3.11 + Flask
- **Data Processing**: Pandas for data manipulation
- **POS Integration**: Lightspeed X-Series API with pagination & rate limiting
- **Data Storage**: Google Sheets via gspread
- **Scheduling**: APScheduler for background jobs
- **Frontend**: Bootstrap 5 with responsive design
- **Testing**: pytest with comprehensive test coverage

## 📁 Project Structure

```
inventory_manager/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── README.md                       # This file
├── services/                       # Business logic services
│   ├── ls_api.py                  # Lightspeed X-Series API integration
│   ├── ls_auth.py                 # Authentication & token management
│   ├── sheets.py                  # Google Sheets operations
│   ├── inventory.py               # Inventory business logic
│   ├── csv_ingest.py              # CSV processing & validation
│   └── ls_webhooks.py             # Webhook handling (optional)
├── web/templates/                  # HTML templates
│   ├── base.html                  # Base template with Bootstrap
│   ├── index.html                 # Dashboard
│   ├── inventory.html             # Inventory management
│   └── low_stock.html             # Low stock alerts
├── jobs/                          # Background job scheduling
│   └── scheduler.py               # APScheduler configuration
├── sample_data/                   # Sample CSV files
│   ├── products.csv               # Sample product data
│   └── sales.csv                  # Sample sales data
├── tests/                         # Test suite
│   ├── conftest.py                # Test configuration & fixtures
│   ├── test_inventory.py          # Inventory logic tests
│   ├── test_csv_ingest.py         # CSV processing tests
│   ├── test_sheets.py             # Google Sheets tests
│   └── test_app.py                # Flask route tests
└── .github/
    └── copilot-instructions.md    # Project requirements
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Google Cloud Service Account with Sheets API access
- Lightspeed Retail X-Series account with API access
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd inventory_manager
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual configuration
   ```

5. **Configure Google Sheets**
   - Create a Google Cloud Service Account
   - Download the JSON credentials file
   - Set `GOOGLE_SERVICE_ACCOUNT_JSON` path in `.env`
   - Create a Google Sheet named "Live ATS Inventory"
   - Share the sheet with your service account email

6. **Configure Lightspeed API**
   - Get your API token from Lightspeed admin panel
   - Set `LS_X_API_TOKEN` and `LS_ACCOUNT_DOMAIN` in `.env`

### Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:8080`

## 📊 Google Sheets Structure

The application creates and manages these worksheets:

### Inventory Sheet
| Column | Description |
|--------|-------------|
| ItemID | Unique item identifier |
| SKU | Stock Keeping Unit |
| Name | Product name |
| Category | Product category (Sneakers, Clothing, Accessories) |
| Color | Product color |
| Size | Product size |
| Barcode | Product barcode |
| RetailPrice | Retail price |
| QtyOnHand | Current quantity on hand |
| QtySold | Total quantity sold |
| Location | Storage location |
| LastUpdated | Last update timestamp |

### Config Sheet
| Setting | Value | Description |
|---------|-------|-------------|
| LowStockThreshold | 5 | Minimum quantity before low stock alert |

### SalesLog Sheet
Used for deduplication of sales data to prevent double-processing.

### RestockList Sheet
Automatically maintained list of items below the low stock threshold.

## 🔄 Automated Jobs

### Hourly Sync (Default)
- Pulls products, variants, and inventory from Lightspeed
- Updates Google Sheets with current data
- Applies sales reconciliation
- Updates low stock list

### Nightly Maintenance (3:00 AM UTC)
- Sorts inventory data (Category → Name → Size)
- Refreshes low stock calculations
- Data consistency checks

### Nightly Backup (2:30 AM UTC)
- Exports inventory to timestamped CSV
- Stores in `backups/` directory

## 🌐 API Endpoints

### Web Routes
- `GET /` - Dashboard with inventory overview
- `GET /inventory` - Full inventory table with search/sort
- `GET /low-stock` - Low stock alerts and recommendations

### API Endpoints
- `POST /sync` - Manual full sync from Lightspeed
- `POST /ingest-csv` - Upload and process CSV files
- `GET /sales?from=YYYY-MM-DD&to=YYYY-MM-DD` - Sales data with date filtering

### Optional Webhook Endpoints
- `POST /webhooks/lightspeed` - Lightspeed webhook notifications
- `GET /webhooks/status` - Webhook configuration status

## 📋 Features

### Dashboard
- **Overview tiles**: Total SKUs, on-hand quantity, low stock count
- **Quick actions**: Sync, CSV upload, reports
- **System status**: API connectivity, last sync time

### Inventory Management
- **Search & filter**: By SKU, name, category, stock level
- **Sortable columns**: Click headers to sort data
- **Export functionality**: Download filtered results as CSV
- **Stock level indicators**: Color-coded status badges

### Low Stock Management
- **Priority alerts**: Critical (out of stock) vs. medium priority
- **Restock suggestions**: Intelligent quantity recommendations
- **Export restock list**: Generate purchase orders

### CSV Processing
- **Auto-detection**: Automatically detect products vs. sales CSV
- **Data cleaning**: Standardize formats, extract variants
- **Validation**: Check required columns and data integrity
- **Deduplication**: Prevent processing duplicate sales

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=services --cov=jobs

# Run specific test file
pytest tests/test_inventory.py

# Run with verbose output
pytest -v
```

### Test Coverage
- **Inventory logic**: Sorting, low stock detection, sales reconciliation
- **CSV processing**: Validation, cleaning, deduplication
- **Google Sheets**: Data operations and error handling
- **Flask routes**: HTTP endpoints and error responses

## 🔧 Configuration

### Environment Variables

```env
# Flask Configuration
FLASK_ENV=development
SECRET_KEY=change-this-in-production
PORT=8080

# Google Sheets Configuration
GOOGLE_SERVICE_ACCOUNT_JSON=./service_account.json
GOOGLE_SHEET_NAME=Live ATS Inventory

# Lightspeed X-Series API Configuration
LS_X_API_TOKEN=your_lightspeed_api_token_here
LS_ACCOUNT_DOMAIN=your_account_domain

# Optional: Scheduler Configuration
SYNC_INTERVAL_HOURS=1
LOW_STOCK_THRESHOLD=5
```

### Google Sheets Setup

1. **Create Service Account**
   - Go to Google Cloud Console
   - Create a new service account
   - Generate JSON key file
   - Enable Google Sheets API

2. **Share Spreadsheet**
   - Create a Google Sheet named "Live ATS Inventory"
   - Share with service account email (with Editor permissions)

3. **Verify Connection**
   - Run the app and check for connection status on dashboard

### Lightspeed API Setup

1. **Get API Credentials**
   - Login to Lightspeed admin panel
   - Go to Settings → Integrations → API
   - Generate API token

2. **Configure Rate Limiting**
   - API calls are automatically rate-limited (500ms between requests)
   - Respects `Retry-After` headers for 429 responses

## 🚨 Troubleshooting

### Common Issues

**Google Sheets Connection Failed**
- Verify service account JSON file path
- Check if sheet is shared with service account email
- Ensure Google Sheets API is enabled

**Lightspeed API Errors**
- Verify API token is correct and not expired
- Check account domain format (no https://)
- Monitor rate limiting and retry logic

**Scheduler Not Running**
- Check for port conflicts
- Verify timezone settings
- Look for background job errors in logs

**CSV Upload Issues**
- Ensure required columns are present
- Check data formats (dates, numbers)
- Verify file encoding (UTF-8 recommended)

### Debug Mode

Enable debug logging:
```env
FLASK_ENV=development
LOG_LEVEL=DEBUG
```

## 📈 Monitoring & Maintenance

### Health Checks
- Dashboard displays system status
- API connectivity indicators
- Last sync timestamps

### Backup Strategy
- Automated nightly CSV backups
- Google Sheets serves as primary data store
- Version history available in Google Sheets

### Performance Optimization
- Batch operations for large datasets
- Efficient pandas operations
- Rate-limited API calls
- Background job scheduling

## 🤝 Contributing

1. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes with tests**
   ```bash
   # Add your changes
   # Write tests in tests/ directory
   pytest  # Ensure all tests pass
   ```

3. **Commit with conventional format**
   ```bash
   git commit -m "feat(inventory): add automated reorder suggestions"
   ```

4. **Push and create pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Coding Standards
- **Type hints**: Use for all function parameters and returns
- **Docstrings**: Document all classes and functions
- **Small functions**: Keep functions focused and testable
- **Error handling**: Graceful degradation for API failures
- **Testing**: Maintain high test coverage

## 📄 License

This project is proprietary software for sneaker/clothing shop inventory management.

## 🆘 Support

For technical support or questions:
1. Check the troubleshooting section above
2. Review logs for error messages
3. Verify configuration settings
4. Test with sample data provided

---

**Last Updated**: October 2025
**Version**: 1.0.0