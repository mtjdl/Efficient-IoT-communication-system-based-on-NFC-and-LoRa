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

# Simulate packet loss rate data
packet_loss_optimized = 2 + np.random.uniform(-0.5, 0.5, size=iterations)  # Optimized Model
packet_loss_baseline = 5 + np.random.uniform(-0.5, 0.5, size=iterations)  # Baseline Model

# Simulate retransmission success rate data
retransmission_success_optimized = 98 + np.random.uniform(-0.5, 0.5, size=iterations)  # Optimized Model
retransmission_success_baseline = 90 + np.random.uniform(-0.5, 0.5, size=iterations)  # Baseline Model

# Plot Packet Loss Rate Comparison
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, packet_loss_optimized, label="Optimized Model", marker='o', linestyle='-',color='blue')
plt.plot(x, packet_loss_baseline, label="Baseline Model", marker='x', linestyle='--',color='red')
plt.title("Packet Loss Rate Comparison")
plt.xlabel("Iteration")
plt.ylabel("Packet Loss Rate (%)")
plt.legend()
plt.grid()

# Plot Retransmission Success Rate Comparison
plt.subplot(1, 2, 2)
plt.plot(x, retransmission_success_optimized, label="Optimized Model", marker='o', linestyle='-',color='blue')
plt.plot(x, retransmission_success_baseline, label="Baseline Model", marker='x', linestyle='--',color='red')
plt.title("Retransmission Success Rate Comparison")
plt.xlabel("Iteration")
plt.ylabel("Retransmission Success Rate (%)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()