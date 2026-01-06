"""
Fraud detection model architecture using Scikit-Learn
"""
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib

class FraudDetectionModel:
    """Deep learning model for fraud detection using Scikit-Learn"""
    
    def __init__(self, input_dim=29, learning_rate=0.0001):
        self.input_dim = input_dim
        self.learning_rate = learning_rate
        self.model = None
        
    def build_model(self):
        """Build the fraud detection neural network"""
        # MLPClassifier with warm_start=True allows partial_fit (online learning)
        self.model = MLPClassifier(
            hidden_layer_sizes=(64, 32, 16),
            activation='relu',
            solver='adam',
            alpha=0.01,
            batch_size=32,
            learning_rate='constant',
            learning_rate_init=self.learning_rate,
            max_iter=1,  # We control epochs manually
            random_state=42,
            warm_start=False,
            verbose=False
        )
        
        # Initialize weights immediately with dummy data
        # This creates the coefs_ and intercepts_ attributes
        dummy_X = np.zeros((1, self.input_dim))
        dummy_y = np.array([0])
        self.model.partial_fit(dummy_X, dummy_y, classes=np.array([0, 1]))
        
        return self.model
    
    def get_model(self):
        """Get or create model"""
        if self.model is None:
            self.build_model()
        return self.model
    
    def train(self, X_train, y_train, X_val=None, y_val=None, epochs=10, batch_size=32, verbose=1):
        """Train the model"""
        if self.model is None:
            self.build_model()
        
        # Always assume binary classification [0, 1] for consistency across batches
        all_classes = np.array([0, 1])
        
        history = {'loss': [], 'accuracy': [], 'val_loss': [], 'val_accuracy': []}
        
        # Flatten structure for sklearn
        y_train = y_train.ravel()
        
        for epoch in range(epochs):
            # partial_fit runs one iteration (epoch) on the data
            self.model.partial_fit(X_train, y_train, classes=all_classes)
            
            # Record metrics (simplified)
            loss = self.model.loss_
            history['loss'].append(loss)
            
            if verbose > 0 and epoch % 5 == 0:
                print(f"Epoch {epoch+1}/{epochs} - loss: {loss:.4f}")
                
        return history
    
    def evaluate(self, X_test, y_test):
        """Evaluate model performance"""
        if self.model is None:
            raise ValueError("Model not trained yet")
        
        # Predictions
        y_pred = self.model.predict(X_test)
        y_prob = self.model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, zero_division=0)
        recall = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        
        try:
            auc = roc_auc_score(y_test, y_prob)
        except:
            auc = 0.5
            
        metrics = {
            'loss': self.model.loss_,
            'accuracy': accuracy,
            'auc': auc,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }
        
        return metrics
    
    def predict(self, X):
        """Make predictions"""
        if self.model is None:
            raise ValueError("Model not trained yet")
        # Return probabilities to match Keras predict output shape (N, 1)
        return self.model.predict_proba(X)[:, 1].reshape(-1, 1)
    
    def get_weights(self):
        """Get model weights (coefs and intercepts)"""
        if self.model is None:
            raise ValueError("Model not built yet")
        
        # Combine coefs and intercepts into a list suitable for transport/averaging
        # coefs_ is a list of weight matrices
        # intercepts_ is a list of bias vectors
        return self.model.coefs_ + self.model.intercepts_
    
    def set_weights(self, weights):
        """Set model weights"""
        if self.model is None:
            self.build_model()
            # Must initialize internal structures if setting weights before any training
            # Dummy fit to initialize shapes
            dummy_X = np.zeros((1, self.input_dim))
            dummy_y = np.array([0])
            self.model.partial_fit(dummy_X, dummy_y, classes=np.array([0, 1]))
            
        # weights list contains [coefs..., intercepts...]
        # MLPClassifier (64, 32, 16) has 3 layers:
        # coefs: [input->64, 64->32, 32->16, 16->1] (4 matrices)
        # intercepts: [64, 32, 16, 1] (4 vectors)
        # Total 8 items in weights list
        
        n_layers = len(self.model.coefs_)
        
        new_coefs = weights[:n_layers]
        new_intercepts = weights[n_layers:]
        
        self.model.coefs_ = new_coefs
        self.model.intercepts_ = new_intercepts
    
    def save(self, filepath):
        """Save model"""
        if self.model is None:
            raise ValueError("Model not built yet")
        joblib.dump(self.model, filepath)
    
    def load(self, filepath):
        """Load model"""
        self.model = joblib.load(filepath)
        return self.model

def create_model(input_dim=29):
    """Factory function to create a fraud detection model"""
    model_builder = FraudDetectionModel(input_dim=input_dim)
    return model_builder.build_model()

if __name__ == "__main__":
    # Test model creation
    model = FraudDetectionModel(input_dim=29)
    model.build_model()
    print("Model created.")

