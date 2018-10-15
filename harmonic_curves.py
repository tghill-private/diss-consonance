"""

    harmonic_curves.py

    Script to plot dissonance curves for a simulated harmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import timbre
import model

# Make instruments
r = 0.88
HarmonicInst = timbre.Instrument((1, 2, 3, 4, 5), [r**i for i in range(5)], name = 'Harmonic')

Harmonic = HarmonicInst(440)

alpha = np.linspace(1, 2.2, 1000)

disson = np.array([model.DF(Harmonic.F, Harmonic.V, a) for a in alpha])
disson /= disson.max()

fig, ax = plt.subplots()

ax.set_title('Dissonance curve for harmonic timbre')

ax.set_xlabel('$\\alpha$')
ax.set_ylabel('Perceived dissonance')

ax.plot(alpha, disson)

ax.set_xticks([2**(i/12.) for i in range(13)])
ax.set_xticklabels([str(i) for i in range(13)])
ax.grid()

fig.savefig('harmonic_dissonance_curve.png', dpi = 600)
