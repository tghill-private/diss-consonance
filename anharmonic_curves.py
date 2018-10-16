"""

    anharmonic_curves.py

    Script to plot dissonance curves for a simulated anharmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import timbre
import model

import curves

from instruments import AharmInst

AHarmonic = AharmInst(440)

curves.dissonance_curve(AHarmonic, 'anharmonic_dissonance_curve.png', title = 'Anharmonic Timbre')
