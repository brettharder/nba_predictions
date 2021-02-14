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
#f = os.path.join(os.getcwd(),'nba_predictions','data','Lebron_James_2018_2019_2020_feature_engineered.csv')
df = pd.read_csv(f)
df
del df['opp']

df.shape

df_train = df.iloc[0:170,:]
df_test = df.iloc[170:,:]

xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 10, alpha = 10, n_estimators = 100)

xg_reg.fit(df_train.drop(['pts'],axis=1),df_train['pts'])
preds = xg_reg.predict(df_test.drop(['pts'],axis=1))
preds
np.array(df_test['pts'])

preds - np.array(df_test['pts'])

xg_reg.get_booster().get_score(importance_type="gain")

# -----------------------------------------
# Quickly see how a binary prediction works
# -----------------------------------------
df['30+'] = np.where(
    df['pts'] >= 30, 1, 0
)
df

df_train = df.iloc[0:150,:]
df_test = df.iloc[150:,:]

model = xgb.XGBClassifier(objective ='binary:logistic', max_depth = 10, n_estimators = 100)

model.fit(df_train.drop(['pts','30+'],axis=1),df_train['30+'])
preds = model.predict_proba(df_test.drop(['pts','30+'],axis=1))[:,1]
preds
labels = np.where(preds > .5, 1, 0)
labels

np.array(df_test['30+'])
labels - np.array(df_test['30+'])

model.get_booster().get_score(importance_type="gain")