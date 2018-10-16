"""

    harmonic_curves.py

    Script to plot dissonance curves for a simulated harmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import timbre
import model

import curves

# Make instruments
r = 0.88
HarmonicInst = timbre.Instrument((1, 2, 3, 4, 5), [r**i for i in range(5)], name = 'Harmonic')

Harmonic = HarmonicInst(440)

curves.dissonance_curve(Harmonic, 'harmonic_dissonance_curve.png', title = 'Harmonic Timbre')
