import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Easy
print("ALL EMPLOYEES:")
cursor.execute("SELECT * FROM employees;")
print(cursor.fetchall())

# Intermediate
print("\nIT employees with salary > 60000:")
cursor.execute("""
SELECT * FROM employees
WHERE department = 'IT'
AND salary > 60000;
""")
print(cursor.fetchall())

# Hard
print("\nTop 5 highest paid employees:")
cursor.execute("""
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 5;
""")
print(cursor.fetchall())

conn.close()
