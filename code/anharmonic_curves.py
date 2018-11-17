"""

    anharmonic_curves.py

    Script to plot dissonance curves for a simulated anharmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import model
import model.timbre
from model import instruments

import curves

AHarmonic = instruments.AharmInst(440)

curves.dissonance_curve(AHarmonic, '../figs/anharmonic_dissonance_curve.png', title = 'Anharmonic Timbre')
