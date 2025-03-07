# 开发人员：ct
# 开发时间：2024/12/10 11:12
# 内容：
# Load the optimized and unoptimized dataframes for comparison
import colorsys

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


np.random.seed(42)
num_samples = 100
simulation_data = {
    "Scenario": ["Indoor Short (<10m)"] * num_samples + ["Outdoor Long (>1km)"] * num_samples,
    "Data Transmission Efficiency (%)": np.concatenate([
        np.random.uniform(72, 80, num_samples),  # Indoor Short
        np.random.uniform(68, 75, num_samples)   # Outdoor Long
    ]),
    "Energy Consumption (mW)": np.concatenate([
        np.random.uniform(65, 75, num_samples),  # Indoor Short
        np.random.uniform(85, 95, num_samples)   # Outdoor Long
    ]),
    "Communication Reliability (%)": np.concatenate([
        np.random.uniform(97, 99, num_samples),  # Indoor Short
        np.random.uniform(96, 98, num_samples)   # Outdoor Long
    ]),
    "Adaptability (s)": np.concatenate([
        np.random.uniform(4, 6, num_samples),    # Indoor Short
        np.random.uniform(9, 11, num_samples)    # Outdoor Long
    ])
}
unoptimized_simulation_data = {
    "Scenario": ["Indoor Short (<10m)"] * num_samples + ["Outdoor Long (>1km)"] * num_samples,
    "Data Transmission Efficiency (%)": np.concatenate([
        np.random.uniform(50, 60, num_samples),  # Indoor Short
        np.random.uniform(40, 50, num_samples)   # Outdoor Long
    ]),
    "Energy Consumption (mW)": np.concatenate([
        np.random.uniform(90, 100, num_samples),  # Indoor Short
        np.random.uniform(110, 120, num_samples)  # Outdoor Long
    ]),
    "Communication Reliability (%)": np.concatenate([
        np.random.uniform(90, 95, num_samples),   # Indoor Short
        np.random.uniform(85, 90, num_samples)    # Outdoor Long
    ]),
    "Adaptability (s)": np.concatenate([
        np.random.uniform(15, 20, num_samples),   # Indoor Short
        np.random.uniform(25, 30, num_samples)   # Outdoor Long
    ])
}
simulation_df = pd.DataFrame(simulation_data)
unoptimized_simulation_df = pd.DataFrame(unoptimized_simulation_data)



optimized_data = simulation_df.groupby("Scenario").agg({
    "Data Transmission Efficiency (%)": ['mean'],
    "Energy Consumption (mW)": ['mean'],
    "Communication Reliability (%)": ['mean'],
    "Adaptability (s)": ['mean']
})

unoptimized_data = unoptimized_simulation_df.groupby("Scenario").agg({
    "Data Transmission Efficiency (%)": ['mean'],
    "Energy Consumption (mW)": ['mean'],
    "Communication Reliability (%)": ['mean'],
    "Adaptability (s)": ['mean']
})

# Extract mean values for comparison
metrics = ["Data Transmission Efficiency (%)", "Energy Consumption (mW)", "Communication Reliability (%)",
           "Adaptability (s)"]
scenarios = ["Indoor Short (<10m)", "Outdoor Long (>1km)"]
optimized_means = optimized_data.xs("mean", level=1, axis=1).loc[scenarios]
unoptimized_means = unoptimized_data.xs("mean", level=1, axis=1).loc[scenarios]

# Create a bar chart for each metric
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, metric in enumerate(metrics):
    ax = axes[i]
    x = np.arange(len(scenarios))
    bar_width = 0.35

    # Plot bars for unoptimized and optimized data
    ax.bar(x - bar_width / 2, unoptimized_means[metric], bar_width, label="Unoptimized",color="blue")
    ax.bar(x + bar_width / 2, optimized_means[metric], bar_width, label="Optimized",color="red")

    # Add labels and title
    ax.set_title(f"{metric} Comparison")
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, rotation=20)
    ax.set_ylabel(metric)
    ax.legend()

plt.tight_layout()
plt.show()
