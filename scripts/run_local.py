#!/usr/bin/env python3
"""
Self-Managing Inventory Manager - Development Server
"""
import os, sys
from pathlib import Path

# Add src/ to Python path
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / 'src'))

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from typing import Dict, Any

load_dotenv()
DEMO_MODE = os.getenv('DEMO_MODE', 'true').lower() == 'true'

try:
    from __version__ import __version__, get_version
except ImportError:
    __version__ = "1.0.0"
    def get_version():
        return __version__

try:
    from services.sheets.service import SheetsService
    from domain.inventory import InventoryService
    from services.lightspeed.api import LightspeedAPI
except ImportError:
    SheetsService = InventoryService = LightspeedAPI = None

if DEMO_MODE:
    from ingestion.demo_data import (load_demo_data, get_demo_inventory, 
                                      update_demo_stock, get_low_stock_items, get_inventory_stats)
    print("🎮 DEMO MODE ENABLED")

app = Flask(__name__, 
            template_folder=str(repo_root / 'src' / 'app' / 'templates'),
            static_folder=str(repo_root / 'src' / 'app' / 'static'))
app.secret_key = os.getenv('SECRET_KEY', 'dev-key')

@app.route('/')
def dashboard():
    try:
        if DEMO_MODE:
            data = get_inventory_stats()
            data['last_sync'] = 'Demo Mode'
        else:
            data = {'total_skus': 0, 'total_on_hand': 0, 'low_stock_count': 0, 'last_sync': 'N/A'}
        return render_template('index.html', **data)
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/inventory')
def inventory():
    try:
        data = get_demo_inventory().to_dict('records') if DEMO_MODE else []
        return render_template('inventory.html', inventory=data)
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/low-stock')
def low_stock():
    try:
        if DEMO_MODE:
            df = get_low_stock_items(threshold=5)
            data = df[['SKU', 'Name', 'QtyOnHand', 'Location']].to_dict('records')
            for item in data:
                item['Threshold'] = 5
        else:
            data = []
        return render_template('low_stock.html', low_stock=data)
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/sync', methods=['POST'])
def manual_sync():
    try:
        if DEMO_MODE:
            load_demo_data()
        return jsonify({'status': 'success', 'message': 'Synced'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/update-stock', methods=['POST'])
def update_stock_endpoint():
    try:
        if not DEMO_MODE:
            return jsonify({'status': 'error', 'message': 'Demo mode only'}), 403
        data = request.get_json()
        if update_demo_stock(int(data.get('item_id')), int(data.get('quantity'))):
            return jsonify({'status': 'success'})
        return jsonify({'status': 'error', 'message': 'Not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/version')
def version():
    return jsonify({'version': get_version(), 'name': 'DonXEra Inventory', 'python': sys.version.split()[0]})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'version': get_version()})

if __name__ == '__main__':
    # Load demo data
    if DEMO_MODE:
        print("🎮 Loading demo data...")
        load_demo_data()
        stats = get_inventory_stats()
        print(f"📊 {stats['total_skus']} SKUs, {stats['total_on_hand']} on hand, {stats['low_stock_count']} low")
    
    # Start scheduler
    if not DEMO_MODE:
        try:
            from core.scheduler import start_scheduler
            start_scheduler()
        except ImportError:
            print("⏸️  No scheduler")
    else:
        print("⏸️  Scheduler disabled")
    
    # Get port from environment
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    # Start ngrok tunnel if enabled
    ngrok_tunnel = None
    if os.getenv('ENABLE_NGROK', 'false').lower() == 'true':
        try:
            from ngrok_manager import start_ngrok_with_flask
            RESERVED_DOMAIN = os.getenv('NGROK_DOMAIN', 'unenriching-janice-unpermanent.ngrok-free.dev')
            ngrok_tunnel = start_ngrok_with_flask(port=port, domain=RESERVED_DOMAIN)
        except Exception as e:
            print(f"⚠️  ngrok failed: {e}")
    
    print(f"\n🚀 http://localhost:{port} | {'DEMO' if DEMO_MODE else 'PROD'} | Debug: {debug}\n")
    
    try:
        app.run(host='0.0.0.0', port=port, debug=debug)
    finally:
        # Cleanup ngrok on exit
        if ngrok_tunnel:
            ngrok_tunnel.stop_tunnel()
