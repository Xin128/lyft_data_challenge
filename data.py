
import pandas as pd
import datetime
# Load the Pandas libraries with alias 'pd'
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)



def merge_data():
    total_rides = pd.DataFrame(columns = ['ride_id','requested_at','accepted_at','arrived_at','picked_up_at','dropped_off_at',
                                'ride_duration','ride_distance','ride_prime_time','driver'])
    data_ride_id = pd.read_csv("ride_ids.csv")
    data_ride_timestamp = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/ride_timestamps.csv')
    data_driver_id = pd.read_csv('/Users/xinhao/Downloads/driver_ids.csv')
    num_rides = len(data_ride_timestamp)/5
    for ind, row in data_ride_id.iterrows():
        all_events = data_ride_timestamp[data_ride_timestamp['ride_id'] == row['ride_id']]
        if len(all_events)!= 0:
            request = all_events[all_events['event'] == 'requested_at']['timestamp'].values[0]
            accept = all_events[all_events['event'] == 'accepted_at']['timestamp'].values[0]
            arrive = all_events[all_events['event'] == 'arrived_at']['timestamp'].values[0]
            pick = all_events[all_events['event'] == 'picked_up_at']['timestamp'].values[0]
            drop = all_events[all_events['event'] == 'dropped_off_at']['timestamp'].values[0]
            total_rides.loc[-1] = [row['ride_id'],request,accept,arrive,pick,drop,row['ride_duration'],row['ride_distance'],
                               row['ride_prime_time'],row['driver_id']]
            total_rides.index = total_rides.index + 1
            total_rides = total_rides.sort_index()
        print(ind)
    return total_rides

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data_ride_id= pd.read_csv("ride_ids.csv")
data_ride_timestamp = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/ride_timestamps.csv')
data_driver_id = pd.read_csv('/Users/xinhao/Downloads/driver_ids.csv')
check_timestamp = data_ride_timestamp.loc[data_ride_timestamp['ride_id'] == '006d61cf7446e682f7bc50b0f8a5bea5']
check_ride_id = data_ride_id.loc[data_ride_id['ride_id'] == '006d61cf7446e682f7bc50b0f8a5bea5']
print(type(check_timestamp))
total_rides = merge_data()
total_rides.to_csv('all_rides')
quit()


# Preview the first 5 lines of the loaded data
print(data_driver_id.columns)
# sorted_driver = data_driver_id.sort_values('ride_duration',ascending = False)
print(data_driver_id)
print(data_ride_timestamp)
# print(data_ride_id)
# sorted_driver = data_ride_id.sort_values('ride_prime_time',ascending = False)

time1 = data_ride_timestamp.iloc[0]['timestamp']
time2 = data_ride_timestamp.iloc[1]['timestamp']
time1_obj = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
time2_obj = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
print(data_ride_timestamp)

print(time2_obj-time1_obj)
