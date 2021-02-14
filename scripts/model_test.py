"""
Doing some inital modelling/messing around with modelling data
"""
import os
import pandas as pd
import numpy as np

import xgboost as xgb
import scipy.stats as stats
from xgboost import plot_importance
from sklearn.metrics import mean_squared_error

f = os.path.join(os.getcwd(),'nba_predictions','data','James_Harden_2018_2019_2020_feature_engineered.csv')
df = pd.read_csv(f)
df
del df['opp']

df.shape

df_train = df.iloc[0:180,:]
df_test = df.iloc[180:,:]


xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)
