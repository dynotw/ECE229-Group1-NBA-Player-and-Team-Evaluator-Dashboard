import numpy as np
import pandas as pd
import math

import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go

cf.go_offline() # required to use plotly offline (no account required).
py.init_notebook_mode() # graphs charts inline (IPython).

import test_DataProcessing as tdp
import test_WinPredict as twp
# import WinPredict as WP

def test_radar_player():
    '''
    This function plots the radar plot for players based on the  selected season and 5 players and 6 attributes
    
    Inputs- 
    season: Selected Season 
    name1-5: Player 1-5
    att1-6: Atrributes 1-6
    
    Output- 
    Radar plot for players
    '''

    # 1.Retrieve the correct .csv File first
    stats = pd.read_csv("2019-20.csv")
    assert isinstance(stats, pd.DataFrame)
    assert not stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM'and'PLAYER') in stats

    # 2.Process Data from  .csv file and only maintain columns you need 
    player_average = tdp.test_playerStats()
    assert isinstance(player_average, pd.DataFrame)
    assert not player_average is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG%'and'FTM'and'FTA'and'FT%'and'OREB'and 'DREB') in player_average

    names = ['James Harden','Jayson Tatum','Trae Young','Anthony Davis','Ben Simmons']
    atributes = ['PTS','AST','REB','STL','BLK','TOV']
    assert isinstance(names, list)
    assert len(names) == 5
    assert isinstance(atributes, list)
    assert len(atributes) == 6
        
    # 3.Set up and extract data to be ploted - each row at a time (for each player)
    labels=np.array(atributes)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(atributes)
    
    player_stats = np.zeros((len(names),len(labels)))
    for i in range(len(names)):
        player_stats[i] = [player_average[labels[0]][names[i]],player_average[labels[1]][names[i]],
                           player_average[labels[2]][names[i]],player_average[labels[3]][names[i]],
                           player_average[labels[4]][names[i]],player_average[labels[5]][names[i]]]
        
    
    assert isinstance(player_stats, np.ndarray)
    assert np.shape(player_stats) == (len(names),len(labels))
    
    # 4.Loop the data around to be able to compatibale with radar plots
    player_stats_mod = np.zeros((len(names),len(labels)+1))
    for i in range(len(names)):
        player_stats_mod[i] = np.concatenate((player_stats[i],[player_stats[i][0]]))
    labels_mod = np.concatenate((labels,[labels[0]]))
    
    assert isinstance(player_stats_mod, np.ndarray)
    assert np.shape(player_stats_mod) == (len(names),(len(labels)+1))
    
    assert isinstance(labels_mod, np.ndarray)
    assert len(labels_mod) == len(labels)+1
        
    # Plot the data
    fig = go.Figure()
    
    for i in range(len(names)):
        fig.add_trace(go.Scatterpolar(r=player_stats_mod[i],theta=labels_mod,name=names[i]))

    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 1])),showlegend=True)

    fig.show()
        
    return
    
def test_radar_team():
    '''
    This function plots the radar plot for teams based on the selected season and 5 teams and 6 attributes
        
    Inputs- 
    season: Selected Season 
    name1-5: Teams 1-5
    att1-6: Atrributes 1-6
    teamA: the team for which you want to predict the win % 
    teamB: the team against which you want to predict the win % 
        
    Output- 
    Radar plot for teams
    '''
#     season,name1,name2,name3,name4,name5,att1,att2,att3,att4,att5,att6,teamA,teamB
    
    # 1.Retrieve the correct .csv File first
    stats = pd.read_csv("Team_2019-20.csv")
    assert isinstance(stats, pd.DataFrame)
    assert not stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM_NAME'and'W'and'W_PCT' and'L'and'BLKA') in stats
    
    # 2.Process Data from  .csv file and only maintain columns you need 
    team_average = tdp.test_teamStats()
    assert isinstance(team_average, pd.DataFrame)
    assert not team_average is None
    assert ('Win%'and'PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG%'and'FTM'and'FTA'and'FT%'and'OREB'and 'DREB') in team_average
    
    names = ['Boston Celtics', 'Houston Rockets', 'Atlanta Hawks', 'Toronto Raptors', 'Los Angeles Lakers']
    atributes = ['PTS','AST','REB','STL','BLK','TOV']
    assert isinstance(names, list)
    assert len(names) == 5
    assert isinstance(atributes, list)
    assert len(atributes) == 6
    
    # 3.Set up and extract data to be ploted - each row at a time (for each player)
    labels=np.array(atributes)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(atributes)
    
    team_stats = np.zeros((len(names),len(labels)))
    for i in range(len(names)):
        team_stats[i] = [team_average[labels[0]][names[i]],team_average[labels[1]][names[i]],
                         team_average[labels[2]][names[i]],team_average[labels[3]][names[i]],
                         team_average[labels[4]][names[i]],team_average[labels[5]][names[i]]]
    
    assert isinstance(team_stats, np.ndarray)
    assert np.shape(team_stats) == (len(names),len(labels))
    
    
    # 4.Loop the data around to be able to compatibale with radar plots
    team_stats_mod = np.zeros((len(names),len(labels)+1))
    for i in range(len(names)):
        team_stats_mod[i] = np.concatenate((team_stats[i],[team_stats[i][0]]))
        
    assert isinstance(team_stats_mod, np.ndarray)
    assert np.shape(team_stats_mod) == (len(names),(len(labels)+1))
        
    ###########################################
    ###########################################
    ###########################################
    
    arealist = [twp.test_TrangleArea() for li in team_stats_mod]
    assert isinstance(arealist, list)
    assert len(arealist) == len(team_stats_mod)
    
    teamID = twp.test_nametolist()
    assert isinstance(teamID, list)
    assert len(arealist) == len(names)
    
    wincomp = twp.test_teamComp1()
    assert isinstance(wincomp, float)
    
    print("Team A has a" , str(round(wincomp*100 , 2)) , "% chance to win over Team B")
    
    # print names + area pair
    TheAreapair = [a + ", Area under team radar = " + str(round(b, 3)) for a, b in zip(names, arealist)]
    assert isinstance(teamID, list)
    assert len(arealist) == len(team_stats_mod)
    
    ###########################################
    ###########################################
    ###########################################
    
    labels_mod = np.concatenate((labels,[labels[0]]))
    assert isinstance(labels_mod, np.ndarray)
    assert len(labels_mod) == len(labels)+1
                
    # Plot the data
    fig = go.Figure()
   
    for i in range(len(names)):
        fig.add_trace(go.Scatterpolar(r=team_stats_mod[i],theta=labels_mod,name=TheAreapair[i]))
        
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 1])),showlegend=True)
     
    fig.show()
    
    return