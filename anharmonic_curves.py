"""

    anharmonic_curves.py

    Script to plot dissonance curves for a simulated anharmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import timbre
import model

import curves

# Make instruments
r = 0.88
F = (1, np.sqrt(2), np.sqrt(3), np.sqrt(5), np.sqrt(7))
HarmonicInst = timbre.Instrument(F, [r**i for i in range(5)], name = 'Harmonic')

Harmonic = HarmonicInst(440)

curves.dissonance_curve(Harmonic, 'anharmonic_dissonance_curve.png', title = 'Anharmonic Timbre')
