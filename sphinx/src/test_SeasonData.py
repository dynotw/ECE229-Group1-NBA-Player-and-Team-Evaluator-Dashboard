import pandas as pd
import plotly.graph_objects as go


def test_highlight_col():
        '''
        tests adding highlight color to pd.DataFrame
        '''

        season_stats = pd.read_csv("2019-20.csv")
        assert isinstance(season_stats,pd.DataFrame)
        assert not season_stats is None

        season_stats = season_stats.drop(['Unnamed: 0'], axis=1)

        x = season_stats

        r = 'background-color: red'
        y = 'background-color: green'
        g = 'background-color: grey'
        df1 = pd.DataFrame('', index=x.index, columns=x.columns)
        df1.iloc[:, 2] = y
        df1.iloc[:, 3] = r
        df1.iloc[:, 4] = g

        return df1


def test_show_latest_cases():
        '''
        tests showing the latest player data
        '''
        
        n = 5
        n = int(n)
        assert isinstance(n,int)

        season_stats = pd.read_csv("2019-20.csv")
        assert isinstance(season_stats,pd.DataFrame)
        assert not season_stats is None

        season_stats = season_stats.drop(['Unnamed: 0'], axis=1)

        season_stats = season_stats.reindex(
            columns=['PLAYER_ID', 'RANK', 'PLAYER', 'TEAM', 'PTS', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A',
                     'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF'])

        assert isinstance(season_stats,pd.DataFrame)

        return season_stats.head(n).style.apply(test_highlight_col())

