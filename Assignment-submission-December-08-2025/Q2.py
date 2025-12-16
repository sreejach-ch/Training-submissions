import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Sales": [120, 90, 150, 80],
    "Profit": [30, 20, 50, 15],
    "Discount": [5, 3, 2, 4]
}

df = pd.DataFrame(data)

plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
