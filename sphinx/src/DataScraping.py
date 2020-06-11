import requests
import json
import pandas as pd
import numpy as np

def get_player_data(sea, cat):
    '''
    Creates a Pandas Dataframe of the stats for a given season and category.
    For example, sea = '2019-2020' and cat = 'AST', will get the amount
    of assists for players in the 2019-2020 season sorted by mosts assists.
    
    :param sea: The NBA Regular Season for which you want to retrive data
    :type sea: string

    :param cat: The Category for which you want the Pandas data frame to be order in
    :type cat: string
         
    :return: A Pandas DataFrame of the stats in respect to the above mentioned criteria
    :rtype: pd.DataFrame
    '''
    
    assert isinstance(sea, str)
    assert isinstance(cat, str)
    
    # Url for the API which is used to retrived by examining the files (json objects) 
    # in the network requests of the website
    url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season='+sea+'&SeasonType=Regular+Season&StatCategory='+cat+''
    print(url)
    
    headers = {
            'Host': 'stats.nba.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://stats.nba.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'x-nba-stats-origin': 'stats',
            'x-nba-stats-token': 'true'
                  }
    
    response = requests.get(url=url, headers=headers)
    
    # Column names for the dataframe
    headers = response.json()['resultSet']['headers']
    # Actual Data
    player_ranking = response.json()['resultSet']['rowSet']
    
    # Create Data frame
    cols = headers
    df_sea_cat = pd.DataFrame(player_ranking,columns = cols)
    
    return df_sea_cat

def get_team_data(sea):
    '''
    Creates a Pandas Dataframe of the stats for a given season and category.
    For example, sea = '2019-2020' and cat = 'AST', will get the amount
    of assists for players in the 2019-2020 season sorted by mosts assists.
    
    :param sea: The NBA Regular Season for which you want to retrive data
    :type sea: string
    
    :return: A Pandas DataFrame of the stats in respect to the above mentioned criteria
    :rtype: pd.DataFrame
    '''
    
    assert isinstance(sea, str)
    assert isinstance(cat, str)
    
    # Url for the API which is used to retrived by examining the files (json objects) 
    # in the network requests of the website
    url = "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season="+sea+"&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="
    print(url)

    headers = {
            'Host': 'stats.nba.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://stats.nba.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'x-nba-stats-origin': 'stats',
            'x-nba-stats-token': 'true'
                  }

    response = requests.get(url=url, headers=headers)

    # Column names for the dataframe
    headers = response.json()['resultSets'][0]['headers']
    # Actual Data
    team_ranking = response.json()['resultSets'][0]['rowSet']
    
    # Create Data frame
    cols = headers
    df_sea = pd.DataFrame(team_ranking,columns = cols)
    
    return df_sea


def shot_ranges(sea):
    '''
    Given a season (ex. 2019-2020), this will return a DataFrame of the
    players shot statistics from different ranges on the basketball court. 

    :param sea: The NBA Regular Season for which you want to retrieve data. (ex. '2019-2020')
    :type sea: string
    
    :return: A Pandas DataFrame of the shot statistics from different distances.
    :rtype: pd.DataFrame
    '''
    
    assert isinstance(sea, str)
    
    # Url for the API which is used to retrived by examining the files (json objects) 
    # in the network requests of the website
    url = "https://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=&DistanceRange=5ft+Range&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season="+sea+"&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
    headers = {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
              }
    
    resp_json = requests.get(url=url, headers=headers).json()
    
    # Column Headers for different shot ranges 
    range_cols = resp_json['resultSets']['headers'][0]['columnNames'] 
    range_cols = ['PLAYER_INFO'] + range_cols
    
    # Column names of attributes namely (FGM, FGA, FG_PCT) repeated for the different shot distances
    att_cols = resp_json['resultSets']['headers'][1]['columnNames'] 

    print(len(range_cols))
    print(range_cols)
    print(att_cols)
    
    # Actual Raw DATA
    shots_distance_data = resp_json['resultSets']['rowSet']
    
    # Create DataFrame and get rid of 'PLAYER_ID', 'TEAM_ID' columns
    shot_distance_by_season = pd.DataFrame(shots_distance_data, columns = att_cols).drop(['PLAYER_ID', 'TEAM_ID'], axis=1)
    
    return shot_distance_by_season