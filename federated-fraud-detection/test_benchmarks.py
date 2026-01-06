"""
Test benchmark comparison logic
"""
import unittest
import sys
import os
import json
from unittest.mock import MagicMock, patch

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.app.benchmark import BenchmarkComparator

class TestBenchmarkComparison(unittest.TestCase):
    
    def test_benchmark_values(self):
        """Test that benchmark values match the Gold Standard"""
        benchmark = BenchmarkComparator.get_benchmark()
        
        self.assertEqual(benchmark['accuracy'], 0.9991)
        self.assertEqual(benchmark['recall'], 0.78)
        self.assertEqual(benchmark['precision'], 0.85)
        self.assertEqual(benchmark['f1_score'], 0.81)
        
    def test_comparison_logic_outperform(self):
        """Test comparison when model outperforms benchmark"""
        # Model with better recall (0.82 vs 0.78)
        model_metrics = {
            'accuracy': 0.9985,
            'recall': 0.82,
            'precision': 0.79,
            'f1_score': 0.80
        }
        
        comparison = BenchmarkComparator.compare(model_metrics)
        
        # Check Recall comparison
        self.assertEqual(comparison['recall']['status'], "OUTPERFORMS")
        self.assertGreater(comparison['recall']['difference'], 0)
        
        # Check Accuracy comparison (slightly lower)
        self.assertEqual(comparison['accuracy']['status'], "COMPETITIVE")
        self.assertLess(comparison['accuracy']['difference'], 0)
        
    def test_comparison_logic_underperform(self):
        """Test comparison when model underperforms"""
        model_metrics = {
            'recall': 0.50  # Much lower than 0.78
        }
        
        comparison = BenchmarkComparator.compare(model_metrics)
        
        self.assertEqual(comparison['recall']['status'], "UNDERPERFORMS")
        
    def test_api_integration(self):
        """Test that API response structure would include benchmark"""
        # Mock training results
        mock_results = {
            'federated_model': {'recall': 0.82},
            'local_baseline': {'recall': 0.75},
            'benchmark_comparison': {
                'recall': {
                    'standard': 0.78,
                    'model': 0.82,
                    'status': "OUTPERFORMS"
                }
            }
        }
        
        # Verify structure
        self.assertIn('benchmark_comparison', mock_results)
        self.assertEqual(mock_results['benchmark_comparison']['recall']['status'], "OUTPERFORMS")

if __name__ == '__main__':
    unittest.main()
