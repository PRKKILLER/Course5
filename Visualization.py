import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle


large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

data=pd.read_csv("sentiments.csv").set_index("Sentiment")
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '311': {
            'values': data['Sound'] / 1,
            'labels': ["{0} ({1})".format(n, v) for n, v in data['Sound'].items()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1), 'fontsize': 12},
            'title': {'label': 'Sound Quality', 'loc': 'left'}
        },
        '312': {
             'values': data['Battery'] / 1,
            'labels': ["{0} ({1})".format(n, v) for n, v in data['Fingerprint'].items()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1), 'fontsize': 12},
            'title': {'label': 'Battery Life', 'loc': 'left'}
            
        },
        '313': {
            'values': data['Picture'] / 1,
            'labels': ["{0} ({1})".format(n, v) for n, v in data['Value'].items()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1), 'fontsize': 12},
            'title': {'label': 'Picture Quality', 'loc': 'left'}
        },
    },
    rows=5,
    colors=("#2196f3", "#ff5252", "#999999"),  # Default argument values for subplots
    figsize=(10, 7),  # figsize is a parameter of plt.figure
    legend={'loc': 'upper left', 'bbox_to_anchor': (2, 3)},
    icons='child', icon_size=18, 
    icon_legend=True
    

   
)
fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
plt.show()


fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '311': {
            'values': data['Value'] / 1,
            'labels': ["{0} ({1})".format(n, v) for n, v in data['Sound'].items()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1), 'fontsize': 12},
            'title': {'label': 'Value for Money', 'loc': 'left'}
        },
        '312': {
             'values': data['Fingerprint'] / 1,
            'labels': ["{0} ({1})".format(n, v) for n, v in data['Fingerprint'].items()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1), 'fontsize': 12},
            'title': {'label': 'Fingerprint', 'loc': 'left'}
            
        },

    },
    rows=5,
    colors=("#2196f3", "#ff5252", "#999999"),  # Default argument values for subplots
    figsize=(10, 7),  # figsize is a parameter of plt.figure
    legend={'loc': 'upper left', 'bbox_to_anchor': (2, 3)},
    icons='child', icon_size=18, 
    icon_legend=True
    

   
)




fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
plt.show()