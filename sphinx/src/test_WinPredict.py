import numpy as np
import pandas as pd
import math

def test_teamComp1():
    '''
    tests calculating the winning rates for two team comparison
    
    :return: winning percentage in decimal
    :rtype: float
    '''
    # team1, team2, Team_Stats
    
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
    tests calculating the area of a polygon
    
    :return: area of the polygon
    :rtype: float
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
    tests creating a list of indices based on team names

    :return: list of indices of teams
    :rtype: list
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