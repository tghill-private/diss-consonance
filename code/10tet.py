"""

    10TET.py

    Script to plot dissonance curves for a simulated anharmonic instrument

"""

from matplotlib import pyplot as plt

import numpy as np

import model
from model import timbre

import curves

b = 2.**(1./10.)

f = [1, b**5, b**8, b**10]
# f = [1, 2, 3]
amps = [1, 0.5, 0.5, 1]
tet = timbre.Instrument(f, amps)

f0 = 440
T = tet(f0)

alpha = np.linspace(1, b**12, 1000)
diss = np.array([model.model.DF(T.F, T.V, a) for a in alpha])
diss /= diss.max()

fig, ax = plt.subplots(figsize = (8, 4))

# ax.set_title(title)

ax.set_ylabel('Perceived dissonance')

ax.plot(alpha, diss)
ax.set_xlabel('Scale step')

ax.grid()

ax.set_xticks([b**i for i in range(12)])

ax.set_xticklabels([str(i) for i in range(12)])

fig.savefig('../figs/10tet_induced_timbre.png', pdi = 400)



# min1 = np.argmin(diss[300:400])
# l1 = np.sqrt(2)
#
# min2 = np.argmin(diss[400:])
# l2 = np.sqrt(3.5)
# print(l2)
#
# l3 = np.sqrt(7)
#
# ax.axvline(np.sqrt(2), color = 'r', lw = 1)
# ax.axvline(l2, color = 'r', lw = 1)
#
# ax.axvline(l3, color = 'r', lw = 1)
# ax.axvline(np.sqrt(5), color = 'r', lw = 1)
#
# ax.axvline(np.sqrt(11), lw = 1, color = 'r')
#
# delta = 0.02
# # ax.text(l1 + delta, 0.6, "$\\alpha = %.4f$" % l1)
# #
# # ax.text(l2 + delta, 0.6, "$\\alpha = %.4f$" % l2)
#
# fig.savefig('../figs/transcendental_curve.png', dpi = 600)
#
# alpha = np.sqrt(2)
#
# fig, ax = plt.subplots(figsize = (3, 6))
#
# for v in f:
#     ax.axhline(v, color = 'k', lw = 1)
#
# for v in alpha * np.array(f):
#     ax.axhline(v, color = 'r', lw = 1)
#
# ax.set_ylabel('$\\alpha$')
#
# ax.set_xticks([])
#
# # ax.set_yscale('log')
#
# plt.tight_layout()
#
# fig.savefig('../figs/transcendental_partials.png', dpi = 400)
