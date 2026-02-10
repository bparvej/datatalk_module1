import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5433/ny_taxi"
)

# ---------- Green taxi trips (Parquet) ----------
print("Loading green taxi data...")
df_green = pd.read_parquet("data/green_tripdata_2025-11.parquet")

df_green.to_sql(
    "green_tripdata",
    engine,
    if_exists="replace",
    index=False
)

print("Green taxi data loaded")

# ---------- Taxi zones (CSV) ----------
print("Loading taxi zones...")
df_zones = pd.read_csv("data/taxi_zone_lookup.csv")

df_zones.to_sql(
    "taxi_zone_lookup",
    engine,
    if_exists="replace",
    index=False
)

print("Taxi zones loaded")
