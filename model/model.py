"""

    Implementation of the dissonance model from Sethares 1993

"""

import numpy as np
from matplotlib import pyplot as plt

## CONSTANTS

a = 3.5
b = 5.75


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
    Da = 0
    for i,fi in enumerate(F):
        for j,fj in enumerate(F):
            Da += d(fi, alpha*fj, V[i], V[j])

    return D(F, V) + D(alpha*F, V) + Da
#    return Da

def d(f1, f2, v1, v2):
    dstar = 0.24
    s1 = 0.0021
    s2 = 19
    s = dstar/(s1*f1 + s2)
    exp1 = np.exp(- a * s * np.abs(f2-f1) )
    exp2 = np.exp(- b * s * np.abs(f2-f1) )
    return v1*v2*(exp1 - exp2)

if __name__ == '__main__':
    print(d(440, 440, 1, 1))
    print(d(440, 442, 1, 1))
    print(d(440, 440*3/2, 1, 1))

    v1 = 1
    v2 = 1
    f1 = 440
    F2 = np.linspace(f1, 2*f1, 1000)
    diss = [d(f1, f2, v1, v2) for f2 in F2]

    fig, ax = plt.subplots()
    ax.plot(F2/f1, diss)
    ax.set_xlabel('$\\alpha = \\frac{f_2}{f_1}$')
    ax.set_ylabel('Perceived dissonance')
    ax.set_title('Dissonance curve for $f_1 = 440$ Hz')
    ax.grid()
    fig.savefig('disscurve0.png', dpi = 400)

    F = np.array([440*i for i in range(1, 6)])
    V = [np.exp(np.log(0.88)*i) for i in range(5)]
    print(F)
    print(V)

    fig, ax = plt.subplots()
    alpha = np.linspace(1., 2.1, 1000)
    disson = [DF(F, V, a) for a in alpha]

    ax.plot(alpha, np.array(disson)/np.max(disson))
    ax.set_xlabel('$\\Number of semitones$')
    ax.set_ylabel('Perceived Dissonance')
    ax.set_title('Dissonance curve for harmonic timbre')
#    ax.set_xticks(np.linspace(1, 2, 13))
    ax.set_xticks([2.0**(i/12.) for i in range(13)])
    ax.set_xticklabels([str(i) for i in range(13)])
    ax.grid()
    fig.savefig('disscurve_harmonic.png', dpi = 400)
