# ngrok Integration Setup

Your Flask app is now configured to automatically start with ngrok!

## 🎯 Quick Start

### Option 1: Automatic (Recommended)
```bash
./scripts/start_with_ngrok.sh
```

This will:
- ✅ Start Flask on port 5000
- ✅ Automatically start ngrok tunnel  
- ✅ Use your reserved domain: `unenriching-janice-unpermanent.ngrok-free.dev`
- ✅ Print the public URL

### Option 2: Manual Control
```bash
# Start Flask with ngrok
PYTHONPATH=src ENABLE_NGROK=true python3 scripts/run_local.py

# Start Flask WITHOUT ngrok
PYTHONPATH=src ENABLE_NGROK=false python3 scripts/run_local.py
```

### Option 3: Test ngrok Only
```bash
python3 scripts/ngrok_manager.py
```

## ⚙️ Configuration (.env file)

```bash
# Enable/disable ngrok
ENABLE_NGROK=true

# Your ngrok authtoken (from dashboard.ngrok.com)
NGROK_AUTH_TOKEN=344s0e8OMV1TQG74funRVyfCUMq_6sDhpto4fim3KCoes29A3

# Your reserved domain
NGROK_DOMAIN=unenriching-janice-unpermanent.ngrok-free.dev

# Flask port (ngrok will tunnel to this port)
PORT=5000
```

## 📱 Usage

1. **Start the app:**
   ```bash
   ./scripts/start_with_ngrok.sh
   ```

2. **Look for the output:**
   ```
   ============================================================
   🌐 PUBLIC URL: https://unenriching-janice-unpermanent.ngrok-free.dev
   📱 Share this with your cousin!
   ============================================================
   ```

3. **Share the URL** with anyone who needs to access your app!

## 🔧 How It Works

1. **ngrok_manager.py** - Python module that:
   - Configures ngrok with your authtoken from `.env`
   - Starts ngrok tunnel with your reserved domain
   - Retrieves the public URL
   - Manages tunnel lifecycle

2. **run_local.py** - Updated to:
   - Check `ENABLE_NGROK` environment variable
   - Automatically start ngrok when enabled
   - Print the public URL
   - Clean up tunnel on exit

3. **start_with_ngrok.sh** - Convenience script that:
   - Sets all required environment variables
   - Starts everything in one command

## 🎨 Features

- ✅ **Automatic startup** - ngrok starts with Flask
- ✅ **Reserved domain** - Always same URL
- ✅ **Environment-based** - Configure via `.env`
- ✅ **Clean shutdown** - Tunnel stops when Flask stops
- ✅ **Error handling** - Falls back gracefully if ngrok fails

## 🐛 Troubleshooting

**Problem: "authentication failed"**
- Check that `NGROK_AUTH_TOKEN` in `.env` is correct
- Get fresh token from: https://dashboard.ngrok.com/get-started/your-authtoken

**Problem: "domain not found"**
- Verify your reserved domain at: https://dashboard.ngrok.com/cloud-edge/domains
- Update `NGROK_DOMAIN` in `.env` to match

**Problem: Port already in use**
- Change `PORT` in `.env` to different number (e.g., 5001, 8000)
- Make sure no other Flask app is running

**Problem: ngrok not found**
- Install: `snap install ngrok`

## 📖 Related Files

- `scripts/ngrok_manager.py` - ngrok tunnel manager
- `scripts/run_local.py` - Flask app with integrated ngrok
- `scripts/start_with_ngrok.sh` - Quick start script
- `.env` - Configuration file

## 💡 Tips

1. **Share the URL** as soon as you see it printed
2. **Keep terminal open** - closing it stops both Flask and ngrok
3. **Use reserved domain** - URL stays the same across restarts
4. **Disable in production** - Set `ENABLE_NGROK=false` when deploying

---

**Your Public URL:** https://unenriching-janice-unpermanent.ngrok-free.dev
