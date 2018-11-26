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
J = np.arange(1, 4)

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

synthesizer_compressed = synth.synthesizer(Ic)
synthesizer_stretched = synth.synthesizer(Is)

# synthesizer_compressed.play_interval(440, 1, duration = 1.)
# synthesizer_compressed.play_interval(440, 2.**(2./12.), duration = 1.)
# synthesizer_compressed.play_interval(440, 2.**(4./12.), duration = 1.)
#
# synthesizer_compressed.play_interval(440, 2.**(5./12.), duration = 1.)
# synthesizer_compressed.play_interval(440, 2.**(7./12.), duration = 1.)
# synthesizer_compressed.play_interval(440, 2.**(9./12.), duration = 1.)
# synthesizer_compressed.play_interval(440, 2.**(11./12.), duration = 1.)
# synthesizer_compressed.play_interval(440, 2.**(12./12.), duration = 1.)
# synthesizer_compressed.play_interval(440, 2.25, duration = 1.)

ints = (1, 2**(1./6.), 2**(1./3.), 2**(5./12.), 2**(7./12.), 2**(9./12.), 2**(11./12.), 2., 2.25)
synthesizer_compressed.save_interval(440, ints, '../audio/compressed_timbre_12TET_scale.wav', duration = 1.)


# synthesizer_compressed.save_interval(440, 1, "../audio/compressed_timbre_unison.wav")
# synthesizer_stretched.save_interval(440, 1, "../audio/stretched_timbre_unison.wav")
#
# synthesizer_compressed.save_interval(440, 1.75, "../audio/compressed_timbre_virt_octave.wav")
# synthesizer_stretched.save_interval(440, 2.25, "../audio/stretched_timbre_virt_octave.wav")
#
# synthesizer_compressed.save_interval(440, 1.75, "../audio/compressed_timbre_true_octave.wav")
# synthesizer_stretched.save_interval(440, 2.25, "../audio/stretched_timbre_true_octave.wav")
