#!/bin/bash
# Setup script for AI Agent Security competition
# Run this after cloning to set up your environment

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

echo "=== AI Agent Security Competition Setup ==="

# 1. Create virtual environment if not exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# 2. Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# 3. Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Check for Kaggle credentials
echo ""
echo "=== Kaggle Setup ==="
if [ -f "$HOME/.kaggle/kaggle.json" ] || [ -f "$HOME/.kaggle/access_token" ]; then
    echo "Kaggle credentials found!"
else
    echo "Kaggle credentials NOT found."
    echo ""
    echo "Option A (OAuth - recommended):"
    echo "  source .venv/bin/activate"
    echo "  kaggle auth login"
    echo ""
    echo "Option B (API token):"
    echo "  1. Go to https://www.kaggle.com/settings/api"
    echo "  2. Click 'Generate New Token'"
    echo "  3. Save the downloaded kaggle.json to ~/.kaggle/"
    echo "  4. chmod 600 ~/.kaggle/kaggle.json"
fi

# 5. Download competition data if credentials available
echo ""
echo "=== Competition Data ==="
if command -v kaggle &> /dev/null && ([ -f "$HOME/.kaggle/kaggle.json" ] || [ -f "$HOME/.kaggle/access_token" ]); then
    echo "Downloading competition data..."
    mkdir -p data/raw
    kaggle competitions download -c ai-agent-security-multi-step-tool-attacks -p data/raw/
    cd data/raw/
    unzip -o ai-agent-security-multi-step-tool-attacks.zip 2>/dev/null || true
    cd "$PROJECT_DIR"
    echo "Competition data downloaded to data/raw/"
else
    echo "Skip downloading. Set up Kaggle credentials first."
fi

# 6. Install competition SDK if wheel exists
echo ""
echo "=== Competition SDK ==="
SDK_WHEEL=$(find . -name "aicomp_sdk*.whl" 2>/dev/null | head -1)
if [ -n "$SDK_WHEEL" ]; then
    echo "Installing SDK from: $SDK_WHEEL"
    pip install "$SDK_WHEEL"
else
    echo "SDK wheel not found yet. Will be available after downloading competition data."
fi

echo ""
echo "=== Setup Complete ==="
echo "Activate your environment with: source .venv/bin/activate"
echo "Run the smoke test with: python tests/smoke_test.py"
