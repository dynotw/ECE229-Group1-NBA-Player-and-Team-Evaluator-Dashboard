import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_plot_contour():
        '''
        x is the tag of the dataset
        y is another tag of the dataset
        stats is the name of dataframe
        input: selected tags, dataset
        plot: bivariate contour of the selected tag
        '''

        season = 2019
        category1 = "GP"
        category2 = "MIN"
        assert isinstance(season,int)
        assert isinstance(category1, str)
        assert isinstance(category2, str)

        stats = pd.read_csv(str(season)+'-'+ str(season%1000 + 1)+ ".csv")
        assert isinstance(stats,pd.DataFrame)
        assert not stats is None
        df = stats

        sns.set(style="darkgrid")
        sns.jointplot(x=category1, y=category2, data=df, kind="kde", height=10)
 
        return

def test_plot_distribution():
        '''
        x is the tag of the dataset
        stats is the name of dataframe
        input: selected tag, dataset
        plot: distribution of the selected tag
        '''
        season = 2019
        category1 = "GP"
        assert isinstance(season,int)
        assert isinstance(category1, str)

        stats = pd.read_csv(str(season)+'-'+ str(season%1000 + 1)+ ".csv")
        assert isinstance(stats,pd.DataFrame)
        assert not stats is None

        df = stats
        plt.figure(figsize=(15, 8))
        sns.set(style="darkgrid")
        plt.ylabel('Ratio')
        plt.title('Distribution of %s' % category1)
        sns.distplot(df[category1], bins=10, kde=True, rug=False)

        return

def test_plot_bidistribution():
        '''
        x is the tag of the dataset
        y is another tag of the dataset
        stats is the name of dataframe
        input: selected tags, dataset
        plot: bivariate distribution of the selected tag
        '''
        season = 2019
        category1 = "GP"
        category2 = "MIN"
        assert isinstance(season,int)
        assert isinstance(category1, str)
        assert isinstance(category2, str)

        stats = pd.read_csv(str(season)+'-'+ str(season%1000 + 1)+ ".csv")
        assert isinstance(stats,pd.DataFrame)
        assert not stats is None

        df = stats
        sns.set(style="darkgrid")
        dsf = pd.DataFrame(df, columns=[category1, category2])
        sns.jointplot(x=category1, y=category2, data=dsf, height=10)

        return


def plot_kdeaverage():
        '''
        input: selected tag, stats
        plot: distribution's kde curve of the average value of selected tag
        '''

        season = 2019
        category1 = "GP"
        assert isinstance(season,int)
        assert isinstance(category1, str)

        stats = pd.read_csv(str(season)+'-'+ str(season%1000 + 1)+ ".csv")
        assert isinstance(stats,pd.DataFrame)
        assert not stats is None

        sns.set(style="darkgrid")
        y = stats[category1]
        y = y.astype(float)
        plt.figure(figsize=(15, 8))
        plt.ylabel('Probability Density')
        plt.xlabel('%s per game' % category1)
        plt.title('Distribution of %s' % category1)
        seaborn.distplot(y, bins=10, hist=False, kde=True, rug=False)
        seaborn.kdeplot(y, shade=True)

        return
