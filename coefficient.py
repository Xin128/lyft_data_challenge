
import pandas as pd
import datetime
import time
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

def compute_pearson_coefficient(factors):
    """
    compute pearson_coefficient with career length
    :param x:
    :param carreer_len:
    :return:
    """
    for col_x in factors.columns:
        for col_y in factors.columns:
            if col_x != 'driver_id' and col_y != 'driver_id':
                print(col_x, col_y,factors[col_x].corr(factors[col_y]))



def convert_time_to_sec(factors):
    for ind, row in factors.iterrows():
        x = time.strptime(row['responding'].split(' ')[2][:8], '%H:%M:%S')
        factors.loc[ind,'responding'] = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        y = time.strptime(row['arrival'].split(' ')[2][:8], '%H:%M:%S')
        factors.loc[ind,'arrival']  = datetime.timedelta(hours=y.tm_hour, minutes=y.tm_min, seconds=y.tm_sec).total_seconds()
    return factors


main_factors = pd.read_csv('/Users/xinhao/Downloads/lyft_data_challenge/0910/main_factors')
main_factors = convert_time_to_sec(main_factors)
print(main_factors)
compute_pearson_coefficient(main_factors)