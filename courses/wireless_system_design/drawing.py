import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('score.csv')

plt.hist(data, bins=50)
ax = plt.gca()
plt.xlim(ax.get_xlim()[::-1])
plt.show()



