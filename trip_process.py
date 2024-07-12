import pyarrow.parquet as pq

# Read the Parquet file into a PyArrow table
trips = pq.read_table('fhv_apr24_trips.parquet')

# Convert the PyArrow table to a pandas DataFrame
trips_df = trips.to_pandas()

# Display the head of the DataFrame
print(trips_df)

# Compute the average of the 'trip_miles' column
average_trip_miles = trips_df['trip_miles'].mean()

# Print the average
print(f"Average trip miles: {average_trip_miles}")
