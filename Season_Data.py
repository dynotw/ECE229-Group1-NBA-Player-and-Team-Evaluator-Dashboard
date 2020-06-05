import pandas as pd
import plotly.graph_objects as go

fig = go.FigureWidget(layout=go.Layout())

def highlight_col(x):
    r = 'background-color: red'
    y = 'background-color: green'
    g = 'background-color: grey'
    df1 = pd.DataFrame('', index=x.index, columns=x.columns)
    df1.iloc[:, 2] = y
    df1.iloc[:, 3] = r
    df1.iloc[:, 4] = g

    return df1


def show_latest_cases(n, season):
    n = int(n)
    season_stats = pd.read_csv(str(season) + '-' + str(season % 1000 + 1) + ".csv")

    season_stats = season_stats.drop(['Unnamed: 0'], axis=1)

    season_stats = season_stats.reindex(
        columns=['PLAYER_ID', 'RANK', 'PLAYER', 'TEAM', 'PTS', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A',
                 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF'])
    return season_stats.head(n).style.apply(highlight_col, axis=None)