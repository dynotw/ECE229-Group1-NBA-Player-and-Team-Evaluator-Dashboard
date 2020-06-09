import pandas as pd
import numpy as np
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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



def test_dataproc_bmiper():
    '''
    This function pre-processes the dataset for bmiper.py 

    Input - 
        NBA players attributes dataset
        
    Ouput -
        Processed NBA players attributes dataset for further used in bmiper.py
    '''

    player_data_df = pd.read_csv('player_data.csv')
    assert isinstance(player_data_df, pd.DataFrame)
    season_stats_df = pd.read_csv('Seasons_Stats.csv', index_col=0)
    assert isinstance(season_stats_df, pd.DataFrame)

    # preprocessing the data
    player_data_df.height.fillna("0-0", inplace=True)
    player_data_df.weight.fillna(0, inplace=True)
    player_data_df = player_data_df.assign(height_metric=player_data_df.height.str[:1].astype(int) * 30.48 + player_data_df.height.str[2:].astype(int) * 30.48 / 12)
    player_data_df = player_data_df.assign(weight_metric=player_data_df.weight * 0.453592)

    season_stats_df = season_stats_df[(season_stats_df['MP'] > 1000) & (season_stats_df['Year'] > 2000)] #we only interested in the data after season 2000

    # Drop players partial seasons 
    for temp_tuple in season_stats_df[season_stats_df['Tm'] == 'TOT'].itertuples():
        part_seasons = season_stats_df[
            (season_stats_df.Player == temp_tuple.Player) & (season_stats_df.Year == temp_tuple.Year) & (season_stats_df.Tm != 'TOT')
        ]
        if len(part_seasons) > 0:
            logger.info(f'Deleting {len(part_seasons)} partial seasons for {temp_tuple.Player} in {temp_tuple.Year}')
            season_stats_df = season_stats_df.drop(part_seasons.index)

    # Assign height and weight data
    season_stats_df = season_stats_df.assign(height=0)
    season_stats_df = season_stats_df.assign(weight=0)

    for itertup in season_stats_df.itertuples():
        pname = itertup.Player
        if pname[-1] == '*':
            pname = pname[:-1]
        player_data = player_data_df[player_data_df.name == pname]
        if len(player_data) > 0:
            season_stats_df.loc[itertup.Index, 'height'] = player_data.height_metric.values[0]
            season_stats_df.loc[itertup.Index, 'weight'] = player_data.weight_metric.values[0]
        else:
            player_data = player_data_df[
                (player_data_df.name.str.startswith(pname))
                & (player_data_df.year_start <= itertup.Year)
                & (player_data_df.year_end >= itertup.Year)
            ]
            if len(player_data) > 1:
                logger.warning(f'MULTIPLE NAMES FOUND STARTING WITH {pname}')
            logger.info(f'Populating player data for {pname} in {itertup.Year} with {player_data.name}')
            season_stats_df.loc[itertup.Index, 'height'] = player_data.height_metric.values[0]
            season_stats_df.loc[itertup.Index, 'weight'] = player_data.weight_metric.values[0]

    # Clean up the rest of the data & reset the index
    season_stats_df['GS'] = season_stats_df.GS.fillna(0)
    season_stats_df['3P%'] = season_stats_df['3P%'].fillna(0)
    season_stats_df = season_stats_df.assign(pos_simple=season_stats_df.Pos.str[:2])
    season_stats_df['Position'] = season_stats_df.pos_simple.str.replace('-', '')
    season_stats_df = season_stats_df.drop(['blanl', 'blank2'], axis=1)
    season_stats_df = season_stats_df.reset_index(drop=True)
    season_stats_df.to_csv('seasons_stats_procecced_tmp.csv')


    proc_stats_df = pd.read_csv('seasons_stats_procecced_tmp.csv', index_col=0)
    assert isinstance(proc_stats_df, pd.DataFrame)
    proc_stats_df = proc_stats_df.assign(bmi=proc_stats_df.weight / ((proc_stats_df.height/100) ** 2)) # BMI defination

    #Value Added = ([Minutes * (PER - PRL)] / 67). PRL (Position Replacement Level) = 11.5 for power forwards, 
    #11.0 for point guards, 10.6 for centers, 10.5 for shooting guards and small forwards
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PF', 'PRL'] = 11.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PG', 'PRL'] = 11.0
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'C', 'PRL'] = 10.6
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SG', 'PRL'] = 10.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SF', 'PRL'] = 10.5 
    proc_stats_df = proc_stats_df.assign(value_added = ((proc_stats_df.MP * (proc_stats_df.PER -proc_stats_df.PRL))/67)*proc_stats_df.PRL) #assign value added attribute in our dataset
    proc_stats_df = proc_stats_df.rename({'height':'Height', 'bmi':'BMI', 'value_added':'Value Added'}, axis='columns')
    assert ('weight'and'Height'and'Player'and'FG%'and'Year'and'pos_simple'and'MP'and'PER'and'BMI'and'Value Added') in proc_stats_df


    return  proc_stats_df.to_csv('seasons_stats_procecced.csv')