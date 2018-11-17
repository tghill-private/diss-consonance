"""

    instruments.py

    Module to hold instrument definitions.

"""

import numpy as np

from . import timbre

r = 0.75
amps = [r**i for i in range(5)]
HarmonicInst = timbre.Instrument((1, 2, 3, 4, 5), amps)

AharmInst = timbre.Instrument((1, np.sqrt(2), np.sqrt(5), np.sqrt(7), 1017./313.), amps)
