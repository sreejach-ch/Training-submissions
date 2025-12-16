import plotly.express as px

products = ["A", "B", "C", "D"]
sales = [120, 90, 150, 80]

fig = px.bar(x=products, y=sales, labels={'x':'Products', 'y':'Sales'}, title="Interactive Sales Bar Chart")
fig.show()
