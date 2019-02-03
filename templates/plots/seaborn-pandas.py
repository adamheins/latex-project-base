#!/usr/bin/env python3

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import chain

import IPython


def box_plot():
    # Each row is one run.
    robust = [
        [0.08, 0.07831118909, 0.0792601727, 0.07749300019, 0.07902544397],
        [0.044, 0.04132090475, 0.04147954081, 0.04356325301, 0.04166477053],
        [0.0465, 0.04677486493, 0.04616808733, 0.04638907022, 0.04656522747],
        [0.02050790916, 0.02032825388, 0.02054255897, 0.02044550225, 0.02040942562],
        [0.1522692348, 0.1525553093, 0.1524848025, 0.1526084931, 0.1523906556],
        [0.058, 0.0597247729, 0.05752063332, 0.05669646428, 0.0572725515]]

    nominal = [
        [0.113, 0.1133471099, 0.1132028518, 0.1133153149, 0.1131934735],
        [0.098, 0.09827783782, 0.09790325226, 0.09777538391, 0.09719378262],
        [0.077, 0.07778864667, 0.07779376273, 0.07774054905, 0.07775916191],
        [0.03221161401, 0.03221731026, 0.03226930572, 0.03227976967, 0.03230158247],
        [0.1952487245, 0.1950565572, 0.1950649443, 0.1951113418, 0.1950834155],
        [0.0954, 0.09532654678, 0.09530040828, 0.09524529984, 0.09535713885]]

    rmse = list(chain(*nominal)) + list(chain(*robust))
    case = [i for i in range(1, 7) for _ in range(5)] * 2
    controller = ['Nominal'] * 30 + ['Robust Learning'] * 30

    data = pd.DataFrame({'Controller': controller, 'rmse': rmse, 'case': case})

    fig = plt.figure()
    ax = sns.boxplot(data=data, x='case', y='rmse', hue='Controller',
                     whis=10, showfliers=False)
    ax.get_legend().set_title(None)

    # See https://stackoverflow.com/questions/36874697/how-to-edit-properties-of-whiskers-fliers-caps-etc-in-seaborn-boxplot
    for i, artist in enumerate(ax.artists):
        # Set the linecolor on the artist to the facecolor, and set the facecolor to None
        col = artist.get_facecolor()
        artist.set_edgecolor(col)
        artist.set_facecolor('None')

        # Each box has 6 associated Line2D objects (to make the whiskers,
        # fliers, etc.) Loop over them here, and use the same colour as above
        # (only 5 with fliers removed)
        for j in range(i*5, i*5+5):
            line = ax.lines[j]
            line.set_color(col)
            line.set_mfc(col)
            line.set_mec(col)

    plt.xlabel('Testing Scenario')
    plt.ylabel('Joint RMS Error [rad]')
    plt.grid()

    fig.savefig('boxplot.pdf', bbox_inches='tight', pad_inches=0)

    plt.show()


def plot_multi_eta():
    nominal = [0.23, 0.175, 0.077, 0.12, 0.113, 0.085, 0.094, 0.041, 0.098,
               0.056, 0.170, 0.170, 0.138, 0.106, 0.101]
    robust = [0.146, 0.154, 0.0465, 0.052, 0.08, 0.043, 0.044, 0.027, 0.044,
              0.040, 0.088, 0.088, 0.076, 0.063, 0.052]
    robust_improved = [0.147, 0.153, 0.043, 0.036, 0.079, 0.030, 0.027, 0.018,
                       0.030, 0.024, 0.026, 0.086, 0.075, 0.043, 0.047]

    controller = ['Nominal'] * len(nominal) + ['Robust Learning'] * len(robust) + ['Robust Learning\n(Improved Training)'] * len(robust_improved)
    rmse = nominal + robust + robust_improved
    case = list(range(1, 16)) * 3

    data = pd.DataFrame({'Controller': controller, 'rmse': rmse, 'case': case})

    fig = plt.figure()
    ax = sns.barplot(data=data, x='case', y='rmse', hue='Controller')
    ax.legend(loc=(0.15, 0.55))
    ax.get_legend().set_title(None)
    plt.xlabel('Uncertainty Case')
    plt.ylabel('Joint RMS Error [rad]')
    fig.savefig('many_eta.pdf', bbox_inches='tight', pad_inches=0)
    plt.show()


def plot_multi_traj():
    pass


font_size = 20

params = {
   'axes.labelsize': font_size,
   'font.size': font_size,
   'legend.fontsize': font_size,
   'xtick.labelsize': font_size,
   'ytick.labelsize': font_size,
   'text.usetex': True,
   'figure.figsize': [6, 4]  # Set aspect ratio.
}
# Note figsize was [7,4] for bar plot, [6,4] for box plot,
# and font_size was 16 for bar plot, 20 for box plot.
plt.rcParams.update(params)

#plot_multi_eta()
box_plot()
