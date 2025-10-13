# Easy: create a dictionary and print keys
employees = {
    "E001": {"name": "Alice", "role": "Data Engineer", "dept": "Analytics"},
    "E002": {"name": "Bob",   "role": "QA Analyst",    "dept": "Quality"},
    "E003": {"name": "Cara",  "role": "Product Lead",  "dept": "Product"},
}

# Print all keys (employee IDs)
for emp_id in employees.keys():
    print(emp_id)
