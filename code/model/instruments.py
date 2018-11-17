"""

    instruments.py

    Module to hold instrument definitions.

"""

import numpy as np

from . import timbre

HarmonicInst = timbre.Instrument((1, 2, 3, 4, 5), [1, 1, 1, 1, 1])

AharmInst = timbre.Instrument((1, np.sqrt(2), np.sqrt(5), np.sqrt(7), 1017./313.), (1, 1, 1, 1, 1))
