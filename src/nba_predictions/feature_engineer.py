"""
Pretty basic feature engineering to prepare data for modelling.
Currently build the following features
  use past 10 games as input for predicting performance in next game:
    - average minutes played: MP
    - average field goal attempted: FGA
    - average field goal percentage: FG%
    - average 3point attempted: 3PA
    - average 3point percentage: 3P%
    - average free throw attempted: FTA
    - average free throw percentage: FT%    
    - average turnovers: TOV
    - average personal fouls: PF
    - average points: PTS
TODO: Add some more features, test out different approaches
"""
import os
import pandas as pd
import numpy as np

def preprocess_player_data(f):
    # Read in data 
    df = pd.read_csv(f)

    # remove inactive games 
    df = df[df['G'].notnull()].reset_index(drop=True)

    # Fill na's and fix a few cols
    df = df.fillna(0)
    df['MP'] = df['MP'].str.replace(':','.')

    return df

def create_feature(df,row,feat,lb_games=10):
    df = df.fillna(0)
    feat = df[feat][row-lb_games:row].astype(float).mean()
    return feat

def feature_engineer(f,lb_games=10):
    df = preprocess_player_data(f)

    # Features
    l_avg_mp = []
    l_avg_fga = []
    l_avg_fgp = []
    l_avg_3pa = []
    l_avg_3pp = []
    l_avg_fta = []
    l_avg_ftp = []
    l_avg_to = []
    l_avg_pf = []
    l_avg_pts = []
    
    # Here we have the opponent for the game and the outcome (points scored)
    l_opp = []
    l_pts = []

    # Loop through games to create features and outcome
    for i in df.index[lb_games:]:
        l_avg_mp.append(create_feature(df,i,'MP',lb_games))
        l_avg_fga.append(create_feature(df,i,'FGA',lb_games)) 
        l_avg_fgp.append(create_feature(df,i,'FG%',lb_games))
        l_avg_3pa.append(create_feature(df,i,'3PA',lb_games))
        l_avg_3pp.append(create_feature(df,i,'3P%',lb_games))
        l_avg_fta.append(create_feature(df,i,'FTA',lb_games))
        l_avg_ftp.append(create_feature(df,i,'FT%',lb_games))
        l_avg_to.append(create_feature(df,i,'TOV',lb_games))
        l_avg_pf.append(create_feature(df,i,'PF',lb_games))
        l_avg_pts.append(create_feature(df,i,'PTS',lb_games))

        l_opp.append(df['Opp'][i])
        l_pts.append(df['PTS'][i])

    df_feat = pd.DataFrame({
        'avg_mp': l_avg_mp,
        'avg_fga': l_avg_fga,
        'avg_fgp': l_avg_fgp,
        'avg_3pa': l_avg_3pa,
        'avg_3pp': l_avg_3pp,
        'avg_fta': l_avg_fta,
        'avg_ftp': l_avg_ftp,
        'avg_to': l_avg_to,
        'avg_pf': l_avg_pf,
        'avg_pts': l_avg_pts,
        'opp': l_opp,
        'pts': l_pts
    })

    return df_feat