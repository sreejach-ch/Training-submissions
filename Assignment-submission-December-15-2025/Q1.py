import json

# Sample JSON data
json_data = '''
{
  "id": 101,
  "name": "Sreeja",
  "role": "Data Engineer",
  "skills": ["Python", "SQL", "Azure"]
}
'''

# Load JSON
data = json.loads(json_data)

# Print keys
print("JSON Keys:")
for key in data.keys():
    print(key)
