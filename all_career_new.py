import pandas as pd

Location1 = "/Users/xinhao/Downloads/lyft_data_challenge/final/erin_code.csv"
drive_df = pd.read_csv(Location1)
Location2 = "driver_ids.csv"
driver_df = pd.read_csv(Location2)










# read drivers and their on_board date into dict
drivers = {}
for index, row in driver_df.iterrows():
    dr = row["driver_id"]
    on_board_time = row["driver_onboard_date"]
    drivers[dr] = on_board_time

# find the most recent ride : No. 365    2016-06-26 23:57:45   ---   2016-03-28 05:48:18
# change the on board date format
for idx, row in drive_df["requested_at"].items():
    c_dr = drive_df["driver"][idx]

    # # remove drivers without on_board date
    # if c_dr not in drivers.keys():
    #     drive_df.drop(idx)
    #     continue

    date = row.split("-")
    if len(date[1]) == 1:
        new_date = date[0] + "/0" + date[1] + "/" + date[2]
        drive_df.set_value(idx, "requested_at", new_date)

Sorted = drive_df.sort_values(['requested_at'], ascending=False)
#print (Sorted["requested_at"])


# find inactive drivers
# 20 days ago: 6/06/16
all_drivers = driver_df["driver_id"]
on_board_time = driver_df["driver_onboard_date"]

active_drivers = set([])
current_drivers = set([])
inactive_drivers_workhr = {}

#add the drivers after the break point
for idx, time in Sorted["requested_at"].items():
    if time.startswith('6/06/16'):
        break
    active_drivers.add(Sorted["driver"][idx])

for idx, time in Sorted["requested_at"].items():
    current_drivers.add(Sorted["driver"][idx])

# drop drivers without on_board_date
current_drivers = list(current_drivers)
active_drivers = list(active_drivers)


for dr in current_drivers:
    if dr not in drivers.keys():
        current_drivers.remove(dr)

for dr in active_drivers:
    if dr not in drivers.keys():
        active_drivers.remove(dr)

# print (len(active_drivers)) # 625
# print (len(current_drivers)) # 837
#
# print (len(set(current_drivers).difference(set(active_drivers))))
#
inactive_drivers = (set(current_drivers).difference(set(active_drivers))) # 212


def compute_length(on_board_date, current_date):
    print(on_board_date,current_date)
    s_ds = on_board_date.split("-")
    c_ds = current_date.split("-")
    s_month = int(s_ds[0])
    s_day = int(s_ds[1])
    c_month = int(c_ds[0])
    c_day = int(c_ds[1])

    if s_month == c_month:
        return c_day - s_day
    else:
        if s_month == 3 and c_month == 4:
            return 31-s_day + c_day
        if s_month == 3 and c_month == 5:
            return 31-s_day + 30 + c_day
        if s_month == 3 and c_month == 6:
            return 31-s_day + 61 + c_day
        if s_month == 4 and c_month == 5:
            return 30-s_day+c_day
        if s_month == 4 and c_month == 6:
            return 30-s_day + 31 + c_day
        else:
            return 31-s_day + c_day

# find the last ride of inactive drivers
for idx, time in Sorted["requested_at"].items():
    c_dr = Sorted["driver"][idx]
    if c_dr in inactive_drivers:
        if c_dr not in inactive_drivers_workhr.keys():
            inactive_drivers_workhr[c_dr] = time
print(inactive_drivers_workhr)

# find the career length of inactive drivers
for dr in inactive_drivers:
    print(drivers[dr], inactive_drivers_workhr[dr])
    inactive_drivers_workhr[dr] = compute_length(drivers[dr], inactive_drivers_workhr[dr])

# print (inactive_drivers_workhr)
# average career length of drop-out drivers

# avr = float(sum(inactive_drivers_workhr.values())) / len(inactive_drivers_workhr)
# print (avr) 27.995283018867923

# write drop-out drivers' information into a dataframe & output csv file
data = []
for id, days in  (inactive_drivers_workhr.items()):
    data.append([id, days])
# for id, days in  (inactive_drivers_workhr.items()):
#     data.append([id, days])

inact_df = pd.DataFrame(data, columns = ['driver_id', 'career_length'])

inact_df.to_csv(r'all_career_new.csv')
