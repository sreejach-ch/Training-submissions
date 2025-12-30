import numpy as np

# Generate 1000 random values (normal distribution)
data = np.random.randn(1000)

# Compute mean and standard deviation
mean_value = np.mean(data)
std_value = np.std(data)

print(f"Mean: {mean_value:.4f}")
print(f"Standard Deviation: {std_value:.4f}")
