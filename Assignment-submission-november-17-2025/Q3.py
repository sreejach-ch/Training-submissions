import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

# Merge on customer_id
merged = pd.merge(orders, customers, on="customer_id", how="inner")

# Create a pivot table
pivot = merged.pivot_table(
    index="region",
    columns="product",
    values="sales",
    aggfunc="sum"
)

print(pivot)
