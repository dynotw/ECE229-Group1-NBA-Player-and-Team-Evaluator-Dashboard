import pandas as pd
import numpy as np


def test_playerStats():
    '''
    This function process the input dataframe and only keeps the colums that is required
    
    Input- 
    stats: input dataframe
    
    Output-
    processed dataframe
    '''

    stats = pd.read_csv("2019-20.csv")
    assert isinstance(stats, pd.DataFrame)
    assert not stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM'and'PLAYER') in stats

    player_average = pd.DataFrame()
    for i in range(len(stats)):
        games1 = stats.iloc[i]['GP']
    
        player1 = pd.DataFrame([(stats.iloc[i]['PTS']/stats['PTS'].max(0),stats.iloc[i]['AST']/stats['AST'].max(0),
                                 stats.iloc[i]['REB']/stats['REB'].max(0),stats.iloc[i]['STL']/stats['STL'].max(0),
                                 stats.iloc[i]['BLK']/stats['BLK'].max(0),stats.iloc[i]['TOV']/stats['TOV'].max(0),
                                 stats.iloc[i]['FGM']/stats['FGM'].max(0),stats.iloc[i]['FGA']/stats['FGA'].max(0),
                                stats.iloc[i]['FG_PCT']/stats['FG_PCT'].max(0),  
                                stats.iloc[i]['FTM']/stats['FTM'].max(0), stats.iloc[i]['FTA']/stats['FTA'].max(0), 
                                stats.iloc[i]['FT_PCT']/stats['FT_PCT'].max(0),
                                stats.iloc[i]['OREB']/stats['OREB'].max(0),stats.iloc[i]['DREB']/stats['DREB'].max(0),
                                stats.iloc[i]['GP'], stats.iloc[i]['TEAM'])],
                                columns=['PTS', 'AST','REB','STL','BLK','TOV','FGM','FGA','FG%',
                                         'FTM','FTA','FT%','OREB','DREB','GP','TEAM'],
                                index = [stats.iloc[i]['PLAYER']])
        player_average = pd.concat([player_average,player1])
        
    assert isinstance(player_average, pd.DataFrame)
        
    return player_average


def test_teamStats():
    '''
    This function process the input dataframe and only keeps the colums that is required
    
    Input- 
    stats: input dataframe
    
    Output-
    processed dataframe
    '''
       
    stats = pd.read_csv("Team_2019-20.csv")
    assert isinstance(stats, pd.DataFrame)
    assert not stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM_NAME'and'W'and'W_PCT' and'L'and'BLKA') in stats
    
    team_average = pd.DataFrame()
    for i in range(len(stats)):
        games1 = stats.iloc[i]['GP']
    
        team1 = pd.DataFrame([(stats.iloc[i]['GP'], stats.iloc[i]['W'], stats.iloc[i]['W_PCT'], stats.iloc[i]['L'], 
                               stats.iloc[i]['PTS']/stats['PTS'].max(0), stats.iloc[i]['AST']/stats['AST'].max(0),
                               stats.iloc[i]['REB']/stats['REB'].max(0), stats.iloc[i]['STL']/stats['STL'].max(0),
                               stats.iloc[i]['BLK']/stats['BLK'].max(0), stats.iloc[i]['BLKA']/stats['BLKA'].max(0),
                               stats.iloc[i]['TOV']/stats['TOV'].max(0),
                               stats.iloc[i]['FGM']/stats['FGM'].max(0),stats.iloc[i]['FGA']/stats['FGA'].max(0),
                               stats.iloc[i]['FG_PCT']/stats['FG_PCT'].max(0),
                               stats.iloc[i]['FTM']/stats['FTM'].max(0),stats.iloc[i]['FTA']/stats['FTA'].max(0), 
                               stats.iloc[i]['FT_PCT']/stats['FT_PCT'].max(0), 
                               stats.iloc[i]['OREB']/stats['OREB'].max(0),stats.iloc[i]['DREB']/stats['DREB'].max(0),
                              )],
                               
                              columns=['GP','Wins','Win%','Losses','PTS','AST','REB','STL','BLK','BLK_Attempt',
                                       'TOV','FGM','FGA','FG%','FTM','FTA','FT%','OREB','DREB'],
                               
                            index = [stats.iloc[i]['TEAM_NAME']])
        
        team_average = pd.concat([team_average,team1])
        
    assert isinstance(team_average, pd.DataFrame)
        
    return team_average