#!/bin/bash

echo "=========================================="
echo "Federated Fraud Detection - Frontend Setup"
echo "=========================================="

cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
fi

echo ""
echo "=========================================="
echo "Starting React Development Server..."
echo "=========================================="
echo "Frontend: http://localhost:5173"
echo "=========================================="
echo ""

# Start the development server
npm run dev
