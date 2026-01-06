import sys
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
sys.path.append('backend')
from models.fraud_model import FraudDetectionModel
from data.load_data import load_federated_data

# Load Data
print("Loading data...")
client_data, test_data = load_federated_data(n_clients=5)
X_test, y_test = test_data

# Load Model
print("Loading model...")
model = FraudDetectionModel(input_dim=29)
model.load("backend/models/saved/fraud_detection_model.h5")

# Predict
print("Predicting...")
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Normal', 'Fraud'])

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
disp.plot(cmap='Blues', ax=ax, values_format='d')
plt.title('Confusion Matrix: Federated Fraud Detection')
plt.tight_layout()
plt.savefig('project_assets/confusion_matrix.png', dpi=300)
print("Saved to project_assets/confusion_matrix.png")
