# 开发人员：ct
# 开发时间：2024/12/10 11:12
# 内容：
# Load the optimized and unoptimized dataframes for comparison
import colorsys

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


import pandas as pd
import matplotlib.pyplot as plt
import ace_tools as tools;
# Define data for optimization comparison
metrics = ["Data Transmission Efficiency (%)", "Energy Consumption Reduction (%)",
           "Communication Reliability (%)", "Adaptability Response Time (s)"]

# Data values for proposed and literature
proposed_values = [70, 30, 98, 5]  # Optimized values
literature_values = [50, 20, 90, 10]  # Literature averages (unoptimized)

# Document sources for each metric
documents = ["[16:3], [8:5]", "[10:8], [9:7]", "[16:4], [13:6]", "[17:8], [18:9]"]

# Create a DataFrame for tabular representation
comparison_df = pd.DataFrame({
    "Metric": metrics,
    "Proposed Model": proposed_values,
    "Literature Avg": literature_values,
    "Documents": documents
})

# Plotting the comparison
plt.figure(figsize=(10, 6))

# Line plot for comparison
for i, (proposed, literature) in enumerate(zip(proposed_values, literature_values)):
    plt.plot(["Literature Avg", "Proposed Model"], [literature, proposed], marker='o', label=metrics[i])

# Adding labels, legend, and title
plt.title("Optimization Comparison: Proposed Model vs Literature")
plt.ylabel("Performance Metric Values")
plt.xlabel("Comparison Source")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()

# Display table and plot

#tools.display_dataframe_to_user(name="Optimization Comparison Table", dataframe=comparison_df)

plt.show()
