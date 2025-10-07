import json
import psycopg2
from psycopg2 import sql
from typing import List, Dict, Any

DB_DETAILS = {
    "host": "localhost",
    "database": "SampleDB", 
    "user": "postgres",
    "password": "Sreeja@42", 
    "port": "5432"
}

JSON_FILE_PATH = './data.json' 
TARGET_TABLE = "inventory_data"


def extract_data(file_path: str) -> List[Dict[str, Any]]:   
    print(f"1. Extracting data from {file_path}...")
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print(f"   -> Successfully extracted {len(data)} records.")
        return data
    except FileNotFoundError:
        print(f"ERROR: JSON file not found at {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse JSON file. Check for formatting errors. Details: {e}")
        return []

def load_data_to_postgres(data: List[Dict[str, Any]], table_name: str, db_details: Dict[str, str]):
    if not data:
        print("2. No data to load. Exiting load process.")
        return

    print(f"2. Connecting to PostgreSQL and loading data into '{table_name}'...")
    conn = None
    try:
        conn = psycopg2.connect(**db_details)
        cursor = conn.cursor()
        columns = data[0].keys()
        column_names = sql.SQL(', ').join(map(sql.Identifier, columns))
        placeholders = sql.SQL(', ').join(sql.Placeholder() * len(columns))
        
        insert_query = sql.SQL("""
            INSERT INTO {} ({}) VALUES ({})
        """).format(
            sql.Identifier(table_name),
            column_names,
            placeholders
        )

        success_count = 0
        for record in data:
            values = tuple(record[col] for col in columns)
            cursor.execute(insert_query, values)
            success_count += 1
            
        conn.commit()
        
        print(f"   -> Successfully loaded {success_count} records into {table_name}.")

    except (Exception, psycopg2.Error) as error:
        print(f"ERROR during PostgreSQL operation: {error}")
        if conn:
            conn.rollback() 
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("3. PostgreSQL connection closed.")

def main():
    inventory_records = extract_data(JSON_FILE_PATH)
    load_data_to_postgres(inventory_records, TARGET_TABLE, DB_DETAILS)

if __name__ == "__main__":
    main()
