import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

# Display summary
print(df.head())         # First 5 rows
print(df.info())         # Column info
print(df.describe())     # Statistical summary
