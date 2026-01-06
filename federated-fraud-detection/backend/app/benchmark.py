"""
Benchmark comparison logic for Federated Fraud Detection
"""
import numpy as np

class BenchmarkComparator:
    """
    Compares model performance against 'Gold Standard' research papers.
    Reference: Dal Pozzolo et al. (Credit Card Fraud Detection)
    """
    
    # Gold Standard metrics from 2024 Research Paper
    # Reference: Federated Learning for Credit Card Fraud Detection using SMOTE and LSTM/CNN (2024)
    DAL_POZZOLO_BENCHMARK = {
        'accuracy': 0.9992,  # 99.92% (from similar 2024 studies)
        'recall': 0.889,     # 88.9%
        'precision': 0.887,  # 88.7%
        'f1_score': 0.879    # 87.9%
    }
    
    @staticmethod
    def get_benchmark():
        """Get the Gold Standard benchmark metrics"""
        return BenchmarkComparator.DAL_POZZOLO_BENCHMARK
    
    @staticmethod
    def compare(model_metrics):
        """
        Compare model metrics against the benchmark
        
        Args:
            model_metrics (dict): Dictionary containing model metrics (accuracy, recall, etc.)
            
        Returns:
            dict: Comparison results including differences and analysis
        """
        benchmark = BenchmarkComparator.DAL_POZZOLO_BENCHMARK
        comparison = {}
        
        for metric, standard_value in benchmark.items():
            model_value = model_metrics.get(metric, 0)
            
            # Calculate difference
            diff = model_value - standard_value
            
            # Determine status
            if metric == 'recall':
                # For fraud detection, higher recall is critical
                if diff >= 0:
                    status = "OUTPERFORMS"
                    analysis = "Superior fraud detection rate"
                elif diff > -0.05:
                    status = "COMPETITIVE"
                    analysis = "Comparable detection rate"
                else:
                    status = "UNDERPERFORMS"
                    analysis = "Misses more fraud cases"
            else:
                # For other metrics
                if diff >= 0:
                    status = "OUTPERFORMS"
                    analysis = "Better than standard"
                elif diff > -0.02:
                    status = "COMPETITIVE"
                    analysis = "Comparable performance"
                else:
                    status = "UNDERPERFORMS"
                    analysis = "Below standard"
            
            comparison[metric] = {
                'standard': standard_value,
                'model': model_value,
                'difference': round(diff, 4),
                'status': status,
                'analysis': analysis
            }
            
        return comparison
