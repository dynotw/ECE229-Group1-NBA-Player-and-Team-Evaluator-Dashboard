import numpy as np
import pandas as pd
import math

import matplotlib.pyplot as plt 

import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

cf.go_offline() # required to use plotly offline (no account required).
py.init_notebook_mode() # graphs charts inline (IPython).

import DataProcessing as dp
import WinPredict as WP

def radar_player(season,name1,name2,name3,name4,name5,att1,att2,att3,att4,att5,att6):
        '''
        This function plots the radar plot for players based on the  selected season and 5 players and 6 attributes
        
        :param season: Selected Season 
        :type season: string

        :param name1-5: Player 1-5
        :type name1-5: string

        :param att1-6: Atrributes 1-6
        :type att1-5: string 
        
        :return: Radar plot for players
        '''

        assert isinstance(season, int) 
        assert isinstance(name1, str) and isinstance(name2, str) and isinstance(name3, str) and isinstance(name4, str) 
        assert isinstance(name5, str)
        assert isinstance(att1, str) and isinstance(att2, str) and isinstance(att3, str) and isinstance(att4, str)
        assert isinstance(att5, str) and isinstance(att6, str)

        # 1.Retrieve the correct .csv File first
        stats = pd.read_csv(str(season)+'-'+ str(season%1000+1)+ ".csv")

        # 2.Process Data from  .csv file and only maintain columns you need 
        player_average = dp.playerStats(stats)

        names = [name1, name2, name3, name4, name5]
        atributes = [att1, att2, att3, att4, att5, att6]

        # 3.Set up and extract data to be ploted - each row at a time (for each player)
        labels=np.array(atributes)
        player_stats = np.zeros((len(names),len(labels)))
        for i in range(len(names)):
            player_stats[i] = [player_average[labels[0]][names[i]],player_average[labels[1]][names[i]],
                                player_average[labels[2]][names[i]],player_average[labels[3]][names[i]],
                                player_average[labels[4]][names[i]],player_average[labels[5]][names[i]]]

        # 4.Loop the data around to be able to compatibale with radar plots
        player_stats_mod = np.zeros((len(names),len(labels)+1))
        for i in range(len(names)):
            player_stats_mod[i] = np.concatenate((player_stats[i],[player_stats[i][0]]))

#         # 5. Set up axis for Plotting
#         angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
#         angles=np.concatenate((angles,[angles[0]]))

#         # 6. Finally plot the radar plot for players
#         fig= plt.figure()
#         ax = fig.add_subplot(111, polar=True)
#         for i in range(len(names)):
#             ax.plot(angles, player_stats_mod[i], linewidth=2)
#             ax.fill(angles, player_stats_mod[i], alpha=0.0)

#         plt.legend(names, loc='lower right', bbox_to_anchor=(1., 0.5, 1., 0.5))   
#         ax.set_thetagrids(angles * 180/np.pi, labels)
#         ax.grid(True)
        
#         plt.show()

        labels_mod = np.concatenate((labels,[labels[0]]))
        
        # Plot the data
        fig = go.Figure()
    
        for i in range(len(names)):
            fig.add_trace(go.Scatterpolar(r=player_stats_mod[i],theta=labels_mod,name=names[i]))

        
        fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 1])),showlegend=True)

        fig.show()
        
        return
    
def radar_team(season,name1,name2,name3,name4,name5,att1,att2,att3,att4,att5,att6,teamA,teamB):
    '''
    This function plots the radar plot for teams based on the selected season and 5 teams and 6 attributes
        
    :param season: Selected Season 
    :type season: string

    :param name1-5: Player 1-5
    :type name1-5: string

    :param att1-6: Atrributes 1-6
    :type att1-5: string

    :param teamA: the team for which you want to predict the win % 
    :type teamA: string

    :param teamB: the team against which you want to predict the win % 
    :type teamB: string
        
    :return: Radar plot for teams
    '''
    
    assert isinstance(season, int) 
    assert isinstance(name1, str) and isinstance(name2, str) and isinstance(name3, str) and isinstance(name4, str) 
    assert isinstance(name5, str)
    assert isinstance(att1, str) and isinstance(att2, str) and isinstance(att3, str) and isinstance(att4, str)
    assert isinstance(att5, str) and isinstance(att6, str)
    assert isinstance(teamA, int) and isinstance(teamB, int)
    
    # 1.Retrieve the correct .csv File first
    stats = pd.read_csv('Team_'+str(season)+'-'+ str(season%1000+1)+ ".csv")
    
    # 2.Process Data from  .csv file and only maintain columns you need 
    team_average = dp.teamStats(stats)
    
    names = [name1, name2, name3, name4, name5]
    atributes = [att1, att2, att3, att4, att5, att6]
    
    # 3.Set up and extract data to be ploted - each row at a time (for each player)
    labels=np.array(atributes)
    team_stats = np.zeros((len(names),len(labels)))
    for i in range(len(names)):
        team_stats[i] = [team_average[labels[0]][names[i]],team_average[labels[1]][names[i]],
                         team_average[labels[2]][names[i]],team_average[labels[3]][names[i]],
                         team_average[labels[4]][names[i]],team_average[labels[5]][names[i]]]

    # 4.Loop the data around to be able to compatibale with radar plots
    team_stats_mod = np.zeros((len(names),len(labels)+1))
    for i in range(len(names)):
        team_stats_mod[i] = np.concatenate((team_stats[i],[team_stats[i][0]]))
    
    ###########################################
    ###########################################
    ###########################################
    
    #print("Area for each:")
    arealist = [WP.TrangleArea(li) for li in team_stats_mod]
    #print(arealist)
    teamID = WP.nametolist(names, stats)
    wincomp = WP.teamComp1(teamID[teamA-1], teamID[teamB-1], stats)
    print("Team A has a" , str(round(wincomp*100 , 2)) , "% chance to win over Team B")
    
    # print names + area pair
    TheAreapair = [a + ", Area under team radar = " + str(round(b, 3)) for a, b in zip(names, arealist)]
    
    ###########################################
    ###########################################
    ###########################################
    
    labels_mod = np.concatenate((labels,[labels[0]]))
                
    # Plot the data
    fig = go.Figure()
   
    for i in range(len(names)):
        fig.add_trace(go.Scatterpolar(r=team_stats_mod[i],theta=labels_mod,name=TheAreapair[i]))
        
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0, 1])),showlegend=True)
     
    fig.show()
    
    return