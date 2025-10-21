# 🚀 Quick Start - DonXEra with Auto ngrok

## One-Command Start

```bash
./scripts/start_with_ngrok.sh
```

**That's it!** Your app will:
1. ✅ Load 60 demo products
2. ✅ Start Flask on port 5000
3. ✅ Automatically start ngrok tunnel
4. ✅ Print your public URL

## Your Public URL

**https://unenriching-janice-unpermanent.ngrok-free.dev**

Share this with anyone! Works from anywhere.

## Configuration

All settings in `.env`:
- `ENABLE_NGROK=true` - Auto-start ngrok
- `NGROK_AUTHTOKEN=your_token` - Your authtoken
- `NGROK_DOMAIN=your_domain` - Your reserved domain
- `PORT=5000` - Flask port

## Alternative Ways to Start

```bash
# Method 1: Quick script
./scripts/start_with_ngrok.sh

# Method 2: Direct
python3 scripts/run_local.py

# Method 3: With PYTHONPATH
PYTHONPATH=src python3 scripts/run_local.py

# Method 4: Without ngrok
ENABLE_NGROK=false python3 scripts/run_local.py
```

## What You'll See

```
============================================================
🌐 PUBLIC URL: https://unenriching-janice-unpermanent.ngrok-free.dev
📱 Share this with your cousin!
============================================================
```

## More Info

- **Full Guide**: `AUTO_START_NGROK_COMPLETE.md`
- **Setup Details**: `NGROK_SETUP.md`
- **Integration Info**: `NGROK_INTEGRATION_COMPLETE.md`

---

**Questions?** Check the docs or just run the script! 🎯
