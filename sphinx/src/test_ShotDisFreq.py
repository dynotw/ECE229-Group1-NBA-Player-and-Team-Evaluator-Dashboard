import numpy as np
import pandas as pd 

import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

cf.go_offline() # required to use plotly offline (no account required).
py.init_notebook_mode() # graphs charts inline (IPython).


def test_shotDis_Freq():
    '''
    tests the shot distance frequency plot
    '''
    
    # season, player1, player2, player3, player4, player5, feat


    stats = pd.read_csv('shotDis_2019-2020.csv')
    stats.fillna(0)
    assert isinstance(stats, pd.DataFrame)
    assert not stats is None
    assert ('FGM' and 'FGM.1' and 'FGM.2' and 'FGM.3' and 'FGM.4'and'FGM.5'and'FGM.6'and'FGM.7'and'FGM.8'and'FGA'and'FGA.1'and'FGA.2'and'FGA.3'and 'FGA.4'and'FGA.5'and'FGA.6'and'FGA.7'and 'FGA.8'and'FG_PCT'and'FG_PCT.1'and'FG_PCT.2'and'FG_PCT.3'and 'FG_PCT.4'and'FG_PCT.5'and'FG_PCT.6'and'FG_PCT.7'and 'FG_PCT.8') in stats
    
    # Add row for league averages 
    avg = {'PLAYER_NAME': 'League Average',
           'TEAM_ABBREVIATION': 'AVG'}
    assert isinstance(avg, dict)
    
    for i in list(stats.columns)[2:]:
        avg[i] = stats[i].mean()
    stats = stats.append(avg, ignore_index=True)
         
    # Find the total FGM, FGA, FG% for all distance 
    stats['FGM_Tot'] = stats['FGM']+stats['FGM.1']+stats['FGM.2']+stats['FGM.3']+stats['FGM.4']+stats['FGM.5']+stats['FGM.6']+stats['FGM.7']+stats['FGM.8']
    stats['FGA_Tot'] = stats['FGA']+stats['FGA.1']+stats['FGA.2']+stats['FGA.3']+stats['FGA.4']+stats['FGA.5']+stats['FGA.6']+stats['FGA.7']+stats['FGA.8']
    stats['FG%_Tot'] = stats['FG_PCT']+stats['FG_PCT.1']+stats['FG_PCT.2']+stats['FG_PCT.3']+stats['FG_PCT.4']+stats['FG_PCT.5']+stats['FG_PCT.6']+stats['FG_PCT.7']+stats['FG_PCT.8']
    
    
    if 'FGM' == 'FGM':
        ff = 3
        ffstr = 'FGM_Tot'
    elif 'FGM' == 'FGA':
        ff = 4
        ffstr = 'FGA_Tot'
    elif 'FGM' == 'FG%':
        ff = 5
        ffstr = 'FG%_Tot'

    # Find the row for the input player 
    player_name1 = stats.loc[stats['PLAYER_NAME'] == 'James Harden']
    player_name2 = stats.loc[stats['PLAYER_NAME'] == 'Chris Paul']
    player_name3 = stats.loc[stats['PLAYER_NAME'] == 'Kemba Walker']
    player_name4 = stats.loc[stats['PLAYER_NAME'] == 'Anthony Davis']
    player_name5 = stats.loc[stats['PLAYER_NAME'] == 'Ben Simmons']
    
    assert isinstance(player_name1, pd.DataFrame)
    assert not player_name1 is None
    assert isinstance(player_name2, pd.DataFrame)
    assert not player_name2 is None
    assert isinstance(player_name3, pd.DataFrame)
    assert not player_name3 is None
    assert isinstance(player_name4, pd.DataFrame)
    assert not player_name4 is None
    assert isinstance(player_name5, pd.DataFrame)
    assert not player_name5 is None
    
    # Find the Frequency of shots at each distance for the whole seasons average
    league_avg = stats.loc[stats['PLAYER_NAME'] == 'League Average']
    assert isinstance(league_avg, pd.DataFrame)
    assert not league_avg is None
    
    freq_league_avg = []
    for i in range(ff,len(list(league_avg.columns)),3):
        freq_league_avg.append(int(league_avg[list(stats.columns)[i]]/league_avg[ffstr]*100))
    del(freq_league_avg[-1])
    assert isinstance(freq_league_avg, list)
    assert len(freq_league_avg) == 9
    
    
    # Find the Frequency of shots at each distance for the input player
    freq_player1 = []
    for i in range(ff,len(list(player_name1.columns)),3):
            freq_player1.append(int(player_name1[list(stats.columns)[i]]/player_name1[ffstr]*100))
    del(freq_player1[-1])
    assert isinstance(freq_player1, list)
    assert len(freq_player1) == 9
    
    freq_player2 = []
    for i in range(ff,len(list(player_name2.columns)),3):
            freq_player2.append(int(player_name2[list(stats.columns)[i]]/player_name2[ffstr]*100))
    del(freq_player2[-1])
    assert isinstance(freq_player2, list)
    assert len(freq_player2) == 9
    
    freq_player3 = []
    for i in range(ff,len(list(player_name3.columns)),3):
            freq_player3.append(int(player_name3[list(stats.columns)[i]]/player_name3[ffstr]*100))
    del(freq_player3[-1])
    assert isinstance(freq_player3, list)
    assert len(freq_player3) == 9
    
    freq_player4 = []
    for i in range(ff,len(list(player_name4.columns)),3):
            freq_player4.append(int(player_name4[list(stats.columns)[i]]/player_name4[ffstr]*100))
    del(freq_player4[-1])
    assert isinstance(freq_player4, list)
    assert len(freq_player4) == 9
    
    freq_player5 = []
    for i in range(ff,len(list(player_name5.columns)),3):
            freq_player5.append(int(player_name5[list(stats.columns)[i]]/player_name5[ffstr]*100))
    del(freq_player5[-1])
    assert isinstance(freq_player5, list)
    assert len(freq_player5) == 9
    
    # Format Data to plot
    distances = ['Less Than 5 ft.', '5-9 ft.', '10-14 ft.', '15-19 ft.', '20-24 ft.', '25-29 ft.', '30-34 ft.', '35-39 ft.', '40+ ft.']
    assert isinstance(distances, list)
    assert len(distances) == 9
    
    plot = pd.DataFrame(np.array([freq_league_avg,freq_player1,freq_player2,freq_player3,freq_player4,freq_player5]),
                           columns=distances,
                           index = ['League Average', 'James Harden','Chris Paul','Kemba Walker','Anthony Davis','Ben Simmons'])
    assert isinstance(plot, pd.DataFrame)
    assert not plot is None
    assert len(plot) == 6
    assert len(plot.columns) == len(distances)
    
    to_plot = plot.T
    
    # Plot Data
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot['League Average'], name = 'League Average',
                             line = dict(color='royalblue', width=4, dash='dashdot')))
    
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot['James Harden'], name = 'James Harden',
                             line = dict(color='firebrick', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot['Chris Paul'], name = 'Chris Paul',
                             line = dict(color='seagreen', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot['Kemba Walker'], name = 'Kemba Walker',
                             line = dict(color='orange', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot['Anthony Davis'], name = 'Anthony Davis',
                             line = dict(color='black', width=4, dash='dashdot')))
    fig.add_trace(go.Scatter(x=to_plot.index, y=to_plot['Ben Simmons'], name = 'Ben Simmons',
                             line = dict(color='plum', width=4, dash='dashdot')))
    
    max_val = max(max(to_plot['James Harden']),max(to_plot['Chris Paul']),max(to_plot['Kemba Walker']),max(to_plot['Anthony Davis']),max(to_plot['Ben Simmons']),max(to_plot['League Average']))+1
    
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
    
    fig.update_layout(title = 'Frequency of FGM',
                      xaxis_title = 'Distances',
                      yaxis_title = 'Frequency %')
    
    fig.show()
    
    return