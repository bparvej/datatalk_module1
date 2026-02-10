import os
import pandas as pd
from sqlalchemy import create_engine

# Use the environment variable set in docker-compose
DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@db:5432/ny_taxi")
engine = create_engine(DB_URL)

def ingest_data():
    data_dir = "./data"
    if not os.path.exists(data_dir):
        print(f"Error: {data_dir} folder not found.")
        return

    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        table_name = os.path.splitext(file)[0] # e.g., 'taxi_data' from 'taxi_data.csv'
        ext = os.path.splitext(file)[1].lower()

        try:
            print(f"Processing {file}...")
            if ext == '.csv':
                df = pd.read_csv(file_path)
            elif ext == '.parquet':
                df = pd.read_parquet(file_path)
            elif ext in ['.xls', '.xlsx']:
                df = pd.read_excel(file_path)
            else:
                print(f"Skipping unsupported format: {ext}")
                continue

            # Load into SQL
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Successfully loaded {file} into table '{table_name}'")
            
        except Exception as e:
            print(f"Failed to process {file}: {e}")

if __name__ == "__main__":
    ingest_data()