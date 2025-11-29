# Using Kaggle Credit Card Fraud Detection Dataset

This project now uses real-world data from Kaggle instead of synthetic data.

## Dataset Information

**Kaggle Dataset**: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

- **Size**: 284,807 transactions
- **Fraud Cases**: 492 (0.172% fraud rate)
- **Features**: 
  - `Time`: Seconds elapsed between each transaction and the first transaction
  - `Amount`: Transaction amount
  - `V1-V28`: PCA-transformed features (anonymized)
  - `Class`: Target variable (0 = normal, 1 = fraud)

## Download Methods

### Method 1: Using Kaggle API (Recommended)

1. **Install Kaggle package**:
   ```bash
   pip install kaggle
   ```

2. **Set up Kaggle API credentials**:
   - Go to https://www.kaggle.com/account
   - Scroll to "API" section
   - Click "Create New API Token"
   - This downloads `kaggle.json`
   - Place it in `~/.kaggle/` directory:
     ```bash
     mkdir -p ~/.kaggle
     mv ~/Downloads/kaggle.json ~/.kaggle/
     chmod 600 ~/.kaggle/kaggle.json
     ```

3. **Download the dataset**:
   ```bash
   cd backend/data
   python download_kaggle_dataset.py
   ```

   Or from the backend directory:
   ```bash
   python -m data.download_kaggle_dataset
   ```

### Method 2: Manual Download

1. Visit: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
2. Sign in to Kaggle (required)
3. Click "Download" button
4. Extract `creditcard.csv` from the zip file
5. Place it in `backend/data/creditcard.csv`

## Data Loading Priority

The system will automatically use datasets in this order:

1. **Specified filepath** (if provided in code)
2. **`creditcard.csv`** (official Kaggle dataset)
3. **`clean_dataset.csv`** (if it exists)
4. **Synthetic data** (fallback only)

## Verification

After downloading, verify the dataset:

```python
import pandas as pd
df = pd.read_csv('backend/data/creditcard.csv')
print(f"Rows: {len(df)}")
print(f"Fraud cases: {df['Class'].sum()}")
print(f"Columns: {list(df.columns)}")
```

Expected output:
- Rows: 284,807
- Fraud cases: 492
- Columns: ['Time', 'Amount', 'V1', 'V2', ..., 'V28', 'Class']

## Notes

- The dataset is highly imbalanced (0.172% fraud rate)
- The model uses class weighting to handle this imbalance
- All features are automatically scaled during preprocessing
- The model expects exactly 29 features (Time + Amount + V1-V28)

