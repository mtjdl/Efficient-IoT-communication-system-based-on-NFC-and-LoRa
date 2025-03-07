# 开发人员：ct
# 开发时间：2024/12/10 11:12
# 内容：
# Load the optimized and unoptimized dataframes for comparison
import colorsys

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Define simulation parameters
iterations = 50
x = np.arange(1, iterations + 1)

# Simulate response time (Adaptability) for optimized model
response_time_optimized = np.random.uniform(4, 6, iterations)  # Optimized response time (4-6 seconds)
response_time_baseline = np.random.uniform(15, 20, iterations)  # Baseline response time (15-20 seconds)

# Plot Response Time Comparison (Adaptability)
plt.figure(figsize=(10, 6))
plt.plot(x, response_time_optimized, label="Optimized Model", marker='o', linestyle='-', color='blue')
plt.plot(x, response_time_baseline, label="Baseline Model", marker='x', linestyle='--', color='red')
plt.title("Adaptability Comparison (Response Time)")
plt.xlabel("Iteration")
plt.ylabel("Response Time (seconds)")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
