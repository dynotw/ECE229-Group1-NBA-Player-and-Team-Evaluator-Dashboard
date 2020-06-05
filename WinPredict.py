import numpy as np
import pandas as pd
import math

def teamComp1(team1, team2, Team_Stats):
    '''
    Very simple placeholder for calculating the winning rates for two team comparison
    
    Inputs- 
    team1: int, teamID for team 1
    team2: int. teamID for team 2
    Team_Stats: the panda DataFrame with all the data.
    
    Outputs-
    float winning percentage in decimal.
    '''
    
    W_PCT = Team_Stats["W_PCT"].tolist()
    
    return (W_PCT[team1])/(W_PCT[team1] + W_PCT[team2])

def TrangleArea(li):
    '''
    Calculate the area of a polygon
    
    Inputs- 
    li: the length data for each dimentions as list. e.g. [1 2 3 4 1 4]
    
    Outputs-
    float
    '''
    
    li = list(li)
    li.append(li[0])
    ret = 0
    for i in range(len(li)-1):
        A = li[i]
        B = li[i+1]
        ret += math.sin(math.pi/3)*A*B/2
        
    return ret

def nametolist(names, Team_Stats):
    '''
    Inputs- 
    names: the list of team names, e.g. names = ['Atlanta Hawks', 'Charlotte Bobcats', 'Detroit Pistons', 'Los Angeles Clippers', 'Minnesota Timberwolves']
    Team_Stats: the panda DataFrame with all the data.
    
    Outputs-
    the ID for each team with orders for further calculations.
    '''
    
    li = []
    for each in names:
        li.append(Team_Stats["TEAM_NAME"].tolist().index(each))  
        
    return li