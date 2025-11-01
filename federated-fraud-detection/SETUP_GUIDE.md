# Complete Setup Guide

## 📋 Prerequisites

### Required Software

1. **Python 3.10 or higher**
   ```bash
   python3 --version  # Should be 3.10+
   ```

2. **Node.js 18 or higher**
   ```bash
   node --version  # Should be 18+
   npm --version
   ```

3. **pip (Python package manager)**
   ```bash
   pip --version
   ```

### System Requirements

- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: 2GB free space
- **OS**: macOS, Linux, or Windows (with WSL)

## 🔧 Installation Steps

### Step 1: Clone or Download Project

```bash
cd ~/Documents/sunny
# Project should be in: federated-fraud-detection/
```

### Step 2: Backend Setup

#### 2.1 Navigate to Backend
```bash
cd federated-fraud-detection/backend
```

#### 2.2 Create Virtual Environment
```bash
python3 -m venv venv
```

#### 2.3 Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

#### 2.4 Upgrade pip
```bash
pip install --upgrade pip
```

#### 2.5 Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- TensorFlow 2.15.0
- TensorFlow Federated 0.60.0
- FastAPI 0.104.1
- And all other dependencies

**Note for Mac M1/M2 users:**
If you encounter TensorFlow issues:
```bash
pip install tensorflow-macos tensorflow-metal
```

#### 2.6 Verify Installation
```bash
python -c "import tensorflow as tf; print(f'TensorFlow {tf.__version__}')"
python -c "import fastapi; print(f'FastAPI {fastapi.__version__}')"
```

### Step 3: Frontend Setup

#### 3.1 Navigate to Frontend
```bash
cd ../frontend  # From backend directory
# Or: cd federated-fraud-detection/frontend
```

#### 3.2 Install Dependencies
```bash
npm install
```

This will install:
- React 18.2.0
- Material-UI 5.14.20
- Plotly.js 2.27.1
- D3.js 7.8.5
- And all other dependencies

**If you encounter peer dependency issues:**
```bash
npm install --legacy-peer-deps
```

#### 3.3 Verify Installation
```bash
npm list react plotly.js d3
```

### Step 4: Validate System

Run the validation script:
```bash
cd ..  # Back to project root
python3 test_system.py
```

You should see:
```
✓ TensorFlow
✓ NumPy
✓ Pandas
✓ FastAPI
✓ Generated data
✓ Model created
...
🎉 All tests passed! System is ready to run.
```

## 🚀 Running the Application

### Method 1: Using Scripts (Recommended)

#### Terminal 1 - Backend
```bash
cd federated-fraud-detection
./start_backend.sh
```

Wait for:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

#### Terminal 2 - Frontend
```bash
cd federated-fraud-detection
./start_frontend.sh
```

Wait for:
```
  VITE v5.0.8  ready in XXX ms
  ➜  Local:   http://localhost:5173/
```

### Method 2: Manual Start

#### Backend
```bash
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd frontend
npm run dev
```

## 🌐 Accessing the Application

1. **Frontend Dashboard**: http://localhost:5173
2. **Backend API**: http://localhost:8000
3. **API Documentation**: http://localhost:8000/docs

## 🧪 Testing the System

### 1. Test Backend Health

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status": "healthy"}
```

### 2. Test API Status

```bash
curl http://localhost:8000/api/status
```

### 3. Start Training via API

```bash
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

### 4. Test Frontend

1. Open http://localhost:5173
2. Navigate to **Training Control**
3. Click **Start Training**
4. Monitor progress in **Dashboard**

## 🔍 Troubleshooting

### Backend Issues

#### Issue: Port 8000 already in use
```bash
# Find and kill process
lsof -ti:8000 | xargs kill -9

# Or use different port
uvicorn app.main:app --port 8001
```

#### Issue: TensorFlow import error
```bash
# Reinstall TensorFlow
pip uninstall tensorflow
pip install tensorflow==2.15.0

# For Mac M1/M2
pip install tensorflow-macos tensorflow-metal
```

#### Issue: Module not found
```bash
# Ensure you're in backend directory
cd backend
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue: Permission denied
```bash
chmod +x start_backend.sh
```

### Frontend Issues

#### Issue: Port 5173 already in use
```bash
# Kill process
lsof -ti:5173 | xargs kill -9
```

#### Issue: Module not found
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

#### Issue: Plotly errors
```bash
npm install plotly.js react-plotly.js --legacy-peer-deps
```

#### Issue: Vite errors
```bash
npm install vite@latest --save-dev
```

### Common Issues

#### Issue: CORS errors
- Ensure backend is running on port 8000
- Check `vite.config.js` proxy settings
- Restart both backend and frontend

#### Issue: Training fails
- Check backend logs for errors
- Verify data generation works: `python backend/data/synthetic_generator.py`
- Ensure sufficient RAM (8GB minimum)

#### Issue: Slow training
- Reduce `n_rounds` or `n_clients`
- Use smaller `batch_size`
- This is normal for first run (data generation)

## 📊 Performance Optimization

### For Faster Training

1. **Reduce complexity:**
```python
config = {
    "n_clients": 3,      # Instead of 5
    "n_rounds": 5,       # Instead of 10
    "local_epochs": 3,   # Instead of 5
}
```

2. **Use GPU (if available):**
```bash
# Check GPU availability
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

3. **Increase batch size:**
```python
"batch_size": 64  # Instead of 32 (if RAM allows)
```

### For Better Results

1. **More training rounds:**
```python
"n_rounds": 15  # Instead of 10
```

2. **More clients:**
```python
"n_clients": 7  # Instead of 5
```

3. **Adjust privacy parameters:**
```python
# In backend/app/privacy.py
noise_multiplier=0.9  # Less noise, less privacy, better accuracy
```

## 🔐 Security Notes

### For Development

- Default settings are for local development
- CORS is open (`allow_origins=["*"]`)
- No authentication required

### For Production

Before deploying to production:

1. **Update CORS settings** in `backend/app/main.py`:
```python
allow_origins=["https://yourdomain.com"]
```

2. **Add authentication** to API endpoints

3. **Use HTTPS** for all connections

4. **Set environment variables**:
```bash
export API_SECRET_KEY="your-secret-key"
export DATABASE_URL="your-database-url"
```

5. **Enable rate limiting**

## 📝 Environment Variables

Create `.env` file in backend directory:

```bash
# Backend settings
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Training settings
DEFAULT_CLIENTS=5
DEFAULT_ROUNDS=10

# Privacy settings
DEFAULT_EPSILON=3.0
DEFAULT_NOISE_MULTIPLIER=1.1
```

Create `.env` file in frontend directory:

```bash
# API endpoint
VITE_API_BASE=http://localhost:8000/api
```

## 🎓 Next Steps

After successful setup:

1. **Read the README.md** for detailed documentation
2. **Explore the code** in `backend/` and `frontend/src/`
3. **Run training** with different configurations
4. **Test privacy attacks** in Attack Simulation page
5. **Modify the model** in `backend/models/fraud_model.py`
6. **Experiment with privacy parameters**

## 📚 Additional Resources

- **TensorFlow Federated**: https://www.tensorflow.org/federated
- **TensorFlow Privacy**: https://github.com/tensorflow/privacy
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **React Docs**: https://react.dev/
- **Material-UI**: https://mui.com/

## 💡 Tips

1. **First training takes longer** (5-10 minutes) due to data generation
2. **Subsequent trainings are faster** (3-5 minutes)
3. **Use smaller configurations** for testing
4. **Monitor backend logs** for detailed progress
5. **Check browser console** for frontend errors

## 🆘 Getting Help

If you encounter issues:

1. Check this guide's troubleshooting section
2. Review backend logs in terminal
3. Check browser console for frontend errors
4. Verify all dependencies are installed
5. Try running `test_system.py` again

---

**Setup complete! Ready to explore privacy-preserving federated learning! 🚀**
