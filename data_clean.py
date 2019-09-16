
import pandas as pd
import datetime
import numpy as np
# Load the Pandas libraries with alias 'pd'
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

driver_id_table = pd.read_csv("drop_out_drivers.csv")
data_ride_id = pd.read_csv("driver_ids.csv")
data_total_table = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/final/erin_code.csv')

print(data_total_table)

def compute_drives_per_day(current_table):
    """
    compute the number of drives per day
    :param id:
    :return:
    """
    date_sec = list(current_table['picked_up_at'])
    date = [x[:10] for x in date_sec]
    if len(set(date))==0:
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
    profits = []
    for ind,drive in current_table.iterrows():
        profit_per_drive = (2+1.15*drive['ride_distance']/1609.34+0.22*drive['ride_duration']/60)
        profit_after_prime = profit_per_drive+ drive['ride_prime_time']/float(drive['ride_duration'])*profit_per_drive*0.5+1.75
        if profit_after_prime < 5:
            profit_after_prime = 5
        elif profit_after_prime >400:
            profit_after_prime = 400
        profits.append(profit_after_prime)
    if len(current_table) ==0:
        return 0
    else:
        return profits

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
    return total/float(len(set(date)))

def compute_responding_time(current_table):
    """
#     compute average responding time
#     :param current_table:
#     :return:
#     """
    ride_num = 0.0
    responding_time = datetime.timedelta()

    for ind,drive in current_table.iterrows():
        try:
            request = datetime.datetime.strptime(drive['requested_at'],'%Y-%m-%d %H:%M:%S')
            pick_up = datetime.datetime.strptime(drive['picked_up_at'],'%Y-%m-%d %H:%M:%S')
            if pick_up > request:
                time = pick_up-request
                responding_time = responding_time+time
                ride_num += 1
            else:
                continue
        except:
            continue
    responding_time = int(responding_time.seconds)

    return responding_time/float(ride_num)

def compute_arrival_time(current_table):
    """
#     compute average responding time
#     :param current_table:
#     :return:
#     """
    responding_time = datetime.timedelta()
    ride_num = 0.0
    for ind,drive in current_table.iterrows():
        try:
            request = datetime.datetime.strptime(drive['accepted_at'],'%Y-%m-%d %H:%M:%S')
            pick_up = datetime.datetime.strptime(str(drive['arrived_at']),'%Y-%m-%d %H:%M:%S')

            if pick_up > request:
                time = pick_up - request
                responding_time = responding_time+time
                ride_num+=1
            else:
                continue
        except:
            continue
    responding_time = int(responding_time.seconds)
    # print(len(current_table),ride_num)
    return responding_time/float(ride_num)

def compute_waiting_time(current_table):
    """
#     compute average responding time
#     :param current_table:
#     :return:
#     """
    responding_time = datetime.timedelta()
    ride_num = 0;
    for ind,drive in current_table.iterrows():
        try:
            pick_up = datetime.datetime.strptime(drive['picked_up_at'],'%Y-%m-%d %H:%M:%S')
            arrive = datetime.datetime.strptime(drive['arrived_at'],'%Y-%m-%d %H:%M:%S')

            if pick_up > arrive:
                time = pick_up-arrive
                responding_time = responding_time+time
                ride_num +=1
            else:
                continue
        except:
            continue
    responding_time = int(responding_time.seconds)
    print(responding_time)
    return responding_time/float(ride_num)



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

def compute_10_to_6(current_table):
    slot = 0.0;
    for ind, drive in current_table.iterrows():
        accept_time = datetime.datetime.strptime(drive['accepted_at'], '%Y-%m-%d %H:%M:%S')
        if accept_time.hour >22 or accept_time.hour<6:
            slot+=1
    return float(slot)/len(current_table)

def compute_9_to_5(current_table):
    """
    compute the
    :param current_table:
    :return:
    """
    slot = 0.0;
    for ind, drive in current_table.iterrows():
        accept_time = datetime.datetime.strptime(drive['accepted_at'], '%Y-%m-%d %H:%M:%S')
        if accept_time.hour >9 and accept_time.hour<17:
            slot+=1
    return float(slot)/len(current_table)

def compute_20_to_22(current_table):
    slot = 0.0;
    for ind, drive in current_table.iterrows():
        accept_time = datetime.datetime.strptime(drive['accepted_at'], '%Y-%m-%d %H:%M:%S')
        if accept_time.hour >20 and accept_time.hour<22:
            slot+=1
    return float(slot)/len(current_table)

def compute_prime_percent(current_table):
    total_duration = sum(current_table['ride_duration'])
    total_prime_time = sum(current_table['ride_prime_time'])
    return total_prime_time / float(total_duration)

def compute_prime_total(current_table):
    total_duration = sum(current_table['ride_duration'])
    total_prime_time = sum(current_table['ride_prime_time'])
    return total_prime_time

def compute_career_length(current_table):
    """

    :param current_table:
    :return:
    """
    try:
        current_table = current_table.sort_values(['requested_at'], ascending=False)
        last_ride = datetime.datetime.strptime(current_table.iloc[0]['picked_up_at'], '%Y-%m-%d %H:%M:%S')
        driver_id = current_table.iloc[0]['driver']
        find_onboard = data_ride_id[data_ride_id['driver_id'] == driver_id].iloc[0]['driver_onboard_date']
        onboard_time = datetime.datetime.strptime(find_onboard, '%Y-%m-%d %H:%M:%S')
        time = last_ride - onboard_time
        career_len = int(time.days)
        return career_len
    except:
        return 0

def compute_weekends_per(current_table):
    weekends = 0
    date_sec = list(current_table['picked_up_at'])
    date = set([x for x in date_sec])
    for x in date:
        work_date = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
        if work_date.weekday()>5:
            weekends +=1
    return weekends / float(len(date))

def compute_std_profit(current_table):
    all_profit = std
    for ind, drive in current_table.iterrows():
        profit_per_drive = (2 + 1.15 * drive['ride_distance'] / 1609.34 + 0.22 * drive['ride_duration'] / 60)
        profit_after_prime = profit_per_drive + drive['ride_prime_time'] / float(
            drive['ride_duration']) * profit_per_drive * 0.5 + 1.75
        all_profit.append[profit_after_prime]
    return all_profit


factors = pd.DataFrame(columns = ['driver_id','career_len','rides_per_day','profit_mean','profit_std','responding','arrival',
                                  'waiting','speed','total_duration','average ride time', 'average dist per ride',
                                  '10_to_6','9_to_5','per_20_to_22','prime_time','total_prime_time','weekend_per'])

for driver_id in data_ride_id['driver_id']:
    current_table = data_total_table[data_total_table['driver'] == driver_id]
    print(driver_id)
    print('------------')
    if len(current_table) !=0:
        career_len = compute_career_length(current_table)
        num_per_day =  compute_drives_per_day(current_table)
        all_profit = compute_profit(current_table)
        profit_mean = np.mean(all_profit)
        profit_std = np.std(all_profit)
        responding_time = compute_responding_time(current_table)
        arrival_time = compute_arrival_time(current_table)
        waiting_time = compute_waiting_time(current_table)
        speed = compute_speed(current_table)
        dur= compute_total_duration(current_table)
        aver_ride_time = float(dur) / len(current_table)
        aver_dis_per_ride = float(current_table['ride_distance'].mean())/1609.34
        per_10_to_6 = compute_10_to_6(current_table)
        per_9_to_5 = compute_9_to_5(current_table)
        per_20_to_22 = compute_10_to_6(current_table)
        per_prime_dur = compute_prime_percent(current_table)
        total_prime = compute_prime_total(current_table)
        weekend_per = 1-compute_weekends_per(current_table)
        factors.loc[-1] = [driver_id, career_len,num_per_day, profit_mean, profit_std,responding_time,arrival_time,waiting_time,speed,dur,aver_ride_time,
                           aver_dis_per_ride, per_10_to_6, per_9_to_5, per_20_to_22, per_prime_dur,total_prime,weekend_per]
        print(factors.loc[-1])
        print(len(factors))
        factors.index = factors.index + 1
        factors = factors.sort_index()


factors.to_csv('total_004_for_800.csv')
# print(data_total_table)




