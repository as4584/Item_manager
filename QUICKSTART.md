# 🖤 DonXEra Inventory - Quick Reference

## One-Command Demo

```bash
docker run -p 8080:8080 donxera-inventory
```

Open: **http://localhost:8080**

---

## Build & Run

```bash
# Build
docker build -t donxera-inventory .

# Run
docker run -p 8080:8080 donxera-inventory

# Run in background
docker run -d -p 8080:8080 --name donxera donxera-inventory

# View logs
docker logs donxera

# Stop
docker stop donxera
```

---

## Manual Setup (No Docker)

```bash
pip install -r requirements.txt
DEMO_MODE=true PORT=8080 python3 app.py
```

---

## Features

- ✅ Dashboard with inventory stats
- ✅ Search & filter products
- ✅ Low stock alerts
- ✅ CSV import/export
- ✅ 60 demo products (streetwear brands)
- ✅ Minimalist design

---

## Demo Data

**Brands:** Hellstar, Denim Tears, Bape, Corteiz, Essentials, Sp5der  
**Categories:** Clothing, Sneakers, Accessories  
**Stock:** 334 units | 36 low stock  
**Price Range:** $35 - $850

---

## Endpoints

- `/` - Dashboard
- `/inventory` - All products
- `/low-stock` - Items needing restock
- `/health` - Health check
- `/version` - Version info

---

## Share Image

```bash
# Export
docker save donxera-inventory > donxera.tar

# Import on another machine
docker load < donxera.tar
docker run -p 8080:8080 donxera-inventory
```

---

**Docs:** See `DOCKER_README.md` for complete guide
