"""

    harmonic_curves.py

    Script to plot dissonance curves for a simulated harmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import timbre
import model

import curves

from instruments import HarmonicInst

# Make instruments
r = 0.88

Harmonic = HarmonicInst(440)

curves.dissonance_curve(Harmonic, 'harmonic_dissonance_curve.png', title = 'Harmonic Timbre')
