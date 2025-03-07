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

# Simulate power consumption data
power_consumption_sensor_optimized = 70 + np.random.uniform(-3, 3, size=iterations)  # Optimized Model
power_consumption_sensor_baseline = 100 + np.random.uniform(-3, 3, size=iterations)  # Baseline Model

# Plot Power Consumption Comparison for Sensor Node
plt.figure(figsize=(10, 6))
plt.plot(x, power_consumption_sensor_optimized, label="Optimized Model", marker='o', linestyle='-',color='blue')
plt.plot(x, power_consumption_sensor_baseline, label="Baseline Model", marker='x', linestyle='--',color='red')
plt.title("Sensor Node Power Consumption Comparison")
plt.xlabel("Iteration")
plt.ylabel("Power Consumption (mW)")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
