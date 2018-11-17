"""

    Implementation of the dissonance model from Sethares 1993

"""

import numpy as np
from matplotlib import pyplot as plt

## CONSTANTS

# These were fit to match experimental data
a = 3.5
b = 5.75

def d(f1, f2, v1, v2):
    """Compute total dissonance for pair of frequencies f1, f2 with
    relative amplitudes v1, v2
    """
    dstar = 0.24
    s1 = 0.0021
    s2 = 19
    s = dstar/(s1*f1 + s2)
    exp1 = np.exp(- a * s * np.abs(f2-f1) )
    exp2 = np.exp(- b * s * np.abs(f2-f1) )
    return v1*v2*(exp1 - exp2)


def D(F, V):
    """Compute Plomp-Levelt dissonance for given frequencies and amplitudes.

    Compute d according to Sethares 1993.

    Args:
     * F: iterable of frequencies present
     * V: iterable of relative amplitudes
    """
    D = 0
    for i,fi in enumerate(F):
        for j,fj in enumerate(F):
            D += 0.5 * d(fi, fj, V[i], V[j])
    return D

def DF(F, V, alpha):
    """Compute dissonance for frequency + harmonics given in F,
    when played with same note at interval alpha.

    Args:
     * F: iterable of frequencies present in fundamental note
     * V: iterable of relative amplitudes for each partia
     * alpha: interval to compute dissonance (Frequency ratio)
    """
    Da = 0
    for i,fi in enumerate(F):
        for j,fj in enumerate(F):
            Da += d(fi, alpha*fj, V[i], V[j])

    return D(F, V) + D(alpha*F, V) + Da
