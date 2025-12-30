import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary INTEGER
);
""")

# Insert sample data
cursor.executemany("""
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
""", [
    ("Alice", "IT", 90000),
    ("Bob", "HR", 60000),
    ("Charlie", "IT", 75000),
    ("Diana", "Finance", 85000),
    ("Eve", "IT", 95000),
    ("Frank", "HR", 50000)
])

conn.commit()
conn.close()

print("Database setup complete!")
