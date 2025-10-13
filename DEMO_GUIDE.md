# 🎮 DEMO MODE - Inventory Manager Testing Guide

## 🚀 Server Running
**URL**: http://localhost:8082  
**Mode**: DEMO (using sample data from `/sample_data/products.csv`)  
**Data**: 50 SKUs, 557 items on hand, 17 low stock items

---

## 📍 Available Pages

### 1. Dashboard (`/`)
- **Total SKUs**: 50 products
- **Total On Hand**: 557 items
- **Low Stock Count**: 17 items (≤ 5 units)
- **Total Inventory Value**: Calculated from prices

### 2. Inventory (`/inventory`)
- View all 50 products with full details
- Sortable table (click column headers)
- Searchable (use browser search Ctrl+F)
- Columns: ItemID, SKU, Name, Category, Color, Size, Barcode, Price, QtyOnHand, QtySold, Location, LastUpdated

### 3. Low Stock (`/low-stock`)
- Shows items with ≤ 5 units
- Automatic restock list
- Currently 17 items need restocking

---

## 🔧 API Endpoints for Testing

### Update Stock (Demo Mode Only)
Update the quantity of any item:

```bash
# Update item 1001 to 50 units
curl -X POST http://localhost:8082/update-stock \
  -H "Content-Type: application/json" \
  -d '{"item_id": 1001, "quantity": 50}'

# Update item 1010 to 0 units (out of stock)
curl -X POST http://localhost:8082/update-stock \
  -H "Content-Type: application/json" \
  -d '{"item_id": 1010, "quantity": 0}'

# Update item 1007 to 2 units (low stock)
curl -X POST http://localhost:8082/update-stock \
  -H "Content-Type: application/json" \
  -d '{"item_id": 1007, "quantity": 2}'
```

### Reload Demo Data
Reset all data back to original:

```bash
curl -X POST http://localhost:8082/sync
```

### Version Info
```bash
curl http://localhost:8082/version
# Returns: {"version": "1.0.0", "name": "Self-Managing Inventory Manager", "python": "3.11.x"}
```

### Health Check
```bash
curl http://localhost:8082/health
# Returns: {"status": "healthy", "version": "1.0.0"}
```

---

## 📦 Sample Products in Demo

### High Stock Items (Good)
- **1001**: Air Jordan 1 Black, Size 8 - **12 units**
- **1002**: Air Jordan 1 Black, Size 9 - **15 units**
- **1011**: Air Force 1 White, Size 8 - **20 units**
- **1013**: Air Force 1 White, Size 10 - **25 units**

### Low Stock Items (Need Restocking)
- **1005**: Air Jordan 1 Black, Size 12 - **4 units** ⚠️
- **1007**: Air Jordan 1 White, Size 9 - **3 units** ⚠️
- **1008**: Air Jordan 1 White, Size 10 - **2 units** ⚠️
- **1010**: Air Jordan 1 White, Size 12 - **1 unit** ⚠️
- **1018**: Air Force 1 Black, Size 11 - **0 units** ❌ OUT OF STOCK

### Product Categories
- Sneakers (Air Jordan 1, Air Force 1, Yeezy 350 Boost)
- Apparel (Nike Hoodies, Champion T-Shirts, Levi's Jeans)
- Accessories (Caps, Beanies, Belts)

---

## 🧪 Test Scenarios

### Scenario 1: Restock Low Items
1. View `/low-stock` page (17 items shown)
2. Update item 1010 (Air Jordan 1 White Size 12):
   ```bash
   curl -X POST http://localhost:8082/update-stock \
     -H "Content-Type: application/json" \
     -d '{"item_id": 1010, "quantity": 20}'
   ```
3. Refresh `/low-stock` - item 1010 should no longer appear
4. Check `/inventory` - quantity updated to 20

### Scenario 2: Simulate Sales
1. View item 1001 (Air Jordan 1 Black Size 8) - currently **12 units**
2. Reduce quantity to simulate 5 sales:
   ```bash
   curl -X POST http://localhost:8082/update-stock \
     -H "Content-Type: application/json" \
     -d '{"item_id": 1001, "quantity": 7}'
   ```
3. Refresh dashboard - "Total On Hand" decreased
4. Check `/inventory` - item 1001 now shows 7 units

### Scenario 3: Create Low Stock Alert
1. Pick a high-stock item (e.g., 1011 - 20 units)
2. Reduce to below threshold:
   ```bash
   curl -X POST http://localhost:8082/update-stock \
     -H "Content-Type: application/json" \
     -d '{"item_id": 1011, "quantity": 3}'
   ```
3. Refresh `/low-stock` - item 1011 now appears in restock list
4. Dashboard "Low Stock Count" increases

### Scenario 4: Out of Stock
1. Set any item to 0:
   ```bash
   curl -X POST http://localhost:8082/update-stock \
     -H "Content-Type: application/json" \
     -d '{"item_id": 1018, "quantity": 0}'
   ```
2. Item appears in low stock with 0 units
3. Visual indicator (red/critical)

### Scenario 5: Reset Everything
```bash
curl -X POST http://localhost:8082/sync
```
All data reloads from `/sample_data/products.csv`

---

## 🎨 UI Features to Test

### Dashboard
- ✅ Total SKUs tile
- ✅ Total On Hand tile
- ✅ Low Stock Count tile (color-coded)
- ✅ Last Sync timestamp
- ✅ Quick navigation buttons

### Inventory Page
- ✅ Sortable columns (click header to sort)
- ✅ Search functionality (browser Ctrl+F)
- ✅ Responsive table design
- ✅ Color-coded stock levels (red < 5, yellow < 10, green ≥ 10)
- ✅ Pagination (if > 100 items)

### Low Stock Page
- ✅ Filtered list (only items ≤ 5)
- ✅ Restock recommendations
- ✅ Priority indicators
- ✅ Quick reorder actions

---

## 🔍 What Changed?

### New in This Demo
1. **Demo Mode**: Uses sample data instead of Google Sheets/Lightspeed API
2. **Update Stock Endpoint**: `/update-stock` to modify quantities on-the-fly
3. **Real-time Stats**: Dashboard pulls live data from demo inventory
4. **Dynamic Low Stock**: Automatically recalculates based on threshold (5 units)
5. **Version Endpoint**: `/version` shows app version info
6. **Health Endpoint**: `/health` for monitoring

### Sample Data
- **50 products** loaded from `sample_data/products.csv`
- **3 categories**: Sneakers, Apparel, Accessories
- **10+ locations**: A1, A2, B1, B2, C1, C2, etc.
- **Price range**: $25 - $220
- **Stock range**: 0 - 30 units

---

## 📝 Item IDs for Quick Testing

| Item ID | Product | Size | Current Stock | Status |
|---------|---------|------|---------------|--------|
| 1001 | Air Jordan 1 Black | 8 | 12 | ✅ Good |
| 1002 | Air Jordan 1 Black | 9 | 15 | ✅ Good |
| 1005 | Air Jordan 1 Black | 12 | 4 | ⚠️ Low |
| 1007 | Air Jordan 1 White | 9 | 3 | ⚠️ Low |
| 1008 | Air Jordan 1 White | 10 | 2 | ⚠️ Low |
| 1010 | Air Jordan 1 White | 12 | 1 | ❌ Critical |
| 1011 | Air Force 1 White | 8 | 20 | ✅ Good |
| 1018 | Air Force 1 Black | 11 | 0 | ❌ Out of Stock |
| 1019 | Yeezy 350 Boost | 8 | 5 | ⚠️ Threshold |
| 1025 | Nike Hoodie | M | 8 | ✅ Good |

---

## 🛑 Stop Server

```bash
# Stop the Flask server
pkill -f "python3 app.py"
```

---

## 💡 Tips
- Refresh pages after updating stock to see changes
- Dashboard stats update in real-time
- Low stock threshold is 5 units (configurable in production)
- Demo mode doesn't persist changes (reloads from CSV on restart)
- Use browser DevTools (F12) to see API responses

---

**Enjoy testing! 🎉**
