"""
Differential Privacy implementation for federated learning
"""
import numpy as np

class DifferentialPrivacyManager:
    """
    Manages differential privacy for federated learning
    Implements Weight Perturbation with Gaussian noise
    """
    
    def __init__(self, l2_norm_clip=1.0, noise_multiplier=1.1, num_microbatches=32, learning_rate=0.001):
        self.l2_norm_clip = l2_norm_clip
        self.noise_multiplier = noise_multiplier
        self.num_microbatches = num_microbatches
        self.learning_rate = learning_rate
        self.epsilon = None
        self.delta = None
        
    def compute_privacy_budget(self, n_samples, batch_size, epochs):
        """
        Compute privacy budget (epsilon) using Moments Accountant approximation
        """
        steps = epochs * (n_samples // batch_size)
        delta = 1.0 / n_samples
        
        # Simplified approximation for Moments Accountant
        q = batch_size / n_samples  # Sampling ratio
        sigma = self.noise_multiplier
        
        # Approximation: ε ≈ q * steps / sigma
        epsilon = (q * steps) / (sigma * np.sqrt(2 * np.log(1.25 / delta)))
        
        self.epsilon = epsilon
        self.delta = delta
        
        return epsilon, delta
    
    def add_noise_to_weights(self, weights, scale=None):
        """Add calibrated noise to model weights"""
        if scale is None:
            scale = self.l2_norm_clip * self.noise_multiplier
        
        noisy_weights = []
        for w in weights:
            # Generate noise with same shape as weight matrix/vector
            noise = np.random.normal(0, scale, w.shape)
            noisy_w = w + noise
            noisy_weights.append(noisy_w)
        
        return noisy_weights
    
    def get_privacy_metrics(self):
        """Get current privacy metrics"""
        return {
            'epsilon': self.epsilon,
            'delta': self.delta,
            'l2_norm_clip': self.l2_norm_clip,
            'noise_multiplier': self.noise_multiplier
        }

class PrivacyAttackSimulator:
    """
    Simulate privacy attacks to test robustness
    """
    
    def __init__(self, model):
        self.model = model
        
    def membership_inference_attack(self, X_train, X_test, y_train, y_test, n_samples=100):
        """
        Simulate membership inference attack
        """
        # Select random samples
        n_train = min(n_samples, len(X_train))
        n_test = min(n_samples, len(X_test))
        
        train_indices = np.random.choice(len(X_train), n_train, replace=False)
        test_indices = np.random.choice(len(X_test), n_test, replace=False)
        
        # Get predictions (probabilities)
        # Sklearn predict_proba returns [prob_0, prob_1], we want prob_1
        try:
            train_preds = self.model.predict_proba(X_train[train_indices])[:, 1]
            test_preds = self.model.predict_proba(X_test[test_indices])[:, 1]
        except AttributeError:
             # Fallback if model doesn't support proba (shouldn't happen with MLP)
            train_preds = self.model.predict(X_train[train_indices])
            test_preds = self.model.predict(X_test[test_indices])
            
        # Calculate prediction confidence (dist from 0.5)
        train_confidence = np.abs(train_preds - 0.5).mean()
        test_confidence = np.abs(test_preds - 0.5).mean()
        
        # Attack assumes higher confidence = training member
        attack_accuracy = abs(train_confidence - test_confidence) / (train_confidence + test_confidence + 1e-10)
        
        # Convert to success rate
        attack_success_rate = min(attack_accuracy * 2, 1.0)
        
        return {
            'attack_success_rate': float(attack_success_rate),
            'defense_success_rate': float(1.0 - attack_success_rate),
            'train_confidence': float(train_confidence),
            'test_confidence': float(test_confidence)
        }
    
    def model_inversion_attack(self, X_sample):
        """
        Simulate model inversion attack
        """
        # Start with random input
        reconstructed = np.random.randn(*X_sample.shape)
        
        # Prediction
        try:
            original_pred = self.model.predict_proba(X_sample.reshape(1, -1))[:, 1]
            reconstructed_pred = self.model.predict_proba(reconstructed.reshape(1, -1))[:, 1]
        except:
            original_pred = self.model.predict(X_sample.reshape(1, -1))
            reconstructed_pred = self.model.predict(reconstructed.reshape(1, -1))
        
        # Calculate reconstruction error
        reconstruction_error = np.mean(np.abs(X_sample - reconstructed))
        prediction_diff = np.abs(original_pred - reconstructed_pred)
        
        defense_score = min(reconstruction_error / 10.0, 1.0)
        
        return {
            'reconstruction_error': float(reconstruction_error),
            'prediction_difference': float(prediction_diff[0]),
            'defense_score': float(defense_score)
        }
    
    def run_all_attacks(self, X_train, X_test, y_train, y_test):
        """Run all privacy attacks"""
        print("Running privacy attack simulations...")
        
        membership = self.membership_inference_attack(X_train, X_test, y_train, y_test)
        
        sample_idx = np.random.randint(0, len(X_test))
        inversion = self.model_inversion_attack(X_test[sample_idx])
        
        results = {
            'membership_inference': membership,
            'model_inversion': inversion,
            'overall_defense_rate': (membership['defense_success_rate'] + inversion['defense_score']) / 2
        }
        
        return results
