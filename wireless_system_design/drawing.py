import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('score.csv')

plt.hist(data, bins=50)
ax = plt.gca()
plt.xlim(ax.get_xlim()[::-1])
plt.ylim(0, int(max(ax.get_ylim()))+1)
plt.xlabel("Grade", fontsize=15)
plt.ylabel("Number of Students", fontsize=15)
plt.savefig("score_distr.pdf", format='pdf')



