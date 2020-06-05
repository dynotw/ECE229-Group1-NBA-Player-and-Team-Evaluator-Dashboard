import pandas as pd
import numpy as np

def playerStats(stats):
    '''
    This function process the input dataframe and only keeps the colums that is required
    
    Input- 
    stats: input dataframe
    
    Output-
    processed dataframe
    '''
    
    assert isinstance(stats, pd.DataFrame) 

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
        
    return player_average

def teamStats(stats):
    '''
    This function process the input dataframe and only keeps the colums that is required
    
    Input- 
    stats: input dataframe
    
    Output-
    processed dataframe
    '''
    
    assert isinstance(stats, pd.DataFrame) 
    
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
        
    return team_average

def dataproc_bmiper():
    '''

    '''

    player_data_df = pd.read_csv('player_data.csv')
    season_stats_df = pd.read_csv('Seasons_Stats.csv', index_col=0)

    # preprocessing the data
    player_data_df = pd.read_csv('player_data.csv')
    player_data_df.height.fillna("0-0", inplace=True)
    player_data_df.weight.fillna(0, inplace=True)
    player_data_df = player_data_df.assign(height_metric=player_data_df.height.str[:1].astype(int) * 30.48 + player_data_df.height.str[2:].astype(int) * 30.48 / 12)
    player_data_df = player_data_df.assign(weight_metric=player_data_df.weight * 0.453592)
    season_stats_df = season_stats_df[(season_stats_df.MP > 1000) & (season_stats_df.Year > 2000)]

    # Drop players partial seasons 
    for temp_tuple in season_stats_df[season_stats_df.Tm == 'TOT'].itertuples():
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
    season_stats_df.GS = season_stats_df.GS.fillna(0)
    season_stats_df['3P%'] = season_stats_df['3P%'].fillna(0)
    season_stats_df = season_stats_df.assign(pos_simple=season_stats_df.Pos.str[:2])
    season_stats_df.position = season_stats_df.pos_simple.str.replace('-', '')
    season_stats_df = season_stats_df.drop(['blanl', 'blank2'], axis=1)
    season_stats_df = season_stats_df.reset_index(drop=True)
    season_stats_df.to_csv('seasons_stats_procecced.csv')
    
    return