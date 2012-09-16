import numpy as np
from math import e, log10, exp
from scipy.stats.distributions import norm
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def main():
    gamma = np.arange(2, 6.01, 0.01)
    delta = np.arange(4, 12.01, 0.01)
    c = np.zeros((len(gamma), len(delta)))

    # Calculate the expectation for coverage area
    for i in range(len(gamma)):
        for j in range(len(delta)):
            b = 10*gamma[i]*log10(e)/delta[j]
            c[i,j] = 0.5+exp(1/b**2)*norm.cdf(-2/b)
    print np.max(c), np.min(c)
    
    # Plotting
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(delta, gamma)
    surf = ax.plot_surface(X, Y, c, rstride=5, cstride=5, cmap=cm.jet, linewidth=1, antialiased=True)
    ax.set_zlim3d(np.min(c), np.max(c))
    ax.set_xlabel('delta')
    ax.set_ylabel('gamma')
    ax.set_zlabel('coverage')
    fig.colorbar(surf)
    plt.show()

if __name__ == "__main__":
    main()
