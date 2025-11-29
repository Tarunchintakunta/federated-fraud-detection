#!/bin/bash
# Script to download Kaggle Credit Card Fraud Detection dataset

echo "=========================================="
echo "Kaggle Dataset Download Script"
echo "=========================================="
echo ""

# Check if kaggle is installed
if ! command -v kaggle &> /dev/null; then
    echo "Installing kaggle package..."
    pip install kaggle
fi

# Check for kaggle credentials
if [ ! -f ~/.kaggle/kaggle.json ]; then
    echo "ERROR: Kaggle API credentials not found!"
    echo ""
    echo "Please set up Kaggle API credentials:"
    echo "1. Go to https://www.kaggle.com/account"
    echo "2. Scroll to 'API' section and click 'Create New API Token'"
    echo "3. Place the downloaded kaggle.json in ~/.kaggle/"
    echo "4. Run: chmod 600 ~/.kaggle/kaggle.json"
    echo ""
    exit 1
fi

# Download dataset
echo "Downloading Credit Card Fraud Detection dataset..."
cd backend/data
python download_kaggle_dataset.py

echo ""
echo "=========================================="
echo "Download complete!"
echo "=========================================="
