import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

import plotly.express as px

import test_DataProcessing as tdp

def test_best_player_features():
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
#     season == 2019, label == 'PTS', top = 6

    stats = pd.read_csv("2019-20.csv")
    assert isinstance(stats, pd.DataFrame)
    assert not stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM'and'PLAYER') in stats
    
    player_average = tdp.test_playerStats()
    assert isinstance(player_average, pd.DataFrame)
    assert not player_average is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG%'and'FTM'and'FTA'and'FT%'and'OREB'and 'DREB') in player_average
    
    features = ['PTS','AST','REB','STL','BLK','TOV','FGM','FGA','FG%','FTM','FTA','FT%','OREB','DREB']
    features.remove('PTS')
    assert isinstance(features, list)
    assert len(features) == 13
    
    X = player_average[features].to_numpy()
    y = player_average['PTS'].to_numpy()
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    
    reg = LinearRegression().fit(X,y)
    feature_weight = {feature:weight for feature, weight in zip(features, reg.coef_)}
    feature_weight = sorted(feature_weight.items(), key=lambda d:d[1], reverse=True)
    
    top_features = [feature for feature, _ in feature_weight[:6]]
    top_features_weight = [1/(1+np.exp(-weight)) for _, weight in feature_weight[:6]]
    assert isinstance(top_features, list)
    assert isinstance(top_features_weight, list)
    
    x = np.arange(6)
    assert isinstance(x, np.ndarray)
    
    feat_weights = pd.DataFrame({'Attribute': top_features, 'Weight': top_features_weight})
    assert isinstance(feat_weights, pd.DataFrame)
    assert not feat_weights is None
    
    fig = px.bar(feat_weights, x='Attribute', y='Weight', 
                 title='Weights of the top '+str(6)+' attributes that contribute towards PTS')
    fig.show()
    
    return


def test_best_team_features():
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

    
    stats = pd.read_csv("Team_2019-20.csv")
    assert isinstance(stats, pd.DataFrame)
    assert not stats is None
    assert ('PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG_PCT'and'FTM'and'FTA'and'FT_PCT'and'OREB'and 'DREB'and'GP'and'TEAM_NAME'and'W'and'W_PCT' and'L'and'BLKA') in stats

    team_average = tdp.test_teamStats()
    assert isinstance(team_average, pd.DataFrame)
    assert not team_average is None
    assert ('Win%'and'PTS' and 'AST' and 'REB' and 'STL' and 'BLK'and'TOV'and'FGM'and'FGA'and'FG%'and'FTM'and'FTA'and'FT%'and'OREB'and 'DREB') in team_average
    
    features = ['Win%','PTS','AST','REB','STL','BLK','TOV','FGM','FGA','FG%','FTM','FTA','FT%','OREB','DREB']
    features.remove('Win%')
    assert isinstance(features, list)
    assert len(features) == 14
    
    X = team_average[features].to_numpy()
    y = team_average['Win%'].to_numpy()
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    
    reg = LinearRegression().fit(X,y)
    feature_weight = {feature:weight for feature, weight in zip(features, reg.coef_)}
    feature_weight = sorted(feature_weight.items(), key=lambda d:d[1], reverse=True)

    top_features = [feature for feature, _ in feature_weight[:6]]
    top_features_weight = [1/(1+np.exp(-weight)) for _, weight in feature_weight[:6]]
    assert isinstance(top_features, list)
    assert isinstance(top_features_weight, list)
    
    x = np.arange(6)
    assert isinstance(x, np.ndarray)
    
    feat_weights = pd.DataFrame({'Attribute': top_features, 'Weight': top_features_weight})
    assert isinstance(feat_weights, pd.DataFrame)
    assert not feat_weights is None
    
    fig = px.bar(feat_weights, x='Attribute', y='Weight', 
                 title='Weights of the top '+str(6)+' attributes that contribute towards Win%')
    fig.show()

    return 
