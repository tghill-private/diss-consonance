"""

    script to plot a plomp-levelt dissonance curve

"""

import numpy as np
from matplotlib import pyplot as plt

# CONSTANTS
a = 3.5
b = 5.75

f0 = np.array([[440], [880], [440*4]])

alpha = np.linspace(1., 2., 1000)
d = np.exp(-a * ((alpha-1))) - np.exp(-b * ((alpha-1)))
# d /= d.max()

fig, ax = plt.subplots()

ax.plot(alpha, d)
ax.set_ylabel('Perceived dissonance')
ax.set_xlabel('Interval')
ax.grid()

fig.savefig('../figs/plomplevelt.png', dpi = 400)
