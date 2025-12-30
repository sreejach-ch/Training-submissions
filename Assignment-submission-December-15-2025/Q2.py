import pandas as pd

# Sample data
data = {
    "employee_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [70000, 80000, 90000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Transformation: add 10% bonus column
df["bonus"] = df["salary"] * 0.10

# Save to CSV
df.to_csv("employees_transformed.csv", index=False)

print("CSV file created successfully.")
