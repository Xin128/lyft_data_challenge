# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Location1 = "/Users/liutianrui/Desktop/drop_out_drivers.csv"
# drop_out = pd.read_csv(Location1)

# x = []
# y = []
# for idx, row in drop_out.iterrows():
#     id = row["driver_id"]
#     length = row["career_length"]
#     x.append(id)
#     y.append(length)
#
# plt.scatter(x,y)
# plt.show()


# correlation result:
# career_len Unnamed: 0 0.7582875786513847
# career_len career_len 0.9999999999999998
# career_len rides_per_day -0.09991971712322564 (mild, have trend)
# career_len responding -0.01867912490201997
# career_len arrival -0.03260281643681055
# career_len speed 0.009380393772661767 (mild, not trend)

# career_len waiting -0.28145012879390385 (almost none)
# career_len total_duration 0.4374133992561635 (ok)
# career_len profit 0.44338364542657593 (ok)

loc = "/Users/liutianrui/Desktop/main_factors_new.csv"
df=pd.read_csv(loc)
# responding arrival speed
plt.scatter(df['speed'], df['career_len'], color='red')
plt.title('speed Vs Career Length', fontsize=14)
plt.xlabel('speed', fontsize=14)
plt.ylabel('Career Length', fontsize=14)
plt.grid(True)
plt.show()


plt.scatter(df['rides_per_day'], df['career_len'], color='red')
plt.title('rides_per_day Vs Career Length', fontsize=14)
plt.xlabel('rides_per_day', fontsize=14)
plt.ylabel('Career Length', fontsize=14)
plt.grid(True)
plt.show()


plt.scatter(df['total_duration'], df['career_len'], color='red')
plt.title('total_duration Vs Career Length', fontsize=14)
plt.xlabel('total_duration', fontsize=14)
plt.ylabel('Career Length', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['profit'], df['career_len'], color='red')
plt.title('profit Vs Career Length', fontsize=14)
plt.xlabel('profit', fontsize=14)
plt.ylabel('Career Length', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['waiting'], df['career_len'], color='red')
plt.title('waiting Vs Career Length', fontsize=14)
plt.xlabel('waiting', fontsize=14)
plt.ylabel('Career Length', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['responding'], df['career_len'], color='red')
plt.title('responding Vs Career Length', fontsize=14)
plt.xlabel('responding', fontsize=14)
plt.ylabel('Career Length', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['arrival'], df['career_len'], color='red')
plt.title('arrival Vs Career Length', fontsize=14)
plt.xlabel('arrival', fontsize=14)
plt.ylabel('Career Length', fontsize=14)
plt.grid(True)
plt.show()

# plt.scatter(df['total_duration'], df['career_len'], color='red')
# plt.title('Total duration Vs Career Length', fontsize=14)
# plt.xlabel('Total duration', fontsize=14)
# plt.ylabel('Career Length', fontsize=14)
# plt.grid(True)
# plt.show()

# split into training and testing dataset
#X_train, X_eval,y_train,y_eval=train_test_split(x_data,y_val,test_size=0.3,random_state=101)


# # multivariate linear regression
# Location2 = "/Users/liutianrui/Desktop/0910/main_factors"
# df=pd.read_csv(Location2)
#
# y_val = df[["career_len"]]
# # columns in the order: profit, waiting, total_duration
# x_data = df.drop(["Unnamed: 0","rides_per_day","responding","arrival","speed","driver_id","waiting"], axis = 1)
#

