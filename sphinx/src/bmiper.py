import pandas as pd
import logging

import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

cf.go_offline() # required to use plotly offline (no account required).
py.init_notebook_mode() # graphs charts inline (IPython).

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def plot_choice(year, choice1, choice2, player):
    '''
    plot 2D figure for chosen attributes
    
    :param year: the year for which you want to plot the data for
    :type year: int

    :param choice1: Selected attribute to compare 1
    :type choice1: string

    :param choice2: Selected attribute to compare 2
    :type choice2: string

    :param player: the player you want to highlight
    :type player: string
    
    :return: 2D plot based on the selected input choices
    '''
    assert isinstance(choice1,str) and isinstance(choice2,str)
    assert choice1 != choice2, "please choose 2 different attributes"
    
    proc_stats_df = pd.read_csv('seasons_stats_procecced.csv', index_col=0)
    proc_stats_df = proc_stats_df.assign(bmi = proc_stats_df.weight / ((proc_stats_df.height/100) ** 2))
    
    #Value Added = ([Minutes * (PER - PRL)] / 67). PRL (Position Replacement Level) = 11.5 for power forwards, 
    #11.0 for point guards, 10.6 for centers, 10.5 for shooting guards and small forwards
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PF', 'PRL'] = 11.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PG', 'PRL'] = 11.0
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'C', 'PRL'] = 10.6
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SG', 'PRL'] = 10.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SF', 'PRL'] = 10.5 
    proc_stats_df = proc_stats_df.assign(value_added = ((proc_stats_df.MP * (proc_stats_df.PER -proc_stats_df.PRL))/67)*proc_stats_df.PRL)
    
    proc_stats_df = proc_stats_df.rename({'height':'Height', 'bmi':'BMI', 'value_added':'Value Added'}, axis='columns')
    to_plot = proc_stats_df.loc[proc_stats_df['Year'] == year]
    to_plot = to_plot.reset_index() 
    
    #highlight selected player
    colors = ['seagreen',] * len(to_plot)
    colors[to_plot.loc[to_plot['Player'] == player].index.to_numpy()[0]] = 'crimson'

    fig = go.Figure(data=[go.Scatter(
    x=to_plot[choice1],
    y=to_plot[choice2],
    text=to_plot['Player'],
    mode='markers',
    marker_color=colors # marker color can be a single color value or an iterable
    )])
    
    fig.update_layout(title_text= choice1+' vs. '+choice2, xaxis_title = choice1, yaxis_title = choice2)
    
    fig.show()
    
    return 


def plot_3d(year,choice1,choice2,choice3,player):
    '''
    plot 3D figure for chosen attributes
      
    :param year: the year for which you want to plot the data for
    :type year: int

    :param choice1: Selected attribute to compare 1
    :type choice1: string

    :param choice2: Selected attribute to compare 2
    :type choice2: string

    :param choice2: Selected attribute to compare 3
    :type choice3: string

    :param player: the player you want to highlight
    :type player: string
    
    :return: 3D plot based on the selected input choices
    '''
    assert isinstance(choice1,str) and isinstance(choice2,str) and isinstance(choice3,str)
    assert choice1 != choice2 and choice2 != choice3 and choice1 != choice3,"please choose 3 different attributes"
    
    proc_stats_df = pd.read_csv('seasons_stats_procecced.csv', index_col=0)
    proc_stats_df = proc_stats_df.assign(bmi=proc_stats_df.weight / ((proc_stats_df.height/100) ** 2))
    
    #Value Added = ([Minutes * (PER - PRL)] / 67). PRL (Position Replacement Level) = 11.5 for power forwards, 
    #11.0 for point guards, 10.6 for centers, 10.5 for shooting guards and small forwards
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PF', 'PRL'] = 11.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PG', 'PRL'] = 11.0
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'C', 'PRL'] = 10.6
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SG', 'PRL'] = 10.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SF', 'PRL'] = 10.5 
    proc_stats_df = proc_stats_df.assign(value_added = ((proc_stats_df.MP * (proc_stats_df.PER - proc_stats_df.PRL))/67)*proc_stats_df.PRL)
    
    proc_stats_df = proc_stats_df.rename({'height':'Height', 'bmi':'BMI', 'value_added':'Value Added'}, axis='columns')
    to_plot = proc_stats_df.loc[proc_stats_df['Year'] == year]
    to_plot = to_plot.reset_index() 
    
    #highlight selected player
    colors = ['seagreen',] * len(to_plot)
    colors[to_plot.loc[to_plot['Player'] == player].index.to_numpy()[0]] = 'crimson'

    fig = go.Figure(data=[go.Scatter3d(
    x=to_plot[choice1],
    y=to_plot[choice2],
    z=to_plot[choice3],
    text=to_plot['Player'],
    mode='markers',
    marker_color=colors)], layout = go.Layout(xaxis = dict(title = choice1), yaxis = dict(title = choice2)))
    
    fig.update_layout(title_text= choice1+' (x-axis) vs. '+choice2+' (y-axis) vs. '+choice3+ ' (z-axis) ')
    
    fig.show()
    
    return 