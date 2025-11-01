# Visual Guide: Federated Fraud Detection System

## 📂 Complete Project Structure

```
federated-fraud-detection/
│
├── 📄 README.md                    # Main documentation (200+ lines)
├── 📄 QUICKSTART.md                # 5-minute getting started
├── 📄 SETUP_GUIDE.md               # Detailed setup instructions
├── 📄 PROJECT_SUMMARY.md           # Project completion summary
├── 📄 VISUAL_GUIDE.md              # This file
├── 🔒 .gitignore                   # Git ignore rules
│
├── 🚀 start_backend.sh             # Backend startup script
├── 🚀 start_frontend.sh            # Frontend startup script
├── 🧪 test_system.py               # System validation script
│
├── 📁 backend/                     # Python Backend
│   ├── 📄 requirements.txt         # Python dependencies
│   │
│   ├── 📁 app/                     # Application layer
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI application (CORS, routes)
│   │   ├── api.py                  # REST API endpoints (8 endpoints)
│   │   ├── trainer.py              # Federated learning orchestrator
│   │   ├── aggregator.py           # Model aggregation strategies
│   │   ├── privacy.py              # Differential Privacy (DP-SGD)
│   │   └── utils.py                # Helper functions
│   │
│   ├── 📁 models/                  # ML Models
│   │   ├── __init__.py
│   │   ├── fraud_model.py          # Neural network architecture
│   │   └── secure_aggregation.py  # Secure aggregation protocol
│   │
│   ├── 📁 data/                    # Data management
│   │   ├── __init__.py
│   │   ├── synthetic_generator.py # Synthetic data generation
│   │   └── load_data.py            # Federated data partitioning
│   │
│   └── 📁 results/                 # Training results (auto-generated)
│       └── performance.json        # Metrics and results
│
└── 📁 frontend/                    # React Frontend
    ├── 📄 package.json             # Node dependencies
    ├── 📄 vite.config.js           # Vite configuration
    ├── 📄 index.html               # HTML entry point
    │
    └── 📁 src/
        ├── index.jsx               # React entry point
        ├── App.jsx                 # Main app component
        │
        ├── 📁 api/
        │   └── api.js              # Backend API client
        │
        └── 📁 components/          # React components
            ├── Dashboard.jsx              # Main dashboard (metrics overview)
            ├── TrainingControl.jsx        # Training configuration panel
            ├── InstitutionSimulator.jsx   # Federated clients visualization
            ├── PerformanceCharts.jsx      # Training progress charts
            ├── PrivacyVisualizer.jsx      # Privacy mechanisms (D3.js)
            └── AttackSimulation.jsx       # Privacy attack testing
```

## 🔄 System Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERACTION                         │
│                    Browser: localhost:5173                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      REACT FRONTEND                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Dashboard   │  │  Training    │  │  Privacy     │          │
│  │  Component   │  │  Control     │  │  Visualizer  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Performance  │  │ Institution  │  │   Attack     │          │
│  │   Charts     │  │  Simulator   │  │ Simulation   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP REST API
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FASTAPI BACKEND                             │
│                   localhost:8000/api                             │
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    API ENDPOINTS                          │  │
│  │  POST /train      │  GET /metrics    │  POST /predict    │  │
│  │  GET /status      │  GET /history    │  GET /clients     │  │
│  │  GET /attack-test │  DELETE /reset                       │  │
│  └───────────────────────────────────────────────────────────┘  │
│                             │                                     │
│                             ▼                                     │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              FEDERATED LEARNING TRAINER                   │  │
│  │  • Orchestrates training rounds                           │  │
│  │  • Manages client coordination                            │  │
│  │  • Applies privacy mechanisms                             │  │
│  └───────────────────────────────────────────────────────────┘  │
│                             │                                     │
│         ┌───────────────────┼───────────────────┐                │
│         ▼                   ▼                   ▼                │
│  ┌──────────┐        ┌──────────┐        ┌──────────┐           │
│  │  Bank 1  │        │  Bank 2  │        │  Bank 3  │           │
│  │  Client  │        │  Client  │        │  Client  │           │
│  │  Model   │        │  Model   │        │  Model   │           │
│  └────┬─────┘        └────┬─────┘        └────┬─────┘           │
│       │                   │                   │                  │
│       └───────────────────┴───────────────────┘                  │
│                           │                                       │
│                           ▼                                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │           DIFFERENTIAL PRIVACY (DP-SGD)                   │  │
│  │  • Gradient clipping (L2 norm ≤ 1.0)                     │  │
│  │  • Gaussian noise addition (σ = 1.1)                     │  │
│  │  • Privacy budget tracking (ε, δ)                        │  │
│  └───────────────────────────────────────────────────────────┘  │
│                           │                                       │
│                           ▼                                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              SECURE AGGREGATION                           │  │
│  │  • Additive masking protocol                             │  │
│  │  • Encrypted model updates                               │  │
│  │  • FedAvg weighted averaging                             │  │
│  └───────────────────────────────────────────────────────────┘  │
│                           │                                       │
│                           ▼                                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              GLOBAL MODEL UPDATE                          │  │
│  │  • Aggregated weights                                     │  │
│  │  • Broadcast to all clients                              │  │
│  │  • Next training round                                    │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## 🎨 Frontend Component Hierarchy

```
App.jsx (Main Router)
│
├── AppBar (Top Navigation)
│   └── "Federated Fraud Detection System"
│
├── Drawer (Sidebar Navigation)
│   ├── Dashboard
│   ├── Training Control
│   ├── Institutions
│   ├── Performance
│   ├── Privacy
│   └── Attack Simulation
│
└── Routes (Main Content Area)
    │
    ├── / → Dashboard.jsx
    │   ├── MetricCard (x4)
    │   │   ├── Federated AUC
    │   │   ├── F1 Score
    │   │   ├── Privacy Budget
    │   │   └── Communication Cost
    │   ├── ComparisonTable
    │   └── PrivacyMetrics
    │
    ├── /training → TrainingControl.jsx
    │   ├── Configuration Form
    │   │   ├── n_clients (slider)
    │   │   ├── n_rounds (slider)
    │   │   ├── local_epochs (slider)
    │   │   ├── batch_size (slider)
    │   │   ├── use_dp (switch)
    │   │   └── use_secure_agg (switch)
    │   ├── Start Training Button
    │   └── Configuration Summary
    │
    ├── /institutions → InstitutionSimulator.jsx
    │   ├── Training Status Bar
    │   ├── ClientCard (x5)
    │   │   ├── Bank Icon
    │   │   ├── Sample Count
    │   │   ├── Fraud Rate
    │   │   └── Progress Bar
    │   └── Network Summary
    │
    ├── /performance → PerformanceCharts.jsx
    │   ├── Metric Selector (Toggle)
    │   ├── TrainingProgressChart (Plotly)
    │   ├── ComparisonBarChart (Plotly)
    │   └── ImprovementChart (Plotly)
    │
    ├── /privacy → PrivacyVisualizer.jsx
    │   ├── PrivacyCard (x3)
    │   │   ├── Differential Privacy
    │   │   ├── Secure Aggregation
    │   │   └── Privacy Attacks
    │   ├── SecureAggregationFlow (D3.js SVG)
    │   └── DP Explanation
    │
    └── /attacks → AttackSimulation.jsx
        ├── Attack Description
        ├── Run Attack Button
        ├── Overall Defense Rate
        └── AttackResultCard (x2)
            ├── Membership Inference
            └── Model Inversion
```

## 🔌 API Endpoint Map

```
Backend API: http://localhost:8000/api

┌─────────────────────────────────────────────────────────┐
│                    TRAINING ENDPOINTS                    │
├─────────────────────────────────────────────────────────┤
│ POST   /train         Start federated training          │
│ GET    /status        Get current training status       │
│ GET    /history       Get training history              │
│ DELETE /reset         Reset training state              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                   EVALUATION ENDPOINTS                   │
├─────────────────────────────────────────────────────────┤
│ GET    /metrics       Get performance metrics           │
│ GET    /clients       Get client information            │
│ GET    /attack-test   Run privacy attack simulation     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                  PREDICTION ENDPOINTS                    │
├─────────────────────────────────────────────────────────┤
│ POST   /predict       Predict fraud for transaction     │
└─────────────────────────────────────────────────────────┘
```

## 📊 Data Flow

```
1. DATA GENERATION
   synthetic_generator.py
   ↓
   100,000 transactions
   (98% normal, 2% fraud)
   ↓
   load_data.py
   ↓
   Partition into 5 clients

2. FEDERATED TRAINING
   Client 1 (20K samples) ─┐
   Client 2 (20K samples) ─┤
   Client 3 (20K samples) ─┼→ Local Training
   Client 4 (20K samples) ─┤   (5 epochs each)
   Client 5 (20K samples) ─┘
   ↓
   Model Updates (weights)
   ↓
   Differential Privacy
   (Add noise, clip gradients)
   ↓
   Secure Aggregation
   (Encrypt, aggregate)
   ↓
   Global Model Update
   ↓
   Broadcast to Clients
   ↓
   Repeat for 10 rounds

3. EVALUATION
   Global Test Set (20K samples)
   ↓
   Evaluate Metrics
   (AUC, F1, Accuracy, etc.)
   ↓
   Privacy Attack Testing
   ↓
   Save Results
   ↓
   Display in Dashboard
```

## 🎯 Training Workflow

```
USER ACTION                 BACKEND PROCESS              RESULT
─────────────────────────────────────────────────────────────────
1. Click "Start Training"
   ↓
   POST /api/train
                            ↓
                            Initialize Trainer
                            ↓
                            Generate/Load Data
                            ↓
                            Partition into 5 clients
                                                         ↓
                                                         Status: "training"

2. Monitor Progress
   ↓
   GET /api/status (every 5s)
                            ↓
                            Round 1/10
                            ├─ Train Client 1
                            ├─ Train Client 2
                            ├─ Train Client 3
                            ├─ Train Client 4
                            └─ Train Client 5
                            ↓
                            Apply DP Noise
                            ↓
                            Secure Aggregation
                            ↓
                            Update Global Model
                            ↓
                            Evaluate
                                                         ↓
                                                         Progress: 10%

   [Repeat for rounds 2-10]
                                                         ↓
                                                         Progress: 100%

3. View Results
   ↓
   GET /api/metrics
                            ↓
                            Load results.json
                            ↓
                            Format metrics
                                                         ↓
                                                         Display Dashboard
```

## 🔐 Privacy Mechanism Flow

```
CLIENT MODEL UPDATE
↓
┌─────────────────────────────────────┐
│    DIFFERENTIAL PRIVACY (DP-SGD)    │
│                                     │
│  1. Compute Gradients               │
│     ∇L = ∂Loss/∂θ                  │
│                                     │
│  2. Clip Gradients                  │
│     ∇L' = ∇L / max(1, ||∇L||/C)   │
│     where C = 1.0                   │
│                                     │
│  3. Add Gaussian Noise              │
│     ∇L'' = ∇L' + N(0, σ²C²)       │
│     where σ = 1.1                   │
│                                     │
│  4. Update Weights                  │
│     θ' = θ - η∇L''                 │
│                                     │
└─────────────────────────────────────┘
↓
NOISY MODEL UPDATE
↓
┌─────────────────────────────────────┐
│      SECURE AGGREGATION             │
│                                     │
│  1. Add Random Mask                 │
│     θ_masked = θ' + mask_i          │
│                                     │
│  2. Send to Server                  │
│     [θ_masked_1, ..., θ_masked_n]  │
│                                     │
│  3. Server Aggregates               │
│     θ_agg = Σ(θ_masked_i) / n      │
│                                     │
│  4. Masks Cancel Out                │
│     Σ(mask_i) ≈ 0                  │
│                                     │
│  5. Clean Aggregated Model          │
│     θ_global = θ_agg                │
│                                     │
└─────────────────────────────────────┘
↓
GLOBAL MODEL UPDATE
```

## 📈 Performance Metrics Visualization

```
DASHBOARD VIEW
┌────────────────────────────────────────────────────────┐
│  Federated AUC    │  F1 Score    │  Privacy ε  │  Cost │
│      0.92         │    0.85      │    2.3      │ 58 MB │
│    (+9.5%)        │  (+18.1%)    │  (Target≤3) │       │
└────────────────────────────────────────────────────────┘

PERFORMANCE CHARTS
┌────────────────────────────────────────────────────────┐
│  Training Progress (Plotly Line Chart)                 │
│  1.0 ┤                                          ●       │
│      │                                    ●             │
│  0.8 ┤                              ●                   │
│      │                        ●                         │
│  0.6 ┤                  ●                               │
│      │            ●                                     │
│  0.4 ┤      ●                                           │
│      │●                                                 │
│  0.2 ┤                                                  │
│      └─────────────────────────────────────────────    │
│       1   2   3   4   5   6   7   8   9   10          │
│                    Training Round                       │
└────────────────────────────────────────────────────────┘

COMPARISON BAR CHART
┌────────────────────────────────────────────────────────┐
│  Federated vs Local Model                              │
│                                                         │
│  Accuracy  ████████████████░░░░  0.93 (Fed)           │
│            ████████████░░░░░░░░  0.88 (Local)         │
│                                                         │
│  AUC       ████████████████████  0.92 (Fed)           │
│            ██████████████░░░░░░  0.84 (Local)         │
│                                                         │
│  F1 Score  ███████████████░░░░░  0.85 (Fed)           │
│            ████████████░░░░░░░░  0.72 (Local)         │
└────────────────────────────────────────────────────────┘
```

## 🛡️ Privacy Visualization (D3.js)

```
SECURE AGGREGATION FLOW
┌──────────┐
│  Bank 1  │──┐
│  🔒      │  │
└──────────┘  │
              │
┌──────────┐  │     ┌──────────────┐     ┌──────────┐
│  Bank 2  │──┼────→│   Secure     │────→│  Global  │
│  🔒      │  │     │ Aggregation  │     │  Model   │
└──────────┘  │     │   Server     │     │    🌐    │
              │     └──────────────┘     └──────────┘
┌──────────┐  │
│  Bank 3  │──┘
│  🔒      │
└──────────┘

Legend:
🔒 = Encrypted updates
─→ = Secure channel
🌐 = Global model
```

## 🎓 Key Concepts Illustrated

### Federated Learning
```
Traditional ML:        Federated Learning:
┌─────────┐           ┌─────────┐
│ Central │           │ Server  │
│  Data   │           │ (Model) │
│ Storage │           └────┬────┘
└────┬────┘                │
     │                ┌────┴────┐
     ↓                ↓         ↓
┌─────────┐      ┌────────┐ ┌────────┐
│  Model  │      │ Bank 1 │ │ Bank 2 │
│Training │      │ (Data) │ │ (Data) │
└─────────┘      └────────┘ └────────┘

❌ Privacy Risk    ✅ Privacy Preserved
❌ Single Point    ✅ Distributed
❌ Data Movement    ✅ Model Movement
```

### Differential Privacy
```
Without DP:              With DP:
Model Output             Model Output + Noise
     │                        │
     ↓                        ↓
Can infer if           Cannot determine if
individual was         individual was in
in training set        training set
     │                        │
     ↓                        ↓
❌ Privacy Leak         ✅ Privacy Protected
```

## 🚀 Quick Command Reference

```bash
# Setup
cd federated-fraud-detection
./start_backend.sh      # Terminal 1
./start_frontend.sh     # Terminal 2

# Test
python3 test_system.py

# Access
http://localhost:5173   # Frontend
http://localhost:8000   # Backend
http://localhost:8000/docs  # API Docs

# Stop
Ctrl+C in both terminals
```

---

**Visual Guide Complete! 🎨**

This guide provides a visual representation of the entire system architecture, data flow, and component relationships.
