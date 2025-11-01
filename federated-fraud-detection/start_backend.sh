#!/bin/bash

echo "=========================================="
echo "Federated Fraud Detection - Backend Setup"
echo "=========================================="

cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Create results directory
mkdir -p results

echo ""
echo "=========================================="
echo "Starting FastAPI Backend Server..."
echo "=========================================="
echo "API: http://localhost:8000"
echo "Docs: http://localhost:8000/docs"
echo "=========================================="
echo ""

# Start the server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
