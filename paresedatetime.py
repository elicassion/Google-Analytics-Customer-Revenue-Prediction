import os, codecs, json, time
import pandas as pd
import numpy as np
import sklearn as sl


train_df_f = pd.read_csv('data\\f_train.csv', nrows=1000)
# def split_datetime(df):
#     new_years, new_months, new_days, new_daytime, new_weekday = zip(*[(d.year, d.month, d.day, d.hour, d.weekday()) for d in pd.to_datetime(df.visitStartTime)])
#     df = df.assign(visit_year=new_years, 
#                    visit_month=new_months, 
#                    visit_day=new_days, 
#                    visit_daytime=new_daytime, 
#                    visit_weekday=new_weekday)
#     return df.drop(columns=['visitStartTime'])
print (train_df_f.visitStartTime)
print (pd.to_datetime(train_df_f.visitStartTime, unit='s'))
# train_df_f = split_datetime(train_df_f)