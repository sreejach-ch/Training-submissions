# intermediate_csv_to_json.py
import csv
import json
from pathlib import Path

csv_file = Path("sample.csv")
json_file = Path("sample.json")

# Read CSV into list of dicts
with csv_file.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Save to JSON (pretty printed)
with json_file.open("w", encoding="utf-8") as jf:
    json.dump(data, jf, indent=2)

print(f"Saved {len(data)} records to {json_file}")
