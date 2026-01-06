#!/bin/bash

echo "=========================================="
echo "Federated Fraud Detection - Backend Setup"
echo "=========================================="

cd backend

# Activate Conda environment
echo "Activating Conda environment..."
source ~/miniconda3/etc/profile.d/conda.sh
conda activate tf_env

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
