"""
Demo data loader for testing the Inventory Manager UI.
Loads sample CSV data into an in-memory DataFrame for testing.
"""
import pandas as pd
from pathlib import Path

# Global in-memory inventory storage for demo mode
DEMO_INVENTORY = None

def load_demo_data():
    """Load sample inventory data from CSV for demo mode."""
    global DEMO_INVENTORY
    
    # Path to sample_data at repo root (three levels up from src/ingestion)
    csv_path = Path(__file__).parent.parent.parent / 'sample_data' / 'products.csv'
    
    if csv_path.exists():
        DEMO_INVENTORY = pd.read_csv(csv_path)
        print(f"✅ Loaded {len(DEMO_INVENTORY)} demo products")
        return DEMO_INVENTORY
    else:
        # Create minimal demo data if file doesn't exist
        DEMO_INVENTORY = pd.DataFrame({
            'ItemID': [1001, 1002, 1003, 1004, 1005],
            'SKU': ['JD1-BLK-8', 'JD1-BLK-9', 'JD1-BLK-10', 'AF1-WHT-8', 'AF1-WHT-9'],
            'Name': ['Air Jordan 1 Black', 'Air Jordan 1 Black', 'Air Jordan 1 Black', 
                     'Air Force 1 White', 'Air Force 1 White'],
            'Category': ['Sneakers'] * 5,
            'Color': ['Black', 'Black', 'Black', 'White', 'White'],
            'Size': [8, 9, 10, 8, 9],
            'Barcode': ['123456780', '123456781', '123456782', '234567801', '234567802'],
            'RetailPrice': [170.00, 170.00, 170.00, 110.00, 110.00],
            'QtyOnHand': [12, 15, 8, 3, 2],
            'QtySold': [8, 12, 22, 35, 40],
            'Location': ['A1', 'A1', 'A1', 'B1', 'B1'],
            'LastUpdated': ['2025-10-10 12:00:00'] * 5
        })
        print(f"✅ Created {len(DEMO_INVENTORY)} demo products (CSV not found)")
        return DEMO_INVENTORY

def get_demo_inventory():
    """Get the current demo inventory DataFrame."""
    global DEMO_INVENTORY
    if DEMO_INVENTORY is None:
        load_demo_data()
    return DEMO_INVENTORY.copy()

def update_demo_stock(item_id: int, new_qty: int):
    """Update stock quantity for a demo item."""
    global DEMO_INVENTORY
    if DEMO_INVENTORY is None:
        load_demo_data()
    
    mask = DEMO_INVENTORY['ItemID'] == item_id
    if mask.any():
        old_qty = DEMO_INVENTORY.loc[mask, 'QtyOnHand'].values[0]
        DEMO_INVENTORY.loc[mask, 'QtyOnHand'] = new_qty
        DEMO_INVENTORY.loc[mask, 'LastUpdated'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"✅ Updated ItemID {item_id}: {old_qty} → {new_qty}")
        return True
    return False

def get_low_stock_items(threshold: int = 5):
    """Get items below the stock threshold."""
    inventory = get_demo_inventory()
    return inventory[inventory['QtyOnHand'] <= threshold]

def get_inventory_stats():
    """Get summary statistics for the inventory."""
    inventory = get_demo_inventory()
    return {
        'total_skus': len(inventory),
        'total_on_hand': int(inventory['QtyOnHand'].sum()),
        'total_sold': int(inventory['QtySold'].sum()),
        'low_stock_count': len(inventory[inventory['QtyOnHand'] <= 5]),
        'total_value': float((inventory['QtyOnHand'] * inventory['RetailPrice']).sum()),
        'categories': inventory['Category'].unique().tolist(),
        'locations': inventory['Location'].unique().tolist()
    }
