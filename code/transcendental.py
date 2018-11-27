"""

    anharmonic_curves.py

    Script to plot dissonance curves for a simulated anharmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import model
from model import timbre
from model import synth

import curves

f = [1, np.sqrt(2), np.sqrt(5), np.sqrt(7), np.sqrt(11)]
# f = [1, 2, 3]
amps = [0.75**i for i in range(len(f))]
transc = timbre.Instrument(f, amps)

f0 = 440
T = transc(f0)

alpha = np.linspace(1, 3.5, 1000)
diss = np.array([model.model.DF(T.F, T.V, a) for a in alpha])
diss /= diss.max()

fig, ax = plt.subplots(figsize = (8, 4))

# ax.set_title(title)

ax.set_ylabel('Perceived dissonance')

ax.plot(alpha, diss)
ax.set_xlabel('$\\alpha$')

ax.grid()



min1 = np.argmin(diss[300:400])
l1 = np.sqrt(2)

min2 = np.argmin(diss[400:])
l2 = np.sqrt(3.5)
print(l2)

l3 = np.sqrt(7)

ax.axvline(np.sqrt(2), color = 'r', lw = 1)
ax.axvline(l2, color = 'r', lw = 1)

ax.axvline(l3, color = 'r', lw = 1)
ax.axvline(np.sqrt(5), color = 'r', lw = 1)

ax.axvline(np.sqrt(11), lw = 1, color = 'r')

delta = 0.02
# ax.text(l1 + delta, 0.6, "$\\alpha = %.4f$" % l1)
#
# ax.text(l2 + delta, 0.6, "$\\alpha = %.4f$" % l2)

fig.savefig('../figs/transcendental_curve.png', dpi = 600)

alpha = np.sqrt(2)

fig, ax = plt.subplots(figsize = (3, 6))

for v in f:
    ax.axhline(v, color = 'k', lw = 1)

for v in alpha * np.array(f):
    ax.axhline(v, color = 'r', lw = 1, ls = '--')

ax.set_ylabel('$\\alpha$')

ax.set_xticks([])

# ax.set_yscale('log')

plt.tight_layout()

fig.savefig('../figs/transcendental_partials.png', dpi = 400)

synth_transc = synth.synthesizer(transc)

synth_transc.save_interval(440, 1, '../audio/transcendental_unison.wav')
synth_transc.save_interval(440, 2., '../audio/transcendental_octave.wav')
synth_transc.save_interval(440, np.sqrt(2), '../audio/transcendental_sqrt2.wav')
