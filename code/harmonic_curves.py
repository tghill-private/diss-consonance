"""

    harmonic_curves.py

    Script to plot dissonance curves for a simulated harmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import model
from model import timbre
from model import model

import curves

from model.instruments import HarmonicInst

# Make instruments
r = 0.88

Harmonic = HarmonicInst(440)

curves.dissonance_curve(Harmonic, '../figs/harmonic_dissonance_curve.png', title = 'Harmonic Timbre')
