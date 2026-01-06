import os
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve
import json

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from app.trainer import FederatedTrainer
from models.fraud_model import FraudDetectionModel

def set_style():
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.size': 12,
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'figure.titlesize': 18,
        'legend.fontsize': 12,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11
    })

def generate_confusion_matrix(y_true, y_pred_prob, threshold=0.5):
    y_pred = (y_pred_prob > threshold).astype(int)
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Legitimate', 'Fraud'],
                yticklabels=['Legitimate', 'Fraud'])
    plt.title('Confusion Matrix: Federated Model')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig('thesis_report/figures/fig10_confusion_matrix.png', dpi=300)
    print("Generated Confusion Matrix")

def generate_roc_curve(y_true, y_pred_prob):
    fpr, tpr, _ = roc_curve(y_true, y_pred_prob)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='#2196f3', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate (Recall)')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('thesis_report/figures/fig11_roc_curve.png', dpi=300)
    print("Generated ROC Curve")

def generate_benchmark_chart():
    # Data from report
    metrics = ['Recall', 'Precision', 'F1-Score']
    our_model = [0.83, 0.13, 0.23]
    industry_std = [0.78, 0.85, 0.81]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, our_model, width, label='Our Federated Model', color='#2196f3')
    plt.bar(x + width/2, industry_std, width, label='Industry Standard (Centralized)', color='#9e9e9e')
    
    plt.ylabel('Score')
    plt.title('Performance Comparison: Federated vs. Centralized')
    plt.xticks(x, metrics)
    plt.ylim(0, 1.1)
    
    # Add value labels
    for i, v in enumerate(our_model):
        plt.text(i - width/2, v + 0.02, f'{v:.2f}', ha='center', va='bottom', fontweight='bold')
        
    for i, v in enumerate(industry_std):
        plt.text(i + width/2, v + 0.02, f'{v:.2f}', ha='center', va='bottom')

    plt.legend()
    plt.tight_layout()
    plt.savefig('thesis_report/figures/fig9_benchmark_chart.png', dpi=300)
    print("Generated Benchmark Chart")

def main():
    os.makedirs('thesis_report/figures', exist_ok=True)
    set_style()
    
    print("Initializing Trainer...")
    # Initialize with same params as training
    trainer = FederatedTrainer(n_clients=5, n_rounds=10, local_epochs=5, batch_size=32, use_dp=True)
    
    print("Loading Data...")
    trainer.load_data()
    
    # Try to load trained model
    model_path = 'backend/models/saved/fraud_detection_model.h5'
    if os.path.exists(model_path):
        print("Loading trained model weights...")
        try:
            # We need to build the model first to load weights into it
            trainer.global_model.build_model()
            # Loading weights from h5 is tricky if it's full model vs weights. 
            # safe assumption: if save() used model.save(), then load_model() works.
            # But FederatedTrainer uses global_model.save() which calls model.save().
            # Let's try loading.
            import tensorflow as tf
            loaded_model = tf.keras.models.load_model(model_path)
            trainer.global_model.model = loaded_model
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}. Retraining...")
            trainer.train()
    else:
        print("Model not found. Retraining...")
        trainer.train()

    # Get predictions on test set
    print("Evaluating on Test Set...")
    X_test, y_test = trainer.test_data
    y_pred_prob = trainer.global_model.predict(X_test)
    
    # Generate Plots
    generate_confusion_matrix(y_test, y_pred_prob)
    generate_roc_curve(y_test, y_pred_prob)
    generate_benchmark_chart()
    
    print("All plots generated in thesis_report/figures/")

if __name__ == "__main__":
    main()
