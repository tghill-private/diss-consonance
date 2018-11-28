"""

    stetched.py

    Script to plot dissonance curves for a stretched timbres

"""

from matplotlib import pyplot as plt

import numpy as np

import model
from model import timbre
from model import synth

import curves

# import synthesizer as synth

A = [1.75, 2.25]
J = np.arange(1, 6)

f0 = 440

alpha = np.linspace(1., 2.**(15/12.), 1000)
fc = A[0]**np.log2(J)
fs = A[1]**np.log2(J)

print(fc)
print(fs)

v = 0.75**(J-1)

print(v)

Ic = timbre.Instrument(fc, v)
Is = timbre.Instrument(fs, v)

Tc = Ic(f0)
Ts = Is(f0)

dc = np.array([model.model.DF(Tc.F, Tc.V, a) for a in alpha])
ds = np.array([model.model.DF(Ts.F, Ts.V, a) for a in alpha])

dc /= dc.max()
ds /= ds.max()

fig, (ax1, ax2) = plt.subplots(figsize = (8, 5), nrows = 2, sharex = False)

ax1.set_ylabel('Perceived dissonance')
ax2.set_ylabel('Perceived dissonance')
ax1.plot(alpha, dc)
ax2.plot(alpha, ds)

ax2.set_xlabel('$\\alpha$')

n1 = int(12*np.log(alpha[-1])/np.log(A[0])) + 1
n2 = int(12*np.log(alpha[-1]/np.log(A[1]))) + 1

print(n1)
print(n2)
ax1.set_xticks([A[0]**(i/12.) for i in range(n1)])
ax1.set_xticklabels([str(i) for i in range(n1)])

ax1twin = ax1.twiny()
ax1twin.set_xlim(ax1.get_xlim())
ax1twin.set_xticks([2**(i/12.) for i in range(15)])
ax1twin.set_xticklabels([str(i) for i in range(15)])
ax1twin.tick_params(axis='x', which='both', bottom = False, top = True, labelbottom=False, labeltop=True)
ax1twin.tick_params(axis='y', which='both', bottom = False, top = False)

ax2twin = ax2.twiny()
ax2twin.set_xlim(ax1.get_xlim())
ax2twin.set_xticks([2**(i/12.) for i in range(15)])
ax2twin.set_xticklabels([str(i) for i in range(15)])
ax2twin.tick_params(axis='x', which='both', bottom = False, top = True, labelbottom=False, labeltop=True)
ax2twin.tick_params(axis='y', which='both', bottom = False, top = False)


ax1twin.xaxis.tick_top()
ax2.set_xticks([A[1]**(i/12.) for i in range(n2)])
ax2.set_xticklabels([str(i) for i in range(n2)])
ax2.set_xlabel('Number of tones $A^{n/12}$')

induced1 = [1, 1.195, 1.2626, 1.386, 1.51, A[0]]
induced2 = [1, 1.3, 1.4, 1.605, 1.8175, A[1]]

for i in induced1[1:]:
    ax1.axvline(i, color = 'k', lw = 1)

for i in induced2[1:]:
    ax2.axvline(i, color = 'k', lw = 1)

ax1.grid()
ax2.grid()

ax1.axvline(A[0], color = 'red')

ax2.axvline(A[1], color = 'red')
plt.tight_layout()

fig.savefig('../figs/stretched_timbres.png', dpi = 600)

synthesizer_compressed = synth.synthesizer(Ic)
synthesizer_stretched = synth.synthesizer(Is)

# List of frequencies to play
ints = [1, 2**(1./6.), 2**(1./3.), 2**(5./12.), 2**(7./12.), 2**(9./12.), 2**(11./12.), 2.]
synthesizer_compressed.save_interval(440, ints, '../audio/02_01_compressed_timbre_12TET_scale_440.wav', duration = 1.)
synthesizer_compressed.save_interval(440, induced1, '../audio/02_02_compressed_timbre_induced_scale_440.wav', duration = 1.)

synthesizer_stretched.save_interval(220, ints, '../audio/03_01_stretched_timbre_12TET_scale_220.wav', duration = 1.)
synthesizer_stretched.save_interval(220, induced2, '../audio/03_02_stretched_timbre_induced_scale_220.wav', duration = 1.)
