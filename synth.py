"""

    synth.py

    Script to play with python synthesizer package
    https://pypi.org/project/synthesizer/

"""

import numpy as np

import synthesizer as synth

import timbre

HarmonicInst = timbre.Instrument((1, 2, 3, 4, 5), [1, 1, 1, 1, 1])

AharmInst = timbre.Instrument((1, np.sqrt(2), np.sqrt(5), np.sqrt(7), 1017./313.), (1, 1, 1, 1, 1))

player = synth.Player()
player.open_stream()

writer = synth.Writer()

sy = synth.Synthesizer()

f01 = 220.
f02 = 440.

H1 = HarmonicInst(f01)
H2 = HarmonicInst(f02)

A1 = AharmInst(f01)
A2 = AharmInst(f02)

print(np.concatenate((A1.F, A2.F)))

print(np.concatenate((H1.F, H2.F)))

harmwave = sy.generate_chord(list(np.concatenate((H1.F, H2.F))), 3.0)
player.play_wave(harmwave)
writer.write_wave("harmonic.wav", harmwave)

# aharmchord = [440., 440.*817/411]
aharmwave = sy.generate_chord(list(np.concatenate((A1.F, A2.F))), 3.0)
player.play_wave(aharmwave)
writer.write_wave("anharmonic.wav", aharmwave)
