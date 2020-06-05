import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

cf.go_offline() # required to use plotly offline (no account required).
py.init_notebook_mode() # graphs charts inline (IPython).

import DataProcessing as dp

def best_player_features(season=2019, label='PTS', top=6):
    '''
    This function returns the plot for the top k attributes that contribute the most to the chosen y value using 
    linear reggression. This is based on player data
    
    Input- 
    season: the season for which you want to plot the data for 
    label: the y-value (main attribute) that you want to find the top k atrributes for
    top: the number of k attributes
    
    Output- 
    Bar plot of the top k choosen atrributes and their weights for the players data set
    '''
    
    assert isinstance(season, int) 
    assert isinstance(label, str)
    assert isinstance(top, int)
    
    stats = pd.read_csv(str(season)+'-'+ str(season%1000+1)[-2:]+ ".csv")

    player_average = dp.playerStats(stats)
    
    features = ['PTS','AST','REB','STL','BLK','TOV','FGM','FGA','FG%','FTM','FTA','FT%','OREB','DREB']
    features.remove(label)
    
    X = player_average[features].to_numpy()
    y = player_average[label].to_numpy()
    reg = LinearRegression().fit(X,y)
    feature_weight = {feature:weight for feature, weight in zip(features, reg.coef_)}
    feature_weight = sorted(feature_weight.items(), key=lambda d:d[1], reverse=True)
    top_features = [feature for feature, _ in feature_weight[:top]]
    top_features_weight = [1/(1+np.exp(-weight)) for _, weight in feature_weight[:top]]
    
    x = np.arange(top)
    feat_weights = pd.DataFrame({'Attribute': top_features, 'Weight': top_features_weight})
    
    fig = px.bar(feat_weights, x='Attribute', y='Weight', 
                 title='Weights of the top '+str(top)+' attributes that contribute towards '+label)
    fig.show()
    
    return

def best_team_features(season=2019, label='Win%', top=6):
    '''
    This function returns the plot for the top k attributes that contribute the most to the chosen y value using 
    linear reggression. This is based on team data
    
    Input- 
    season: the season for which you want to plot the data for 
    label: the y-value (main attribute) that you want to find the top k atrributes for
    top: the number of k attributes
    
    Output- 
    Bar plot of the top k choosen atrributes and their weights for the teams data set
    '''
    
    assert isinstance(season, int) 
    assert isinstance(label, str)
    assert isinstance(top, int)
    
    stats = pd.read_csv('Team_'+str(season)+'-'+ str(season%1000+1)+ ".csv")

    team_average = dp.teamStats(stats)
    
    features = ['Win%','PTS','AST','REB','STL','BLK','TOV','FGM','FGA','FG%','FTM','FTA','FT%','OREB','DREB']
    features.remove(label)
    
    X = team_average[features].to_numpy()
    y = team_average[label].to_numpy()
    reg = LinearRegression().fit(X,y)
    feature_weight = {feature:weight for feature, weight in zip(features, reg.coef_)}
    feature_weight = sorted(feature_weight.items(), key=lambda d:d[1], reverse=True)
    top_features = [feature for feature, _ in feature_weight[:top]]
    top_features_weight = [1/(1+np.exp(-weight)) for _, weight in feature_weight[:top]]
    
    x = np.arange(top)
    feat_weights = pd.DataFrame({'Attribute': top_features, 'Weight': top_features_weight})
    
    fig = px.bar(feat_weights, x='Attribute', y='Weight', 
                 title='Weights of the top '+str(top)+' attributes that contribute towards '+label)
    fig.show()

    return 