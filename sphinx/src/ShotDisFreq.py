import numpy as np
import pandas as pd 

import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

cf.go_offline() # required to use plotly offline (no account required).
py.init_notebook_mode() # graphs charts inline (IPython).


def shotDis_Freq(season, player1, player2, player3, player4, player5, feat):
    '''
    This function plot the frequency of FGM, FGA or FG% based on the season and 5 players and the selected attribute
    
    :param season: Selected Season
    :type season: int

    :param player1-5: The 5 selected players
    :type player1-5: string

    :param feat: the selected attribute (FGM, FGA or FG%)
    :type feat: string
    
    :return: Frequency of attributed from different distances 
    '''
    
    assert isinstance(season, int) 
    assert isinstance(player1, str) and isinstance(player2, str) and isinstance(player3, str) and isinstance(player4, str) and isinstance(player5, str)
    assert isinstance(feat, str)
    
    stats = pd.read_csv('shotDis_'+str(season)+'-'+ str(season+1)+ ".csv")
    stats.fillna(0)
    
    # Add row for league averages 
    avg = {'PLAYER_NAME': 'League Average',
           'TEAM_ABBREVIATION': 'AVG'}
    for i in list(stats.columns)[2:]:
        avg[i] = stats[i].mean()
    stats = stats.append(avg, ignore_index=True)
         
    # Find the total FGM, FGA, FG% for all distance 
    stats['FGM_Tot'] = stats['FGM']+stats['FGM.1']+stats['FGM.2']+stats['FGM.3']+stats['FGM.4']+stats['FGM.5']+stats['FGM.6']+stats['FGM.7']+stats['FGM.8']
    stats['FGA_Tot'] = stats['FGA']+stats['FGA.1']+stats['FGA.2']+stats['FGA.3']+stats['FGA.4']+stats['FGA.5']+stats['FGA.6']+stats['FGA.7']+stats['FGA.8']
    stats['FG%_Tot'] = stats['FG_PCT']+stats['FG_PCT.1']+stats['FG_PCT.2']+stats['FG_PCT.3']+stats['FG_PCT.4']+stats['FG_PCT.5']+stats['FG_PCT.6']+stats['FG_PCT.7']+stats['FG_PCT.8']
    
    if feat == 'FGM':
        ff = 3
        ffstr = 'FGM_Tot'
    elif feat == 'FGA':
        ff = 4
        ffstr = 'FGA_Tot'
    elif feat == 'FG%':
        ff = 5
        ffstr = 'FG%_Tot'

    # Find the row for the input player 
    player_name1 = stats.loc[stats['PLAYER_NAME'] == player1]
    player_name2 = stats.loc[stats['PLAYER_NAME'] == player2]
    player_name3 = stats.loc[stats['PLAYER_NAME'] == player3]
    player_name4 = stats.loc[stats['PLAYER_NAME'] == player4]
    player_name5 = stats.loc[stats['PLAYER_NAME'] == player5]
    
    # Find the Frequency of shots at each distance for the whole seasons average
    league_avg = stats.loc[stats['PLAYER_NAME'] == 'League Average']
    freq_league_avg = []
    for i in range(ff,len(list(league_avg.columns)),3):
        freq_league_avg.append(int(league_avg[list(stats.columns)[i]]/league_avg[ffstr]*100))
    del(freq_league_avg[-1])
    
    
    # Find the Frequency of shots at each distance for the input player
    freq_player1 = []
    for i in range(ff,len(list(player_name1.columns)),3):
            freq_player1.append(int(player_name1[list(stats.columns)[i]]/player_name1[ffstr]*100))
    del(freq_player1[-1])
    
    freq_player2 = []
    for i in range(ff,len(list(player_name2.columns)),3):
            freq_player2.append(int(player_name2[list(stats.columns)[i]]/player_name2[ffstr]*100))
    del(freq_player2[-1])
    
    freq_player3 = []
    for i in range(ff,len(list(player_name3.columns)),3):
            freq_player3.append(int(player_name3[list(stats.columns)[i]]/player_name3[ffstr]*100))
    del(freq_player3[-1])
    
    freq_player4 = []
    for i in range(ff,len(list(player_name4.columns)),3):
            freq_player4.append(int(player_name4[list(stats.columns)[i]]/player_name4[ffstr]*100))
    del(freq_player4[-1])
    
    freq_player5 = []
    for i in range(ff,len(list(player_name5.columns)),3):
            freq_player5.append(int(player_name5[list(stats.columns)[i]]/player_name5[ffstr]*100))
    del(freq_player5[-1])
    
    # Format Data to plot
    distances = ['Less Than 5 ft.', '5-9 ft.', '10-14 ft.', '15-19 ft.', '20-24 ft.', '25-29 ft.', '30-34 ft.', '35-39 ft.', '40+ ft.']
    plot = pd.DataFrame(np.array([freq_league_avg,freq_player1,freq_player2,freq_player3,freq_player4,freq_player5]),
                           columns=distances,
                           index = ['League Average', player1, player2, player3, player4, player5] )
    to_plot = plot.T
    
    
    
    # Plot Data
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot['League Average'], name = 'League Average',
                             line = dict(color='royalblue', width=4, dash='dashdot')))
    
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot[player1], name = player1,
                             line = dict(color='firebrick', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot[player2], name = player2,
                             line = dict(color='seagreen', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot[player3], name = player3,
                             line = dict(color='orange', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot[player4], name = player4,
                             line = dict(color='black', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot[player5], name = player5,
                             line = dict(color='plum', width=4, dash='dashdot')))
    
    max_val = max(max(to_plot[player1]),max(to_plot[player2]),max(to_plot[player3]),max(to_plot[player4]),max(to_plot[player5]),max(to_plot['League Average']))+1
    
    fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=4,
            y0=-1,
            x1=4,
            y1=max_val,
            
            line=dict(
                color="rgb(150,150,150)",
                width=3,
                dash='dash'
            )
        ))
    
    fig.add_trace(go.Scatter(
    x=[list(to_plot.index)[4]],
    y=[max_val],
    text=['  3 Point  Distance'],
    mode="text",
    name = '3 Point Distance',
    showlegend=False
    ))
    
    fig.update_layout(title = 'Frequency of '+feat,
                      xaxis_title = 'Distances',
                      yaxis_title = 'Frequency %')
    
    fig.show()
    
    return