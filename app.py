"""
Self-Managing Inventory Manager for sneaker/clothing shop.
Flask app with dashboard and inventory management features.
"""
import os
from typing import Dict, Any
from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='web/templates')
app.secret_key = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# Import services (will be created next)
try:
    from services.sheets import SheetsService
    from services.inventory import InventoryService
    from services.ls_api import LightspeedAPI
except ImportError:
    # Services not yet implemented, create stubs
    SheetsService = None
    InventoryService = None
    LightspeedAPI = None


@app.route('/')
def dashboard() -> str:
    """Dashboard with inventory overview tiles."""
    try:
        # Mock data for now - will be replaced with real data from sheets
        dashboard_data = {
            'total_skus': 245,
            'total_on_hand': 1842,
            'low_stock_count': 12,
            'last_sync': '2025-10-09 14:30:00'
        }
        return render_template('index.html', **dashboard_data)
    except Exception as e:
        return f"Dashboard error: {str(e)}", 500


@app.route('/inventory')
def inventory() -> str:
    """Inventory table view with search and sort capabilities."""
    try:
        # Mock inventory data - will be replaced with real data from sheets
        inventory_data = [
            {
                'ItemID': '1001',
                'SKU': 'JD1-BLK-10',
                'Name': 'Air Jordan 1 Black',
                'Category': 'Sneakers',
                'Color': 'Black',
                'Size': '10',
                'Barcode': '123456789',
                'RetailPrice': 170.00,
                'QtyOnHand': 8,
                'QtySold': 2,
                'Location': 'A1',
                'LastUpdated': '2025-10-09 12:00:00'
            },
            {
                'ItemID': '1002',
                'SKU': 'JD1-WHT-9',
                'Name': 'Air Jordan 1 White',
                'Category': 'Sneakers',
                'Color': 'White',
                'Size': '9',
                'Barcode': '123456790',
                'RetailPrice': 170.00,
                'QtyOnHand': 3,
                'QtySold': 7,
                'Location': 'A2',
                'LastUpdated': '2025-10-09 12:00:00'
            }
        ]
        return render_template('inventory.html', inventory=inventory_data)
    except Exception as e:
        return f"Inventory error: {str(e)}", 500


@app.route('/low-stock')
def low_stock() -> str:
    """Low stock items view."""
    try:
        # Mock low stock data - will be replaced with real data from sheets
        low_stock_data = [
            {
                'SKU': 'JD1-WHT-9',
                'Name': 'Air Jordan 1 White',
                'QtyOnHand': 3,
                'Threshold': 5,
                'Location': 'A2'
            }
        ]
        return render_template('low_stock.html', low_stock=low_stock_data)
    except Exception as e:
        return f"Low stock error: {str(e)}", 500


@app.route('/sync', methods=['POST'])
def manual_sync() -> Dict[str, Any]:
    """Manual full sync from Lightspeed to Google Sheets."""
    try:
        # TODO: Implement full sync logic
        return jsonify({'status': 'success', 'message': 'Sync completed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/ingest-csv', methods=['POST'])
def ingest_csv() -> Dict[str, Any]:
    """Upload and process CSV file (fallback for Lightspeed data)."""
    try:
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'message': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No file selected'}), 400
        
        # TODO: Implement CSV processing logic
        return jsonify({'status': 'success', 'message': 'CSV processed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/sales')
def sales_endpoint() -> Dict[str, Any]:
    """Sales data endpoint with date range filtering."""
    try:
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        
        # TODO: Implement sales reconciliation logic
        return jsonify({
            'status': 'success',
            'from_date': from_date,
            'to_date': to_date,
            'message': 'Sales data retrieved successfully'
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    # Initialize scheduler (will be implemented later)
    try:
        from jobs.scheduler import start_scheduler
        start_scheduler()
    except ImportError:
        print("Scheduler not yet implemented - running without background jobs")
    
    port = int(os.getenv('PORT', 8080))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)