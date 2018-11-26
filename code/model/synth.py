"""

    synthmodule.py

    Module to synthesize timbres using synth package
    https://pypi.org/project/synthesizer/

    Class synthesizer represents a virtual instrument.

    Synthesizer instances are constructed from an Instrument instance.
    Method save_interval saves an interval (or intervals) to an audio file,
    and method play_interval plays an interval(s) at run time.


"""

import numpy as np

import synthesizer as synth

class synthesizer:

    def __init__(self, instrument):
        """Construct a synthesizer object for Instrument instance instrument.

        Instrument object is used to compute frequency components based on
        a given fundamental frequency."""
        self.instrument = instrument

        # Synthesizer stuff
        self.player = synth.Player()
        self.player.open_stream()

        self.writer = synth.Writer()

        self.synth = synth.Synthesizer()

        self.synth.waveform = 'sine'

    def save_interval(self, f0, alpha, filename , duration = 3.0):
        """Play instrument at interval alpha, save to file as filename

        Args:
         * f0: Fundamental frequency to play instrument at
         * alpha: Frequency ratio. Instrument played at frequencies f0
                  and alpha*f0. Can be list or scalar. If list, will
                  be played at each interval consecutively.
         * filename: File path to save recording as. Should be .wav.
         * duration: Time to play note for. Default 3 seconds. Can be scalar
                or list of same length as alpha.
        """
        if not hasattr(alpha, '__iter__'):
            alpha = [alpha]
        fund_inst = self.instrument(f0)
        insts = [self.instrument(f0*a) for a in alpha]
        sounds = []
        for j,inst in enumerate(insts):
            waves = list(np.concatenate((fund_inst.F, inst.F)))

            if hasattr(duration, '__iter__'):
                sound = self.synth.generate_chord(waves, duration[j])

            else:
                sound = self.synth.generate_chord(waves, duration)
            sounds.append((sound))

        self.writer.write_waves(filename, *sounds)

    def play_interval(self, f0, alpha, duration = 3.0):
        """Play instrument at interval alpha.

        Args:
         * f0: Fundamental frequency to play instrument at
         * alpha: Frequency ratio. Instrument played at frequencies f0
                  and alpha*f0. Can be list or scalar. If list, will
                  be played at each interval consecutively.
         * filename: File path to save recording as. Should be .wav.
         * duration: Time to play note for. Default 3 seconds. Can be scalar
                or list of same length as alpha
        """
        if not hasattr(alpha, '__iter__'):
            alpha = [alpha]
        finst = self.instrument(f0)
        insts = [self.instrument(f0*a) for a in alpha]
        for j,inst in enumerate(insts):
            waves = list(np.concatenate((finst.F, inst.F)))
            if hasattr(duration, '__iter__'):
                sound = self.synth.generate_chord(waves, duration[j])
            else:
                sound = self.synth.generate_chord(waves.duration)

            self.player.play_wave(sound)

if __name__ == "__main__":
    ## Testing / example usage
    from model import timbre

    inst = timbre.Instrument((1, 2, 3, 4, 5), (1, 1, 1, 1, 1))
    synth = synthesizer(inst)

    synth.play_interval(440, 2.**(7./12.), "../audio/harmonic_fifth_ET.wav", duration = 5.0)
