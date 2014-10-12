import matplotlib.pyplot as plt
import numpy as np
from math import e

x = np.arange(-5, 5, 0.01)
h = lambda x: 1/(1+e**(-x))

plt.figure(1)
plt.plot(x, h(x))

plt.figure(2)
plt.plot(h(x), -np.log(h(x)))

plt.figure(3)
plt.plot(h(x), -np.log(1-h(x)))

plt.show()
