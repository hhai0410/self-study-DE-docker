import sys
import pandas as pd
print("arguments: ", sys.argv)
month = int(sys.argv[1])
print("hello pipeline", month)
df = pd.DataFrame({"Room_Number": [1, 2], "Passenger_Number": [3,4]})
df['month'] = month
print(df.head())
df.to_parquet(f"Data_Of_{month}.parquet")

