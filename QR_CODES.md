# 📱 Quick Access QR Codes

Scan these QR codes to quickly access the DonXEra Inventory Manager.

---

## 🌐 Live Demo (ngrok)

**Scan to access the live demo:**

![ngrok QR Code](docs/assets/qr_ngrok.png)

**URL:** [https://unenriching-janice-unpermanent.ngrok-free.dev](https://unenriching-janice-unpermanent.ngrok-free.dev)

- ✅ Publicly accessible
- ✅ No installation required
- ✅ Full inventory with 140+ items
- ✅ Mobile responsive

---

## 🐳 Docker Local Access

**Scan to access locally (after running Docker):**

![Docker Local QR Code](docs/assets/qr_docker.png)

**URL:** http://localhost:8000

### Quick Start with Docker

**Scan for Docker run command:**

![Docker Command QR Code](docs/assets/qr_docker_command.png)

Or copy/paste:

```bash
docker run -p 8000:8000 -e DEMO_MODE=false donxera-inventory
```

Then scan the **Docker Local QR Code** above to access on your phone.

---

## 📋 Features Available

Both access methods provide:

- ✅ **140+ inventory items** (Clothing & Sneakers)
- ✅ **Category filtering** (All Items, Clothing, Sneakers)
- ✅ **Search functionality** (by name, SKU, color)
- ✅ **Size availability** (hover on desktop, tap on mobile)
- ✅ **Stock status indicators** (In Stock, Low Stock, Out of Stock)
- ✅ **Export to CSV**
- ✅ **Mobile responsive design**

### Brands Included

**Clothing:**
- Hellstar, Denim Tears, Vlone, Bape, Corteiz
- Essential Fear of God, Sp5der, Stussy, Trapstar

**Sneakers:**
- Travis Scott Jordans, Nike Dunk Low Panda
- Air Jordan 1 Chicago, Air Jordan 4 Military Black
- Yeezy Slides & Foam Runners, New Balance 550/2002R
- Nike Air Force 1, Vans Old Skool, Converse Chuck Taylor

---

## 🔧 Troubleshooting

### ngrok Access
- If ngrok link doesn't work, the tunnel may be down
- Check [NGROK_SETUP.md](NGROK_SETUP.md) for restarting

### Docker Access
- Ensure Docker is running: `docker ps`
- Check port 8000 is free: `lsof -i :8000`
- Access from same network (or use ngrok for remote access)

---

## 📸 Screenshots

| Desktop View | Mobile View |
|--------------|-------------|
| ![Dashboard](docs/assets/dashboard.png) | ![Inventory](docs/assets/health.png) |

---

**Built with:** Python • Flask • Bootstrap • Pandas

**Repository:** [as4584/Item_manager](https://github.com/as4584/Item_manager)
