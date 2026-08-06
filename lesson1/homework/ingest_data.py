
import pandas as pd 
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import pyarrow.parquet as pq
import urllib.request
import requests

prefix = "https://d37ci6vzurychx.cloudfront.net/trip-data"
url = f"{prefix}/green_tripdata_2025-11.parquet"
local_file = "green_tripdata_2025-11.parquet"
urllib.request.urlretrieve(url, local_file)

response = requests.get(url, stream=True)
response.raise_for_status()
df = pq.ParquetFile(local_file)
chunksize = 100000

engine = create_engine("postgresql+psycopg://root:root@localhost:5432/homework_db")

first = True
for batch in tqdm(df.iter_batches(batch_size=10_000)):
    df_chunk = batch.to_pandas()
    if first:
        df_chunk.head(0).to_sql("green_trip_data", con = engine, if_exists="replace", index=False)
        first = False
    df_chunk.to_sql("green_trip_data", con = engine, if_exists="append", index=False)
print("-----Import Data Completely-----")




