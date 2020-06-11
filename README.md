# NBA Player and Team Evaluator Dashboard

## User Dashboard
URL: http://44.230.28.148:8866/

## Team Members
- Hassan Eid, Jinglong Du, Tejas Sadarahalli, Yening Dong, Yuchen Tang, Xiaotian Ma

## Product Motivation
* We have made many insights using NBA data by analyzing multiple statistics:
     * On-court: PTS, AST, etc.
     * Physical: Height, BMI, etc. 
* Our insights can be extremely useful to users making high-level decisions regarding NBA players.

## User Story
* User: NBA General Manager
* Goal: Easily visualize large data sets and make predictions based on desired statistic.
* Want: An easy-to-use interface that allows me to compare players and predict the strength of teams made up of selected players.

## Dataset

* [NBA Stats Official Website](https://stats.nba.com)
* [NBA Player Stats Kaggle Dataset](https://www.kaggle.com/drgilermo/nba-players-stats)

## Solution 
* A dashboard that provides the desired functionality:
    * Interactive player comparisons
    * Highly-detailed player metrics
    * Team-based evaluations / predictions

## File Structure
```
|pyTest                                 <- Contains all test scripts for the project
|   |coverage_report.pdf                <- Coverage report of pytest 
|   |test_AtrributeDisrabution.py 
|   |test_BestFeatures.py
|   |test_DataProcessing.py
|   |test_DataScrapping.py
|   |test_RadarPlot.py
|   |test_SeasonData.py
|   |test_ShotDisFreq.py
|   |test_WinPredict.py
|   |test_bmiper.py
|
|Atrributes_Distribution.py             
|BestFeatures.py
|DataProcessing.py
|DataScrapping.py
|Main.ipynb                             <- Main Jupyter Notebook file that contains all code required and visualize the dashboard
|NBA.png                                <- Image for glossery of acronyms
|README.md                              <- Github Documenation file
|RadarPlot.py
|Season_Data.py
|ShotDisFreq.py
|WinPredict.py
|bmiper.py

```
## Instructions on Running Code

-Python version: Python 3.6.6 64-bit

### Required Packages

1. numpy
2. pandas
3. sklearn

#### Plotting Packages

1. Seaborn
2. Plotly 

For installing these packages, you can use either pip to install packages. For example,
```
pip3 install numpy
```
if you are using anaconda you can use:

```
conda install numpy
```
