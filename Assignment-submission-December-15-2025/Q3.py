import pandas as pd
import logging
from datetime import datetime
import os

# Setup logging
logging.basicConfig(
    filename="etl_job.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract():
    logging.info("Extraction started")
    data = {
        "id": [1, 2, 3],
        "sales": [1000, 1500, 2000]
    }
    return pd.DataFrame(data)

def transform(df):
    logging.info("Transformation started")
    df["sales_with_tax"] = df["sales"] * 1.08
    return df

def load(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sales_data_{timestamp}.csv"
    df.to_csv(filename, index=False)
    logging.info(f"Data loaded to {filename}")

def etl_pipeline():
    logging.info("ETL job started")
    df = extract()
    df = transform(df)
    load(df)
    logging.info("ETL job completed successfully")

if __name__ == "__main__":
    etl_pipeline()
