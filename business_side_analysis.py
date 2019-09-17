"""
Ride distribution over the day
Value generated over the day
Waiting time distribution over the day
Responding time distribution over the day
Arriving Time distribution over the day
Average speed distribution over the day
Prime time distribution over the day

Segment each day into 24 hrs (time based on the request time of a ride)
(0,1), (1,2).....(23,24)
0, 1, 2, ......., 23
"""
from collections import defaultdict
from pylab import *
import matplotlib.pylab as plt
import pandas as pd
import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

loc = "/Users/liutianrui/Desktop/erin_code.csv"
df = pd.read_csv(loc)
df = df.drop("Unnamed: 0", axis=1)
# print (df.head())

def classify_time (time):
    date = time.split(" ")[0]
    t = time.split(" ")[1]
    type = t.split(":")[0]
    if type[0] == "0":
        return int(type[1])
    else:
        return int(type)

def classify_time_date (time):
    date = time.split(" ")[0]
    work_date = datetime.datetime.strptime(date, '%Y-%m-%d')

    return work_date.weekday()

# 1.  classify rides based on their time
rides_class = defaultdict(int)

for idx, row in df.iterrows():
    if idx not in [87666]:
        time = row["requested_at"]
        type = classify_time_date(time)
        rides_class[type] += 1

# print (len(rides_class))
# print (rides_class)

#2.  classify rides based on their value
val_class = defaultdict(float)

for idx, row in df.iterrows():
     if idx not in [87666]:
        time = row["requested_at"]
        type = classify_time_date(time)
        profit_per_drive = (2+1.15*row['ride_distance']/1609.34+0.22*row['ride_duration']/60)
        profit_after_prime = profit_per_drive+ row['ride_prime_time']/float(row['ride_duration'])*profit_per_drive*0.22
        val_class[type] += profit_after_prime

print (len(val_class))
print (val_class)

# 3.  average ride responding time (accept to request), arriving time (arrive to accept)
# waiting time (pickup to arrive)
respond_class = defaultdict(int)
arrive_class = defaultdict(int)
wait_class = defaultdict(int)

for idx, row in df.iterrows():
    if idx not in [87666]:
        time = row["requested_at"]
        type = classify_time_date(time)
        responding_time = datetime.timedelta()
        accept = datetime.datetime.strptime(row['accepted_at'],'%Y-%m-%d %H:%M:%S')
        request = datetime.datetime.strptime(row['requested_at'],'%Y-%m-%d %H:%M:%S')
        arrive = datetime.datetime.strptime(row['arrived_at'], '%Y-%m-%d %H:%M:%S')
        pickup = datetime.datetime.strptime(row['picked_up_at'], '%Y-%m-%d %H:%M:%S')

        if accept > request:
            res = accept - request
        if arrive > accept:
            arr = arrive - accept
        if pickup > arrive:
            wait = pickup - arrive
        respond_class[type] += int(res.seconds)
        arrive_class[type] += int(arr.seconds)
        wait_class[type] += int(wait.seconds)

for type, val in respond_class.items():
    respond_class[type] = float(val)/ rides_class[type]

for type, val in arrive_class.items():
    arrive_class[type] = float(val)/ rides_class[type]

for type, val in wait_class.items():
    wait_class[type] = float(val)/ rides_class[type]

# print (respond_class)
# print (arrive_class)
# print (wait_class)
ride = sorted(rides_class.items()) # sorted by key, return a list of tuples
respond = sorted(respond_class.items())
arrive = sorted(arrive_class.items())
wait = sorted(wait_class.items())

x1, y1 = zip(*ride) # unpack a list of pairs into two tuples
x2, y2 = zip(*respond)
x3, y3 = zip(*arrive)
x4, y4 = zip(*wait)

plt.subplot(2,2,1)
plt.title("Distribution of number of rides throughout the week")
#plt.title("Distribution of number of rides throughout the day")
plt.bar([x+1 for x in x1], y1, color='#0504aa')

plt.subplot(2,2,2)
plt.title("Distribution of average responding time throughout the week")
#plt.title("Distribution of average responding time throughout the day")
plt.bar([x+1 for x in x2], y2, color='#0504aa')

plt.subplot(2,2,3)
plt.title("Distribution of average arriving time throughout the week")
#plt.title("Distribution of average arriving time throughout the day")
plt.bar([x+1 for x in x3], y3, color='#0504aa')

plt.subplot(2,2,4)
plt.title("Distribution of average waiting time throughout the week")
#plt.title("Distribution of average waiting time throughout the day")
plt.bar([x+1 for x in x4], y4, color='#0504aa')

plt.show()


# 4 classify ride on week days
# day_type_class = defaultdict(int)
# for idx, row in df.iterrows():
#     if idx not in [87666]:
#         time = row["requested_at"]
#         day_type = classify_time_date(time)
#         day_type_class[day_type] += 1
#
# w_d = sorted(day_type_class.items())
#
# x_d, y_d = zip(*w_d) # unpack a list of pairs into two tuples
# plt.title("Distribution of rides throughout a week")
# plt.bar([x+1 for x in x_d], y_d)
#
# plt.show()

