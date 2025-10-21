#!/bin/bash
set -e

echo "🔄 Starting src/ layout refactor..."

# Create all directories
echo "📁 Creating directory structure..."
mkdir -p src/app/routes src/core src/services/lightspeed src/services/sheets
mkdir -p src/domain/models src/ingestion scripts deploy/docker config

# Move files with git mv
echo "📦 Moving files..."

# Templates and static
git mv templates src/app/templates
git mv static src/app/static

# Lightspeed services
git mv ls_api.py src/services/lightspeed/api.py
git mv ls_auth.py src/services/lightspeed/auth.py  
git mv ls_webhooks.py src/services/lightspeed/webhooks.py

# Sheets service
git mv sheets.py src/services/sheets/service.py

# Domain
git mv inventory.py src/domain/inventory.py
git mv models/database.py src/domain/models/database.py
rm -f models/__init__.py
rmdir models

# Ingestion
git mv csv_ingest.py src/ingestion/csv_ingest.py
git mv demo_data.py src/ingestion/demo_data.py

# Core
git mv scheduler.py src/core/scheduler.py

# Version
git mv __version__.py src/__version__.py

# Config files
git mv .env.example config/.env.example
git mv .env.docker config/.env.docker

# Docker files
git mv Dockerfile deploy/docker/Dockerfile
git mv .dockerignore deploy/docker/.dockerignore
git mv DOCKER_README.md deploy/docker/README.md
git mv docker-build.sh deploy/docker/build.sh
chmod +x deploy/docker/build.sh
git mv verify-docker-setup.sh deploy/docker/verify-setup.sh
chmod +x deploy/docker/verify-setup.sh

# Move main app
git mv app.py scripts/run_local.py

echo "✅ Files moved successfully!"
