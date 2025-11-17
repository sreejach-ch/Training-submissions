import pandas as pd

df = pd.read_csv("sales_data.csv")

# Group by region
region_totals = df.groupby("region")["sales"].sum()

print(region_totals)
