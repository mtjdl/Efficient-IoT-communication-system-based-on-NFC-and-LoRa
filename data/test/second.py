# 开发人员：ct
# 开发时间：2024/12/10 11:12
# 内容：
# Load the optimized and unoptimized dataframes for comparison
import colorsys

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


iterations = 50
x = np.arange(1, iterations + 1)

# Simulate data compression ratios
compression_optimized = 70 + np.random.uniform(-2, 2, size=iterations)  # Optimized Model
compression_baseline = 50 + np.random.uniform(-2, 2, size=iterations)  # Baseline Model

# Simulate transmission latency
latency_optimized = 2.5 + np.random.uniform(-0.1, 0.1, size=iterations)  # Optimized Model
latency_baseline = 3.5 + np.random.uniform(-0.1, 0.1, size=iterations)  # Baseline Model

# Plot Data Compression Ratio
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(x, compression_optimized, label="Optimized Model", marker='o', linestyle='-',color='blue')
plt.plot(x, compression_baseline, label="Baseline Model", marker='x', linestyle='--',color='red')
plt.title("Data Compression Ratio")
plt.xlabel("Iteration")
plt.ylabel("Compression Ratio (%)")
plt.legend()
plt.grid()

# Plot Transmission Latency
plt.subplot(1, 2, 2)
plt.plot(x, latency_optimized, label="Optimized Model", marker='o', linestyle='-',color='blue')
plt.plot(x, latency_baseline, label="Baseline Model", marker='x', linestyle='--',color='red')
plt.title("Transmission Latency Comparison")
plt.xlabel("Iteration")
plt.ylabel("Latency (seconds)")
plt.legend()
plt.grid()

# Add labels below each subplot
plt.figtext(0.25, 0.01, "(a)", ha="center", fontsize=12, fontweight="bold")  # Label below the first subplot
plt.figtext(0.75, 0.01, "(b)", ha="center", fontsize=12, fontweight="bold")  # Label below the second subplot
# Adjust layout and show the plot
plt.tight_layout(rect=[0, 0.05, 1, 1])  # Adjust layout to make space for labels

plt.tight_layout()
plt.show()

