"""

    synthmodule.py

    Module to synthesize timbres using synth package
    https://pypi.org/project/synthesizer/


"""

import numpy as np

import synthesizer as synth

class synthesizer:

    def __init__(self, instrument):
        """Construct a synthesizer object for Instrument instance instrument"""
        self.instrument = instrument

        # Synthesizer stuff
        self.player = synth.Player()
        self.player.open_stream()

        self.writer = synth.Writer()

        self.synth = synth.Synthesizer()

    def play_interval(self, f0, alpha, filename , duration = 3.0):
        """Play instrument at interval alpha, save to file as filename

        Args:
         * f0: Fundamental frequency to play instrument at
         * alpha: Frequency ratio. Instrument played at frequencies f0
                  and alpha*f0
         * filename: File path to save recording as. Should be .wav.
         * duration: Time to play note for. Default 3 seconds
        """

        # Timbre instances to play
        sound1 = self.instrument(f0)
        sound2 = self.instrument(f0 * alpha)

        # Join together all frequencies into one list
        waves = list(np.concatenate((sound1.F, sound2.F)))

        sound = self.synth.generate_chord(waves, duration)

        self.writer.write_wave(filename, sound)

if __name__ == "__main__":
    ## Testing / example usage
    from model import timbre

    inst = timbre.Instrument((1, 2, 3, 4, 5), (1, 1, 1, 1, 1))
    synth = synthesizer(inst)

    synth.play_interval(440, 2.**(7./12.), "../audio/harmonic_fifth_ET.wav", duration = 5.0)
