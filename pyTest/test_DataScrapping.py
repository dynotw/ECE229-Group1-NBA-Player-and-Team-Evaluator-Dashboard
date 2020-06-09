import requests
import pandas as pd

def player_scrapper():
    '''
    Inputs-
    sea: The NBA Regular Season for which you want to retrive data
    cat: The Category for which you want the Pandas data frame to be order in
         Example;
         cat = AST
         the first row of the dataframe will be the player with the most assist that season

    Outputs-
    A Pandas DataFrame of the stats in respect to the above mentioned criteria
    '''
    # 1st, This part is player data scrapper
    # Url for the API which is used to retrived by examining the files (json objects)
    # in the network requests of the website
    url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2018-19&SeasonType=Regular+Season&StatCategory=PTS'
    # https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2018-19&SeasonType=Regular+Season&StatCategory=PTS
    response = requests.get(url)

    assert (response.status_code) == 400
    assert (response.headers['Content-Type']) == 'application/json; charset=utf-8'

    headers = response.json()['resultSet']['headers']
    # Actual Data
    player_ranking = response.json()['resultSet']['rowSet']
    
    assert isinstance(headers, list)
    assert isinstance(player_ranking, list)

    # Create Data frame
    df_sea_cat = pd.DataFrame(player_ranking,columns = headers)

    assert isinstance(df_sea_cat, pd.DataFrame)
    assert not df_sea_cat is None
    

def team_scrapper():
    # 2nd, This part is for team data scrapper
    url = "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season="+"2018-19"+"&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="
    # https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=

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
    assert (response.status_code) == 200
    
    # Column names for the dataframe
    headers = response.json()['resultSets'][0]['headers']
    # Actual Data
    team_ranking = response.json()['resultSets'][0]['rowSet']
    assert isinstance(headers, list)
    assert isinstance(team_ranking, list)
    
    # Create Data frame
    df_sea = pd.DataFrame(team_ranking,columns = headers)
    
    assert isinstance(df_sea, pd.DataFrame)
    assert not df_sea_cat is None



def shot_ranges_scrapper():
    '''
    Inputs- 
    sea: The NBA Regular Season for which you want to retrive data
    
    Outputs- 
    A Pandas DataFrame of the shots from different distances 
    '''
    
    
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

    assert isinstance(range_cols, list)
    assert isinstance(team_ranking, list)
    
    # Column names of attributes namely (FGM, FGA, FG_PCT) repeated for the different shot distances
    att_cols = resp_json['resultSets']['headers'][1]['columnNames'] 
    assert isinstance(att_cols, list)
    
    # Actual Raw DATA
    shots_distance_data = resp_json['resultSets']['rowSet']
    assert isinstance(shots_distance_data, list)
    
    # Create DataFrame and get rid of 'PLAYER_ID', 'TEAM_ID' columns
    shot_distance_by_season = pd.DataFrame(shots_distance_data, columns = att_cols).drop(['PLAYER_ID', 'TEAM_ID'], axis=1)
    assert isinstance(shot_distance_by_season, pd.DataFrame)
    assert not shot_distance_by_season is None

    return shot_distance_by_season


