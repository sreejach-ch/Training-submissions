import csv

with open("Sample.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
