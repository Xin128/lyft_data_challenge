import pandas as pd
import datetime
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

data_total_table = pd.read_csv('main_factors_new.csv')

drop_out_drivers = pd.read_csv('drop_out_drivers.csv')
inactive = pd.DataFrame(columns = ['driver_id','career_len','rides_per_day','profit','responding','arrival',
                                  'waiting','speed','total_duration','average ride time', 'average dist per ride','10_to_6','9_to_5','prime_time'])

for id in drop_out_drivers['driver_id'].values:
    driver = data_total_table[data_total_table['driver_id'] == id]
    inactive = pd.concat([inactive,driver],ignore_index=True, sort =False)

inactive.to_csv('drop_out_full_info.csv')