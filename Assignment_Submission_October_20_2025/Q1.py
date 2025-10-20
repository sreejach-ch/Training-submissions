# easy_read_csv.py
import csv
from pathlib import Path

csv_file = Path("sample.csv")

# If you need a quick sample CSV, create it:
if not csv_file.exists():
    csv_file.write_text("id,name,age,city\n1,Alice,30,Seattle\n2,Bob,28,Boston\n3,Carol,35,Chicago\n", encoding="utf-8")

# Read and print rows
with csv_file.open(newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
