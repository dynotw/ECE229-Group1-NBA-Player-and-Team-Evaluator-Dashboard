import numpy as np
import pandas as pd
import math

def test_teamComp1():
    '''
    Very simple placeholder for calculating the winning rates for two team comparison
    
    Inputs- 
    team1: int, teamID for team 1
    team2: int. teamID for team 2
    Team_Stats: the panda DataFrame with all the data.
    
    Outputs-
    float winning percentage in decimal.
    '''
#     team1, team2, Team_Stats
    
    Team_Stats = pd.read_csv("Team_2019-20.csv")
    assert isinstance(Team_Stats, pd.DataFrame)
    assert not Team_Stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM_NAME'and'W'and'W_PCT' and'L'and'BLKA') in Team_Stats
    
    W_PCT = Team_Stats["W_PCT"].tolist()
    assert isinstance(W_PCT, list)
    assert len(W_PCT) == len(Team_Stats)
    
    return (W_PCT[1])/(W_PCT[1] + W_PCT[2])

def test_TrangleArea():
    '''
    Calculate the area of a polygon
    
    Inputs- 
    li: the length data for each dimentions as list. e.g. [1 2 3 4 1 4]
    
    Outputs-
    float
    '''
    
    li = [1, 2, 3, 4, 1, 4]
    assert isinstance(li, list)
    
    li = list(li)
    li.append(li[0])
 
    ret = 0
    for i in range(len(li)-1):
        A = li[i]
        B = li[i+1]
        ret += math.sin(math.pi/3)*A*B/2
       
    assert isinstance(ret, float)
    
    return ret

def test_nametolist():
    '''
    Inputs- 
    names: the list of team names, e.g. names = ['Boston Celtics', 'Houston Rockets', 'Atlanta Hawks', 'Toronto Raptors', 'Los Angeles Lakers']
    Team_Stats: the panda DataFrame with all the data.
    
    Outputs-
    the ID for each team with orders for further calculations.
    '''
    
    names = ['Boston Celtics', 'Houston Rockets', 'Atlanta Hawks', 'Toronto Raptors', 'Los Angeles Lakers']
    assert isinstance(names, list)
    assert len(names) == 5
    
    Team_Stats = pd.read_csv("Team_2019-20.csv")
    assert isinstance(Team_Stats, pd.DataFrame)
    assert not Team_Stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM_NAME'and'W'and'W_PCT' and'L'and'BLKA') in Team_Stats
    
    li = []
    for each in names:
        li.append(Team_Stats["TEAM_NAME"].tolist().index(each))  
    
    assert isinstance(li, list)
    assert len(li) == len(names)
        
    return li