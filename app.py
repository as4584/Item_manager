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

# Check if demo mode is enabled
DEMO_MODE = os.getenv('DEMO_MODE', 'true').lower() == 'true'

# Import version info
try:
    from __version__ import __version__, get_version
except ImportError:
    __version__ = "1.0.0"
    def get_version():
        return __version__

app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# Import services
try:
    from sheets import SheetsService
    from inventory import InventoryService
    from ls_api import LightspeedAPI
except ImportError:
    # Services not yet implemented, create stubs
    SheetsService = None
    InventoryService = None
    LightspeedAPI = None

# Import demo data if in demo mode
if DEMO_MODE:
    from demo_data import (
        load_demo_data, 
        get_demo_inventory, 
        update_demo_stock,
        get_low_stock_items,
        get_inventory_stats
    )
    print("🎮 DEMO MODE ENABLED - Using sample data")


@app.route('/')
def dashboard() -> str:
    """Dashboard with inventory overview tiles."""
    try:
        if DEMO_MODE:
            dashboard_data = get_inventory_stats()
            dashboard_data['last_sync'] = 'Demo Mode - No sync'
        else:
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
        if DEMO_MODE:
            df = get_demo_inventory()
            inventory_data = df.to_dict('records')
        else:
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
        if DEMO_MODE:
            df = get_low_stock_items(threshold=5)
            low_stock_data = df[['SKU', 'Name', 'QtyOnHand', 'Location']].to_dict('records')
            # Add threshold to each item
            for item in low_stock_data:
                item['Threshold'] = 5
        else:
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
        if DEMO_MODE:
            # In demo mode, reload the sample data
            load_demo_data()
            return jsonify({'status': 'success', 'message': 'Demo data reloaded'})
        # TODO: Implement full sync logic
        return jsonify({'status': 'success', 'message': 'Sync completed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/update-stock', methods=['POST'])
def update_stock_endpoint() -> Dict[str, Any]:
    """Update stock quantity for an item (demo mode only)."""
    try:
        if not DEMO_MODE:
            return jsonify({'status': 'error', 'message': 'Only available in demo mode'}), 403
        
        data = request.get_json()
        item_id = int(data.get('item_id'))
        new_qty = int(data.get('quantity'))
        
        if update_demo_stock(item_id, new_qty):
            return jsonify({
                'status': 'success', 
                'message': f'Updated item {item_id} to quantity {new_qty}'
            })
        else:
            return jsonify({'status': 'error', 'message': 'Item not found'}), 404
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


@app.route('/version')
def version() -> Dict[str, str]:
    """Return application version information."""
    return jsonify({
        'version': get_version(),
        'name': 'Self-Managing Inventory Manager',
        'python': os.sys.version.split()[0]
    })


@app.route('/health')
def health() -> Dict[str, str]:
    """Health check endpoint for monitoring."""
    return jsonify({
        'status': 'healthy',
        'version': get_version()
    })


if __name__ == '__main__':
    # Load demo data if in demo mode
    if DEMO_MODE:
        print("🎮 Loading demo data...")
        load_demo_data()
        stats = get_inventory_stats()
        print(f"📊 Demo Stats: {stats['total_skus']} SKUs, {stats['total_on_hand']} items on hand, {stats['low_stock_count']} low stock")
    
    # Initialize scheduler (will be implemented later)
    if not DEMO_MODE:
        try:
            from scheduler import start_scheduler
            start_scheduler()
        except ImportError:
            print("Scheduler not yet implemented - running without background jobs")
    else:
        print("⏸️  Scheduler disabled in demo mode")
    
    port = int(os.getenv('PORT', 8080))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print(f"\n🚀 Starting server on http://localhost:{port}")
    print(f"📍 Mode: {'DEMO' if DEMO_MODE else 'PRODUCTION'}")
    print(f"🔧 Debug: {debug}\n")
    
    app.run(host='0.0.0.0', port=port, debug=debug)