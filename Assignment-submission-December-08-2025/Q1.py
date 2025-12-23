import matplotlib.pyplot as plt

# Sample sales data
products = ["A", "B", "C", "D"]
sales = [120, 90, 150, 80]

plt.bar(products, sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales by Product")
plt.show()
