
import pandas as pd
import datetime
# Load the Pandas libraries with alias 'pd'
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

data_ride_id = pd.read_csv("drop_out_drivers.csv")
data_total_table = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/final/erin_code.csv')


def compute_drives_per_day(current_table):
    """
    compute the number of drives per day
    :param id:
    :return:
    """
    date_sec = list(current_table['picked_up_at'])
    date = [x[:10] for x in date_sec]
    return float(len(date)) / len(set(date))

def compute_profit(current_table):
    """
    compute Avearge Profit per drive （average earning/day)
    have not considered prime time
    :param current_table:
    :return:
    """
    total = 0
    for ind,drive in current_table.iterrows():
        profit_per_drive = 2+1.15*drive['ride_distance']+0.22*drive['ride_duration']+1.75
        if profit_per_drive < 5:
            profit_per_drive = 5
        elif profit_per_drive >400:
            profit_per_drive = 400
        total += profit_per_drive
    # print(total,len(current_table),total / float(len(current_table)))
    return total / float(len(current_table))

def compute_responding_time(current_table):
    """
#     compute average responding time
#     :param current_table:
#     :return:
#     """
    responding_time = datetime.timedelta()
    for ind,drive in current_table.iterrows():
        try:
            request = datetime.datetime.strptime(drive['requested_at'],'%Y-%m-%d %H:%M:%S')
            pick_up = datetime.datetime.strptime(drive['picked_up_at'],'%Y-%m-%d %H:%M:%S')
            time = pick_up-request
            responding_time = responding_time+time
        except:
            continue
    return responding_time/float(len(current_table))

def compute_arrival_time(current_table):
    """
#     compute average responding time
#     :param current_table:
#     :return:
#     """
    responding_time = datetime.timedelta()
    for ind,drive in current_table.iterrows():
        try:
            request = datetime.datetime.strptime(drive['accepted_at'],'%Y-%m-%d %H:%M:%S')
            pick_up = datetime.datetime.strptime(drive['arrived_at'],'%Y-%m-%d %H:%M:%S')
            time = pick_up-request
            responding_time = responding_time+time
        except:
            continue
    return responding_time/float(len(current_table))

def compute_waiting_time(current_table):
    """
#     compute average responding time
#     :param current_table:
#     :return:
#     """
    responding_time = datetime.timedelta()
    for ind,drive in current_table.iterrows():
        try:
            request = datetime.datetime.strptime(current_table.iloc[ind+1]['picked_up_at'],'%Y-%m-%d %H:%M:%S')
            arr = datetime.datetime.strptime(current_table.iloc[ind]['arrived_at'],'%Y-%m-%d %H:%M:%S')
            time = pick_up-request
            responding_time = responding_time+time
        except:
            continue
    return responding_time/float(len(current_table)-1)

def compute_speed(current_table):
    total_dist = sum(list(current_table['ride_distance']))
    total_duration = sum(list(current_table['ride_duration']))
    return float(total_dist)/total_duration

factors = pd.DataFrame(columns = ['driver_id','career_len','rides_per_day','profit','responding','arrival','waiting','speed'])
for driver_id in data_ride_id['driver_id']:
    current_table = data_total_table[data_total_table['driver'] == driver_id]
    career_len = data_ride_id[data_ride_id['driver_id']== driver_id]['career_length'].values[0]
    num_per_day =  compute_drives_per_day(current_table)
    profit = compute_profit(current_table)
    responding_time = compute_responding_time(current_table)
    arrival_time = compute_arrival_time(current_table)
    waiting_time = compute_waiting_time(current_table)
    speed = compute_speed(current_table)
    print(factors)
    factors.loc[-1] = [driver_id, career_len,num_per_day, profit,responding_time,arrival_time,waiting_time,speed]
    factors.index = factors.index + 1
    factors = factors.sort_index()
print(factors)
factors.to_csv('main_factors')
# print(data_total_table)




