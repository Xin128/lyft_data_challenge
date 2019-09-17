import pandas as pd
import matplotlib.pyplot as plt

loc = "/Users/liutianrui/Desktop/all.csv"
df = pd.read_csv(loc)

# calculate life time value
df["lifetime_value"] = df["rides_per_day"] * df["profit_mean"] * df["career_len"]

df.to_csv(r"/Users/liutianrui/Desktop/full_df.csv")
career_len = df["career_len"]

c = [str(1- item/100.0) for item in career_len]

#plot life time value against factors
# plt.scatter(df['speed'], df['lifetime_value'], color=c)
# plt.title('speed Vs life time value', fontsize=14)
# plt.xlabel('speed', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['rides_per_day'], df['lifetime_value'], color=c)
# plt.title('rides per day Vs life time value', fontsize=14)
# plt.xlabel('rides per day', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['profit_std'], df['lifetime_value'], color=c)
# plt.title('profit standard deviation Vs life time value', fontsize=14)
# plt.xlabel('profit standard deviation', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['waiting'], df['lifetime_value'], color=c)
# plt.title('average waiting time Vs life time value', fontsize=14)
# plt.xlabel('average waiting time', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['arrival'], df['lifetime_value'], color=c)
# plt.title('average arriving time Vs life time value', fontsize=14)
# plt.xlabel('average arriving time', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['total_duration'], df['lifetime_value'], color=c)
# plt.title('total ride duration Vs life time value', fontsize=14)
# plt.xlabel('total ride duration', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
#
# plt.scatter(df['average_dist_per_ride'], df['lifetime_value'], color=c)
# plt.title('average distance per ride Vs life time value', fontsize=14)
# plt.xlabel('average distance per ride', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['10_to_6'], df['lifetime_value'], color=c)
# plt.title('10pm-6am proportion Vs life time value', fontsize=14)
# plt.xlabel('proportion', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['9_to_5'], df['lifetime_value'], color=c)
# plt.title('9am-5pm proportion Vs life time value', fontsize=14)
# plt.xlabel('proportion', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['per_20_to_22'], df['lifetime_value'], color=c)
# plt.title('20pm-22pm proportion Vs life time value', fontsize=14)
# plt.xlabel('proportion', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['per_20_to_22'], df['lifetime_value'], color=c)
# plt.title('20pm-22pm proportion Vs life time value', fontsize=14)
# plt.xlabel('proportion', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
# plt.scatter(df['weekend_per'], df['lifetime_value'], color=c)
# plt.title('weekday proportion Vs life time value', fontsize=14)
# plt.xlabel('proportion', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
#

#
# plt.scatter(df['responding'], df['lifetime_value'], color=c)
# plt.title('responding time Vs life time value', fontsize=14)
# plt.xlabel('responding time', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
#
#
# plt.scatter(df['average_ride_time'], df['lifetime_value'], color=c)
# plt.title('average ride time Vs life time value', fontsize=14)
# plt.xlabel('average ride time', fontsize=14)
# plt.ylabel('life time value', fontsize=14)
# plt.grid(True)
# plt.show()
