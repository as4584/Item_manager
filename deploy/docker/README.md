# 🖤 DonXEra Inventory Manager - Docker Demo

A minimalist inventory management system for streetwear and sneaker shops. Clean design, simple interface, powerful features.

## 🚀 Quick Start (Docker)

Run the demo with one command:

```bash
docker run -p 8080:8080 donxera-inventory
```

Then open your browser to: **http://localhost:8080**

---

## 📦 Setup Instructions

### Prerequisites
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- That's it!

### Build the Image

```bash
# Clone or download the repository
cd inventory_manager

# Build the Docker image
docker build -t donxera-inventory .
```

### Run the Container

```bash
# Run on default port 8080
docker run -p 8080:8080 donxera-inventory

# Or run on a different port (e.g., 3000)
docker run -p 3000:8080 donxera-inventory
```

### Run in Background

```bash
# Detached mode (runs in background)
docker run -d -p 8080:8080 --name donxera donxera-inventory

# View logs
docker logs donxera

# Stop container
docker stop donxera

# Remove container
docker rm donxera
```

---

## 🎯 What's Included

### Demo Data
- **60 products** pre-loaded with Miami streetwear brands:
  - Hellstar hoodies & tees
  - Denim Tears pieces
  - Bape collections
  - Graphic tees
  - Sneakers (Travis Scott, Yeezys, Dunks, New Balance)
  - Accessories

### Features
- ✅ **Dashboard** - Overview of inventory stats
- ✅ **Inventory View** - Search, sort, filter all products
- ✅ **Low Stock Alerts** - Items needing restock
- ✅ **CSV Upload** - Import inventory data
- ✅ **Responsive Design** - Works on desktop & mobile

---

## 📱 Usage Examples

### View Dashboard
Navigate to `http://localhost:8080/` to see:
- Product types count
- Items in stock
- Low stock alerts
- Quick actions

### Browse Inventory
Go to `http://localhost:8080/inventory` to:
- Search products by name, code, or category
- Filter by category (Clothing, Sneakers, Accessories)
- Filter by stock level (In Stock, Low Stock, Out of Stock)
- Sort by any column

### Check Low Stock
Visit `http://localhost:8080/low-stock` to:
- See items below threshold (default: 5 units)
- View priority levels (Critical, High, Medium)
- Export restock list

### API Endpoints

```bash
# Health check
curl http://localhost:8080/health

# Version info
curl http://localhost:8080/version

# Update stock (demo mode)
curl -X POST http://localhost:8080/update-stock \
  -H "Content-Type: application/json" \
  -d '{"sku": "HS-001-M", "quantity": 10}'
```

---

## 🛠️ Configuration

### Environment Variables

```bash
# Run with custom settings
docker run -p 8080:8080 \
  -e DEMO_MODE=true \
  -e PORT=8080 \
  donxera-inventory
```

### Port Mapping

```bash
# Map container port 8080 to host port 3000
docker run -p 3000:8080 donxera-inventory
# Access at: http://localhost:3000
```

---

## 📊 Demo Data Overview

**Categories:**
- Clothing (Hoodies, Tees, Pants, Jeans)
- Sneakers (Jordans, Dunks, Yeezys, New Balance)
- Accessories (Masks, Hats, Sunglasses, Jewelry)

**Stock Levels:**
- In Stock: 334 units across all products
- Low Stock: 36 items need restocking
- Product Types: 60 unique SKUs

**Price Range:**
- Budget: $35-$48 (Graphic tees, accessories)
- Mid-range: $85-$180 (Hoodies, sneakers)
- Premium: $250-$850 (Bape Shark, Travis Scott, Denim Tears)

---

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Check what's using port 8080
lsof -i :8080

# Use a different port
docker run -p 8181:8080 donxera-inventory
```

### Container Won't Start
```bash
# Check logs
docker logs <container-id>

# Remove old containers
docker container prune

# Rebuild image
docker build --no-cache -t donxera-inventory .
```

### Can't Access in Browser
- Make sure container is running: `docker ps`
- Check correct port mapping: `docker ps` shows port mapping
- Try `http://127.0.0.1:8080` instead of `localhost`

---

## 🎨 Design Philosophy

**DonXEra** follows minimalist design principles:
- Clean white background
- Black & grey color scheme
- Subtle shadows and borders
- Professional typography
- Focus on content, not decoration

---

## 📝 Notes

- **Demo Mode**: This runs with sample data only (no database required)
- **No Data Persistence**: Restart = fresh demo data
- **Production**: Not recommended for production use without modifications
- **Image Size**: ~150-200MB (Python 3.11 slim base)

---

## 🚢 Sharing the Image

### Save Image to File
```bash
# Export image
docker save donxera-inventory > donxera-inventory.tar

# Compress (optional)
gzip donxera-inventory.tar
```

### Load Image on Another Machine
```bash
# Load image
docker load < donxera-inventory.tar

# Or from compressed
gunzip -c donxera-inventory.tar.gz | docker load

# Run it
docker run -p 8080:8080 donxera-inventory
```

### Push to Docker Hub (Optional)
```bash
# Tag image
docker tag donxera-inventory yourusername/donxera-inventory:latest

# Login
docker login

# Push
docker push yourusername/donxera-inventory:latest

# Others can pull and run
docker run -p 8080:8080 yourusername/donxera-inventory:latest
```

---

## 📄 License

Demo project for educational purposes.

---

## 🤝 Support

For issues or questions:
1. Check logs: `docker logs <container-name>`
2. Verify port availability
3. Ensure Docker is running
4. Try rebuilding the image

---

**Built with Flask • Powered by Python • Designed for Simplicity**
