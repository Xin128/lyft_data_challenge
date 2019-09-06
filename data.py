
import pandas as pd
import datetime
# Load the Pandas libraries with alias 'pd'
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data_ride_id= pd.read_csv("ride_ids.csv")
data_ride_timestamp = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/ride_timestamps.csv')
data_driver_id = pd.read_csv('/Users/xinhao/Downloads/driver_ids.csv')
# Preview the first 5 lines of the loaded data
sorted_driver = data_ride_id.sort_values('ride_prime_time',ascending = False)

# print(sorted_driver)
# print(data_ride_id)
# sorted_driver = data_ride_id.sort_values('ride_prime_time',ascending = False)
print(data_ride_timestamp)
print(type(data_ride_timestamp.iloc[1]['timestamp']))
str_time = data_ride_timestamp.iloc[1]['timestamp']
date_time_obj = datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
print(type(date_time_obj))
# print(data_driver_id)