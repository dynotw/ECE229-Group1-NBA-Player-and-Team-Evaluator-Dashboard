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

def test_plot_choice():
    '''
    plot 2D figure for chosen attributes
    
    Inputs - 
    choice1: Selected attribute to compare 1
    choice2: Selected attribute to compare 2
    input type: str,str
    
    Output- 
    2D plot based on the selected input choices
    '''
    
    proc_stats_df = pd.read_csv('seasons_stats_procecced.csv', index_col=0)
    assert isinstance(proc_stats_df, pd.DataFrame)
    assert not proc_stats_df is None
    assert ('weight' and 'height'and'Player'and'FG%'and'Year'and'pos_simple'and'MP'and'PER') in proc_stats_df
    
    proc_stats_df = proc_stats_df.assign(bmi = proc_stats_df.weight / ((proc_stats_df.height/100) ** 2))
    assert ('bmi') in proc_stats_df
    
    #Value Added = ([Minutes * (PER - PRL)] / 67). PRL (Position Replacement Level) = 11.5 for power forwards, 
    #11.0 for point guards, 10.6 for centers, 10.5 for shooting guards and small forwards
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PF', 'PRL'] = 11.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PG', 'PRL'] = 11.0
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'C', 'PRL'] = 10.6
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SG', 'PRL'] = 10.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SF', 'PRL'] = 10.5 
    
    proc_stats_df = proc_stats_df.assign(value_added = ((proc_stats_df.MP * (proc_stats_df.PER -proc_stats_df.PRL))/67)*proc_stats_df.PRL)
    
    proc_stats_df = proc_stats_df.rename({'height':'Height', 'bmi':'BMI', 'value_added':'Value Added'}, axis='columns')
    assert ('BMI' and 'Height' and 'Value Added') in proc_stats_df
    
    to_plot = proc_stats_df.loc[proc_stats_df['Year'] == 2015]
    to_plot = to_plot.reset_index() 
    assert isinstance(to_plot, pd.DataFrame)
    assert not to_plot is None
    
    #highlight selected player
    colors = ['seagreen',] * len(to_plot)
    colors[to_plot.loc[to_plot['Player'] == 'Chris Paul'].index.to_numpy()[0]] = 'crimson'
    assert len(colors) == len(to_plot)

    fig = go.Figure(data=[go.Scatter(
    x=to_plot['BMI'],
    y=to_plot['PER'],
    text=to_plot['PER'],
    mode='markers',
    marker_color=colors # marker color can be a single color value or an iterable
    )])
    
    fig.update_layout(title_text= 'BMI vs. PER', xaxis_title = 'BMI', yaxis_title = 'PER')
    
    fig.show()
    
    return 


def test_plot_3d():
    '''
    plot 3D figure for chosen attributes
      
    Inputs - 
    choice1: Selected attribute to compare 1
    choice2: Selected attribute to compare 2
    choice3: Selected attribute to compare 3
    input type: str, str, str
    
    Output- 
    3D plot based on the selected input choices
    '''
    
#     year,choice1,choice2,choice3,player
    
    proc_stats_df = pd.read_csv('seasons_stats_procecced.csv', index_col=0)
    assert isinstance(proc_stats_df, pd.DataFrame)
    assert not proc_stats_df is None
    assert ('weight' and 'height'and'Player'and'FG%'and'Year'and'pos_simple'and'MP'and'PER') in proc_stats_df
    
    proc_stats_df = proc_stats_df.assign(bmi=proc_stats_df.weight / ((proc_stats_df.height/100) ** 2))
    assert ('bmi') in proc_stats_df
    
    #Value Added = ([Minutes * (PER - PRL)] / 67). PRL (Position Replacement Level) = 11.5 for power forwards, 
    #11.0 for point guards, 10.6 for centers, 10.5 for shooting guards and small forwards
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PF', 'PRL'] = 11.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'PG', 'PRL'] = 11.0
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'C', 'PRL'] = 10.6
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SG', 'PRL'] = 10.5 
    proc_stats_df.loc[proc_stats_df['pos_simple'] == 'SF', 'PRL'] = 10.5 
    
    proc_stats_df = proc_stats_df.assign(value_added = ((proc_stats_df.MP * (proc_stats_df.PER - proc_stats_df.PRL))/67)*proc_stats_df.PRL)
    
    proc_stats_df = proc_stats_df.rename({'height':'Height', 'bmi':'BMI', 'value_added':'Value Added'}, axis='columns')
    assert ('BMI' and 'Height' and 'Value Added') in proc_stats_df
        
    to_plot = proc_stats_df.loc[proc_stats_df['Year'] == 2015]
    to_plot = to_plot.reset_index()
    assert isinstance(to_plot, pd.DataFrame)
    assert not to_plot is None
    
    #highlight selected player
    colors = ['seagreen',] * len(to_plot)
    colors[to_plot.loc[to_plot['Player'] == 'Chris Paul'].index.to_numpy()[0]] = 'crimson'
    assert len(colors) == len(to_plot)

    fig = go.Figure(data=[go.Scatter3d(
    x=to_plot['BMI'],
    y=to_plot['PER'],
    z=to_plot['FG%'],
    text=to_plot['Player'],
    mode='markers',
    marker_color=colors)], layout = go.Layout(xaxis = dict(title = 'BMI'), yaxis = dict(title = 'PER')))
    
    fig.update_layout(title_text='BMI (x-axis) vs. PER (y-axis) vs. FG% (z-axis) ')
    
    fig.show()
    
    return 