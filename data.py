# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data_ride_id= pd.read_csv("ride_ids.csv")
data_ride_timestamp = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/ride_timestamps.csv')
data_driver_id = pd.read_csv('/Users/xinhao/Downloads/driver_ids.csv')
# Preview the first 5 lines of the loaded data
print(data_ride_id)
print(data_ride_timestamp)
print(data_driver_id)