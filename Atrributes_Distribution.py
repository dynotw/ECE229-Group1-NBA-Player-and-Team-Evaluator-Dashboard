import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual, Layout, Button, Box, interact_manual



def plot_contour(category1, category2, stats):
    '''
    x is the tag of the dataset
    y is another tag of the dataset
    stats is the name of dataframe
    input: selected tags, dataset
    plot: bivariate contour of the selected tag
    '''
    assert isinstance(category1, str)
    assert isinstance(category2, str)

    #     season_stats = pd.read_csv(str(season)+'-'+ str(season + 1)+ ".csv")
    df = stats

    sns.set(style="darkgrid")
    sns.jointplot(x=category1, y=category2, data=df, kind="kde", height=10)


def plot_distribution(category1, stats):
    '''
    x is the tag of the dataset
    stats is the name of dataframe
    input: selected tag, dataset
    plot: distribution of the selected tag
    '''
    assert isinstance(category1, str)

    #     season_stats = pd.read_csv(str(season)+'-'+ str(season + 1)+ ".csv")
    df = stats
    plt.figure(figsize=(15, 8))
    sns.set(style="darkgrid")
    plt.ylabel('Ratio')
    plt.title('Distribution of %s' % category1)
    sns.distplot(df[category1], bins=10, kde=True, rug=False)


def plot_bidistribution(category1, category2, stats):
    '''
    x is the tag of the dataset
    y is another tag of the dataset
    stats is the name of dataframe
    input: selected tags, dataset
    plot: bivariate distribution of the selected tag
    '''
    assert isinstance(category1, str)
    assert isinstance(category2, str)

    df = stats
    sns.set(style="darkgrid")
    dsf = pd.DataFrame(df, columns=[category1, category2])
    sns.jointplot(x=category1, y=category2, data=dsf, height=10)


def plot_kdeaverage(category1, stats):
    '''
    input: selected tag, stats
    plot: distribution's kde curve of the average value of selected tag
    '''

    sns.set(style="darkgrid")
    y = stats[category1]
    y = y.astype(float)
    plt.figure(figsize=(15, 8))
    plt.ylabel('Probability Density')
    plt.xlabel('%s per game' % category1)
    plt.title('Distribution of %s' % category1)
    sns.distplot(y, bins=10, hist=False, kde=True, rug=False)
    sns.kdeplot(y, shade=True)


def distribution(season, graph):
    season_stats = pd.read_csv(str(season) + '-' + str(season % 1000 + 1) + ".csv")

    if (graph == 1):

        category1_option = widgets.Dropdown(
            options=['GP', 'MIN', 'FGM',
                     'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                     'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'EFF'],
            value='GP',
            description='Category:',
            disabled=False,
        )

        widgets.interact(plot_distribution, category1=category1_option, stats=fixed(season_stats))
        # fixed is to fix arguments, which isn't gotten from this place's interact

    elif (graph == 2):

        category1_option = widgets.Dropdown(
            options=['GP', 'MIN', 'FGM',
                     'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                     'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'EFF'],
            value='GP',
            description='Category:',
            disabled=False,
        )

        category2_option = widgets.Dropdown(
            options=['GP', 'MIN', 'FGM',
                     'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                     'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'EFF'],
            value='MIN',
            description='Category:',
            disabled=False,
        )

        widgets.interact(plot_contour, category1=category1_option, category2=category2_option,
                         stats=fixed(season_stats))

    elif (graph == 3):

        category1_option = widgets.Dropdown(
            options=['GP', 'MIN', 'FGM',
                     'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                     'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'EFF'],
            value='GP',
            description='Category:',
            disabled=False,
        )

        category2_option = widgets.Dropdown(
            options=['GP', 'MIN', 'FGM',
                     'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                     'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'EFF'],
            value='GP',
            description='Category:',
            disabled=False,
        )

        widgets.interact(plot_bidistribution, category1=category1_option, category2=category2_option,
                         stats=fixed(season_stats))

    elif (graph == 4):

        category1_option = widgets.Dropdown(
            options=['GP', 'MIN', 'FGM',
                     'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                     'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'EFF'],
            value='GP',
            description='Category:',
            disabled=False,
        )

        widgets.interact(plot_kdeaverage, category1=category1_option, stats=fixed(season_stats))