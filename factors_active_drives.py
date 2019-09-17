
import pandas as pd
import datetime
import numpy as np
# Load the Pandas libraries with alias 'pd'
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


data_ride_id = pd.read_csv("drop_out_drivers 2.csv")
driver_id_table = pd.read_csv("driver_ids.csv")
data_total_table = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/final/erin_code.csv')
print(driver_id_table)
def compute_drives_per_day(current_table):
    """
    compute the number of drives per day
    :param id:
    :return:
    """
    date_sec = list(current_table['picked_up_at'])
    date = [x[:10] for x in date_sec]
    if len(set(date)) == 0:
        return 0
    else:
        return float(len(date)) / len(set(date))

def compute_total_duration(current_table):
    total_dur = sum(current_table['ride_duration']/60)
    return total_dur

def compute_profit(current_table):
    """
    compute Avearge Profit per drive （average earning/day)
    have not considered prime time
    :param current_table:
    :return:
    """
    total = 0
    for ind,drive in current_table.iterrows():
        profit_per_drive = (2+1.15*drive['ride_distance']/1609.34+0.22*drive['ride_duration']/60)
        profit_after_prime = profit_per_drive+ drive['ride_prime_time']/float(drive['ride_duration'])*profit_per_drive*0.22
        if profit_after_prime < 5:
            profit_after_prime = 5
        elif profit_after_prime >400:
            profit_after_prime = 400
        total += profit_after_prime
    return total / float(len(current_table))

def compute_profit_per_day(current_table):
    total = 0
    for ind,drive in current_table.iterrows():
        profit_per_drive = 2+1.15*drive['ride_distance']/1609.34+0.22*drive['ride_duration']/60+1.75
        if profit_per_drive < 5:
            profit_per_drive = 5
        elif profit_per_drive >400:
            profit_per_drive = 400
        total += profit_per_drive
    # print(total,len(current_table),total / float(len(current_table)))
    date_sec = list(current_table['picked_up_at'])
    date = [x[:10] for x in date_sec]
    if len(set(date)) == 0:
        return 0
    else:
        return total / len(set(date))

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
            responding_time = int(responding_time.seconds)
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
            responding_time = int(responding_time.seconds)
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
            request = datetime.datetime.strptime(drive['picked_up_at'],'%Y-%m-%d %H:%M:%S')
            pick_up = datetime.datetime.strptime(drive['arrived_at'],'%Y-%m-%d %H:%M:%S')
            time = pick_up-request
            responding_time = responding_time+time
            responding_time = int(responding_time.seconds)
        except:
            continue
    return responding_time/float(len(current_table))



def compute_speed(current_table):
    total_dist = sum(list(current_table['ride_distance']))
    total_duration = sum(list(current_table['ride_duration']))
    return float(total_dist)/total_duration


def compute_pearson_coefficient(factors):
    """
    compute pearson_coefficient with career length
    :param x:
    :param carreer_len:
    :return:
    """
    for col in factors.columns:
        if col != 'driver_id':
            print(col, factors[col].corr(factors['career_len']))

def compute_career_length(current_table):
    """

    :param current_table:
    :return:
    """
    current_table = current_table.sort_values(['requested_at'], ascending=False)
    last_ride = datetime.datetime.strptime(current_table.iloc[0]['picked_up_at'], '%Y-%m-%d %H:%M:%S')
    driver_id = current_table.iloc[0]['driver']
    find_onboard = driver_id_table[driver_id_table['driver_id'] == driver_id].iloc[0]['driver_onboard_date']
    onboard_time = datetime.datetime.strptime(find_onboard, '%Y-%m-%d %H:%M:%S')
    time = last_ride - onboard_time
    career_len = int(time.days)
    return career_len

factors = pd.DataFrame(columns = ['driver_id','career_len','rides_per_day','profit','responding','arrival','waiting','speed','total_duration'])
for driver_id in driver_id_table['driver_id']:
    current_table = data_total_table[data_total_table['driver'] == driver_id]
    if len(current_table) > 0:
        num_per_day =  compute_drives_per_day(current_table)
        profit = compute_profit_per_day(current_table)
        responding_time = compute_responding_time(current_table)
        arrival_time = compute_arrival_time(current_table)
        waiting_time = compute_waiting_time(current_table)
        speed = compute_speed(current_table)
        dur = compute_total_duration(current_table)
        career_len = compute_career_length(current_table)
        factors.loc[-1] = [driver_id, career_len,num_per_day, profit,responding_time,arrival_time,waiting_time,speed,dur]
        factors.index = factors.index + 1
        factors = factors.sort_index()

    print(len(factors))

factors.to_csv('main_factors_new.csv')
# print(data_total_table)


