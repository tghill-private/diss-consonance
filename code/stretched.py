"""

    stetched.py

    Script to plot dissonance curves for a stretched timbres

"""

from matplotlib import pyplot as plt

import numpy as np

import model
from model import timbre

import curves

# import synthesizer as synth

A = [1.75, 2.25]
J = np.arange(1, 7)

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

fig, (ax1, ax2) = plt.subplots(figsize = (8, 4), nrows = 2, sharex = True)

ax1.set_ylabel('Perceived dissonance')
ax2.set_ylabel('Perceived dissonance')
ax1.plot(alpha, dc)
ax2.plot(alpha, ds)

ax2.set_xlabel('$\\alpha$')

ax2.set_xticks([2**(i/12.) for i in range(16)])
ax2.set_xticklabels([str(i) for i in range(16)])
ax2.set_xlabel('Number of semitones')

ax1.grid()
ax2.grid()

ax1.axvline(A[0], color = 'red')

ax2.axvline(A[1], color = 'red')

fig.savefig('../figs/stretched_timbres.png', dpi = 600)

# player = synth.Player()
# player.open_stream()
#
# writer = synth.Writer()
#
# sy = synth.Synthesizer()
#
# f01 = 440.
# f02 =
#
# H1 = HarmonicInst(f01)
# H2 = HarmonicInst(f02)
#
# A1 = AharmInst(f01)
# A2 = AharmInst(f02)
#
# print(np.concatenate((A1.F, A2.F)))
#
# print(np.concatenate((H1.F, H2.F)))
#
# harmwave = sy.generate_chord(list(np.concatenate((H1.F, H2.F))), 3.0)
# player.play_wave(harmwave)
# writer.write_wave("harmonic.wav", harmwave)
#
# # aharmchord = [440., 440.*817/411]
# aharmwave = sy.generate_chord(list(np.concatenate((A1.F, A2.F))), 3.0)
# player.play_wave(aharmwave)
# writer.write_wave("anharmonic.wav", aharmwave)
