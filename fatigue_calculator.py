import pandas as pd
import matplotlib
import numpy as np

data1 = pd.ExcelFile("/Users/pradymanepalli/MSAS_Hackathon/UM_field_hockey.xlsx")
data = data1.parse('Sheet1')

def find_max_player_load_per_min(day, player_name):
    s = data[data['Date'] == day]
    s = data[data['Player Name'] == player_name]
    s = s[s['Date'] == day]
    m = s['Player Load Per Minute']
    if len(m) > 0:
        return max(m)
    else:
        return np.nan

def find_max_player_IMA(day, player_name):
    s = data[data['Date'] == day]
    s = data[data['Player Name'] == player_name]
    s = s[s['Date'] == day]
    m = s['High IMA']
    if len(m) > 0:
        return max(m)
    else:
        return np.nan


dates = data['Date'].unique()
for p in data['Player Name'].unique():
    stress_df = pd.DataFrame()
    stress_df['max_player_load_per_min'] = [find_max_player_load_per_min(day, p) for day in dates]
    stress_df['rolling_load'] = pd.rolling_mean(stress_df['max_player_load_per_min'], window=5)
    stress_df['stress_score'] = stress_df['max_player_load_per_min'] - stress_df['rolling_load']
    stress_df['High IMA'] = [find_max_player_IMA(day, p) for day in dates]
    stress_df.to_csv('./' + p + '-improved-stress_df_out.csv')