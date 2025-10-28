#!/bin/bash
# Docker Setup Verification Script

echo "🖤 DonXEra Inventory - Docker Verification"
echo "=========================================="
echo ""

# Check Docker
echo "1️⃣ Checking Docker installation..."
if command -v docker &> /dev/null; then
    echo "   ✅ Docker is installed"
    docker --version
else
    echo "   ❌ Docker is NOT installed"
    echo "   📥 Install from: https://docs.docker.com/get-docker/"
    exit 1
fi
echo ""

# Check Dockerfile
echo "2️⃣ Checking Dockerfile..."
if [ -f "Dockerfile" ]; then
    echo "   ✅ Dockerfile found"
else
    echo "   ❌ Dockerfile not found"
    exit 1
fi
echo ""

# Check .dockerignore
echo "3️⃣ Checking .dockerignore..."
if [ -f ".dockerignore" ]; then
    echo "   ✅ .dockerignore found"
else
    echo "   ⚠️  .dockerignore not found (optional)"
fi
echo ""

# Check required files
echo "4️⃣ Checking required files..."
files=("app.py" "requirements.txt" "demo_data.py" "sample_data/products.csv")
all_present=true
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file NOT FOUND"
        all_present=false
    fi
done
echo ""

if [ "$all_present" = false ]; then
    echo "❌ Some required files are missing!"
    exit 1
fi

# Check templates
echo "5️⃣ Checking templates..."
if [ -d "templates" ]; then
    echo "   ✅ templates/ directory found"
    template_count=$(ls -1 templates/*.html 2>/dev/null | wc -l)
    echo "   📄 Found $template_count HTML templates"
else
    echo "   ❌ templates/ directory not found"
    exit 1
fi
echo ""

# Check static files
echo "6️⃣ Checking static files..."
if [ -d "static" ]; then
    echo "   ✅ static/ directory found"
    if [ -f "static/style.css" ]; then
        echo "   ✅ style.css found"
    fi
    if [ -f "static/app.js" ]; then
        echo "   ✅ app.js found"
    fi
else
    echo "   ⚠️  static/ directory not found (optional)"
fi
echo ""

echo "✅ All checks passed!"
echo ""
echo "🚀 Ready to build Docker image!"
echo ""
echo "Next steps:"
echo "  1. Build: docker build -t donxera-inventory ."
echo "  2. Run:   docker run -p 8000:8000 donxera-inventory"
echo "  3. Open:  http://localhost:8000"
echo ""
echo "Or use the build script:"
echo "  ./docker-build.sh"
