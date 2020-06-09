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