"""

    curves.py

    Module to make it easy to make dissonance curves.

    Having module for making figures will also make sure all the figures
    are in a consistent style.

"""

from matplotlib import pyplot as plt

import numpy as np

from model import model

def dissonance_curve(T, figname, title = 'Dissonance curve'):
    """Draw a dissonance curve.

    Labels the x-axis with semitones for 12 TET scale
    """
    alpha = np.linspace(1, 2.2, 1000)
    dissonance = np.array([model.DF(T.F, T.V, a) for a in alpha])
    dissonance /= dissonance.max()

    fig, ax = plt.subplots(figsize = (8, 4))

    ax.set_title(title)

    ax.set_xlabel('Number of semitones')
    ax.set_ylabel('Perceived dissonance')

    ax.plot(alpha, dissonance)

    ax.set_xticks([2**(i/12.) for i in range(13)])
    ax.set_xticklabels([str(i) for i in range(13)])
    ax.grid()

    fig.savefig(figname, dpi = 600)
