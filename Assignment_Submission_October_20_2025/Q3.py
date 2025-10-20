# hard_logging_example.py
import logging
import time
from functools import wraps
from pathlib import Path
import csv, json

LOG_PATH = Path("script.log")

# Configure logging (file + console)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("job_logger")

def log_execution(func):
    """Decorator to log start, finish, duration, and exceptions for functions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_ts = time.time()
        logger.info(f"START {func.__name__}")
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_ts
            logger.info(f"END {func.__name__} (duration: {duration:.3f}s)")
            return result
        except Exception as exc:
            duration = time.time() - start_ts
            logger.exception(f"ERROR {func.__name__} after {duration:.3f}s: {exc}")
            raise  # re-raise so caller knows it failed
    return wrapper

# Example functions using the decorator:

@log_execution
def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    return rows

@log_execution
def csv_to_json(csv_path, json_path):
    rows = read_csv(csv_path)  # decorated read
    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(rows, jf, indent=2)
    return len(rows)

@log_execution
def task_that_fails():
    # Example to demonstrate exception logging
    x = 1 / 0
    return x

if __name__ == "__main__":
    csv_path = Path("sample.csv")
    json_path = Path("sample.json")
    # Ensure sample CSV exists (same quick sample as above)
    if not csv_path.exists():
        csv_path.write_text("id,name,age,city\n1,Alice,30,Seattle\n2,Bob,28,Boston\n", encoding="utf-8")
    # Run tasks
    count = csv_to_json(csv_path, json_path)
    print(f"Wrote {count} rows to {json_path}")
    # Demonstrate logging of an exception (this will raise)
    try:
        task_that_fails()
    except ZeroDivisionError:
        print("Demonstrated error logged (ZeroDivisionError).")
