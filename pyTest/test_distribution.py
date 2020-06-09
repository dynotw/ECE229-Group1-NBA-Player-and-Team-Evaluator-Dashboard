import Atrributes_Distribution as ad
import Season_Data as sd
import pandas as pd
import matplotlib
import seaborn

def test_ad():
    season = 2010
    assert isinstance(season,int)

    stats = pd.read_csv('C:/Users/83414/Downloads/'+ str(season) + '-' + str(season % 1000 + 1) + ".csv")
    assert isinstance(stats,pd.DataFrame)
    assert not stats is None

    plot1 = ad.plot_distribution("GP", stats)
    assert not plot1 is None

    plot2 = ad.plot_bidistribution("GP","MIN",stats)
    assert isinstance(plot2,seaborn.axisgrid.JointGrid)

    plot3 = ad.plot_contour("GP", "MIN", stats)
    assert isinstance(plot3,seaborn.axisgrid.JointGrid)

    plot4 = ad.plot_kdeaverage("GP", stats)
    assert not plot4 is None

def test_season():
    season = 2010
    assert isinstance(season,int)

    stats = pd.read_csv('C:/Users/83414/Downloads/'+ str(season) + '-' + str(season % 1000 + 1) + ".csv")
    assert isinstance(stats,pd.DataFrame)
    assert not stats is None

    season_stats = sd.highlight_col(stats)
    assert isinstance(season_stats, pd.DataFrame)

    season_stats = season_stats.drop(['Unnamed: 0'], axis=1)

    assert isinstance(season_stats,pd.DataFrame)

    season_stats = season_stats.reindex(
        columns=['PLAYER_ID', 'RANK', 'PLAYER', 'TEAM', 'PTS', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A',
                 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF'])

    assert isinstance(season_stats,pd.DataFrame)


