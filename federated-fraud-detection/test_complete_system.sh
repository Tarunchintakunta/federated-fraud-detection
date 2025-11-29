#!/bin/bash
echo "=========================================="
echo "COMPLETE SYSTEM TEST"
echo "=========================================="

cd backend
source ../venv/bin/activate

echo ""
echo "1. Testing Backend Server..."
uvicorn app.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

echo "2. Testing API Endpoints..."
curl -s http://127.0.0.1:8000/api/status | head -5
echo ""

echo "3. Stopping server..."
kill $SERVER_PID

echo ""
echo "✓ System test complete!"
