# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Option 1: Using Scripts (Recommended)

#### Terminal 1 - Backend
```bash
cd federated-fraud-detection
chmod +x start_backend.sh
./start_backend.sh
```

#### Terminal 2 - Frontend
```bash
cd federated-fraud-detection
chmod +x start_frontend.sh
./start_frontend.sh
```

### Option 2: Manual Setup

#### Backend Setup

1. **Navigate and create virtual environment:**
```bash
cd federated-fraud-detection/backend
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Start backend:**
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend running at: http://localhost:8000

#### Frontend Setup

1. **Navigate and install:**
```bash
cd federated-fraud-detection/frontend
npm install
```

2. **Start frontend:**
```bash
npm run dev
```

✅ Frontend running at: http://localhost:5173

## 📊 Using the Application

### Step 1: Access Dashboard
Open http://localhost:5173 in your browser

### Step 2: Start Training
1. Click **Training Control** in sidebar
2. Configure parameters (or use defaults):
   - Clients: 5
   - Rounds: 10
   - Local Epochs: 5
   - Batch Size: 32
   - ✓ Differential Privacy
   - ✓ Secure Aggregation
3. Click **Start Training**
4. Wait 5-10 minutes for training to complete

### Step 3: View Results
- **Dashboard**: Overall metrics and comparison
- **Institutions**: See individual bank data
- **Performance**: Training progress charts
- **Privacy**: Privacy mechanisms visualization
- **Attack Simulation**: Test privacy defenses

## 🎯 Expected Results

After training completes, you should see:

- **Federated AUC**: ~0.92 (vs Local: ~0.84)
- **F1 Score**: ~0.85 (vs Local: ~0.72)
- **Privacy Budget (ε)**: ~2.3 (target: ≤ 3.0)
- **Defense Rate**: ~90%

## 🔧 Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

**Import errors:**
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

**TensorFlow issues:**
```bash
# For Mac M1/M2
pip install tensorflow-macos tensorflow-metal
```

### Frontend Issues

**Port already in use:**
```bash
# Kill process on port 5173
lsof -ti:5173 | xargs kill -9
```

**Module not found:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Plotly issues:**
```bash
npm install plotly.js react-plotly.js --legacy-peer-deps
```

## 📝 API Testing

Test backend directly:

```bash
# Health check
curl http://localhost:8000/health

# Get status
curl http://localhost:8000/api/status

# Start training (after backend is ready)
curl -X POST http://localhost:8000/api/train \
  -H "Content-Type: application/json" \
  -d '{
    "n_clients": 5,
    "n_rounds": 5,
    "local_epochs": 3,
    "batch_size": 32,
    "use_dp": true,
    "use_secure_agg": true
  }'
```

## 🎓 Next Steps

1. **Experiment with parameters**: Try different privacy settings
2. **Test predictions**: Use the prediction API
3. **Run attack simulations**: Test privacy defenses
4. **Analyze results**: Compare federated vs local models
5. **Modify architecture**: Edit `fraud_model.py` to try different models

## 📚 Learn More

- Full documentation: See `README.md`
- API docs: http://localhost:8000/docs
- Code examples: Check `backend/app/trainer.py`

---

**Need help?** Check the main README.md or open an issue.
