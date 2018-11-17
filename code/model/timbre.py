"""

    timbre.py

    Python module containing Instrument and Timbre classes.

    An Instrument instance stores the frequency ratios the instrument always
    produces; a Timbre instance stores the absolute frequencies present
    when an Instrument is played at a given fundamental frequency.

    See examples at bottom of module

"""

import numpy as np

class Instrument:
    """Instrument represents the partials of a simulated instrument.

    Constructor Arguments:
     * A: List of frequency ratios present. Float or iterable.
     * V: Relative amplitudes of each frequency ratio. Float or iterable.

    Optional Arguments:
     * name: Name of the instrument for pretty printing

    Methods:
     * __call__: Allows calling instance as a function. Returns a Timbre
                    instance corresponding to the instrument at the given
                    fundamental frequency.
    """
    def __init__(self, A, V, name = ''):
        """Instrument constructor.

        A is (float or list of) frequency ratios present.
        V is (float or list of) relative frequency amplitudes.

        For example, if A = (1, 2, 3, 4) and V = (1, 0.5, 0.25, 0.125),
        the instrument has the first 4 harmonics present at relative amplitudes
        each 1/2 of the previous partial.
        """
        A = np.array(A)
        V = np.array(V)

        self.A = A
        self.V = V
        self.name = name if name else 'Instrument'

    def __call__(self, f0):
        """All calling of instrument instance as a function.

        Returns a Timbre instance with fundamental frequency f0. Partials
        are computed as f0 * alpha_i for each frequncy ratio alpha_i of the
        instrument.
        """
        return Timbre(f0 * self.A, self.V, name = '%s (%s)' % (self.name, f0))

    def __repr__(self):
        Alist = ", ".join([str(a) for a in self.A])
        Vlist = ", ".join([str(v) for v in self.V])
        return "Timbre((%s), (%s), %s)" % (Alist, Vlist, self.name)

    def __str__(self):
        Alist = ", ".join([str(a) for a in self.A])
        Vlist = ", ".join([str(v) for v in self.V])
        return "%s: (%s), (%s)" % (self.name, Alist, Vlist)

class Timbre:
    """Timbre represents the frequency components present in a given note.
    """
    def __init__(self, F, V, name = ''):
        F = np.array(F)
        V = np.array(V)

        self.F = F
        self.V = V

        self.name = name if name else 'Timbre'

    def __iter__(self):
        for (f, v) in zip (self.F, self.V):
            return (f, v)

    def __repr__(self):
        Flist = ", ".join([str(f) for f in self.F])
        Vlist = ", ".join([str(v) for v in self.V])
        return "Timbre((%s), (%s), %s)" % (Flist, Vlist, name)

    def __str__(self):
        Flist = ", ".join([str(f) for f in self.F])
        Vlist = ", ".join([str(v) for v in self.V])
        return "%s: (%s), (%s)" % (self.name, Flist, Vlist)

if __name__ == '__main__':
    # Create an instrument with 6 harmonic partials
    harmonic = Instrument((1, 2, 3, 4, 5), (1, 0.5, 0.25, 0.125, 0.125/2), 'Harmonic')

    # Print string representation of instance
    print(harmonic)

    # Calling instrument with a frequency returns a Timbre instance, storing
    #  the absolute frequencies that will be present in the note
    print(harmonic(440))
