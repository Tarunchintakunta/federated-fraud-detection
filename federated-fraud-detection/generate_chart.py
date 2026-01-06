import matplotlib.pyplot as plt
import numpy as np

# Data
metrics = ['Precision', 'F1 Score', 'Recall', 'Accuracy']
benchmark_2025 = [0.887, 0.879, 0.889, 0.999]  # From paper
our_model = [0.972, 0.921, 0.875, 0.997]       # Our results

x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, benchmark_2025, width, label='Benchmark (2025)', color='#e0e0e0', edgecolor='black')
rects2 = ax.bar(x + width/2, our_model, width, label='Our Refactored Model', color='#4CAF50', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Score')
ax.set_title('Performance Comparison: Federated Fraud Detection')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.set_ylim(0, 1.1)
ax.legend(loc='lower right')

ax.bar_label(rects1, padding=3, fmt='%.3f')
ax.bar_label(rects2, padding=3, fmt='%.3f', fontweight='bold')

fig.tight_layout()

plt.savefig('project_assets/performance_comparison.png', dpi=300)
print("Chart saved to project_assets/performance_comparison.png")
