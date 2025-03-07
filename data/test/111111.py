import matplotlib.pyplot as plt

# Data
models = ['Proposed', '[13]', '[14]', '[17]', '[24]', '[37]']
compression_ratios = [70, 52.67, 50, 36, 32.9,  46]

# Plot
plt.bar(models, compression_ratios, color=['red', 'blue', 'blue', 'blue', 'blue','blue'])
plt.xlabel("Models")
plt.ylabel("Compression Ratio (%)")
plt.ylim(0, 80)
plt.show()
