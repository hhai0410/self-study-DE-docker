import sys
import pandas as ps
month = sys.argv[1]

print(f"Running pipeline for month {month}")

df = ps.DataFrame({"Booking_ID":[1, 2, 3], "Room_Number":[101,203,305], "Guest_Name":["Alice", "Bob", "Charlie"]})
df['month'] = month
print(df.head())

df.to_parquet(f"hotel_booking_month_{month}.parquet")