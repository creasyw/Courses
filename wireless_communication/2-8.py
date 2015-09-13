import numpy as np
from math import pi, log10
import matplotlib.pyplot as plt


def log(num):
    result = np.zeros(len(num))
    for i in range(len(num)):
        result[i] = log10(num[i])
    return result


def main():
    ht = 50
    hr = 2
    f = 900 * 10**6
    c = 3 * 10**8
    gr = [1, 0.316, 0.1, 0.01]
    gl = 1
    r = -1

    distance = np.arange(1, 100001, 1, dtype=float)
    lambd = c / float(f)
    dc = 4 * ht * hr / lambd
    reflect = (distance**2 + (ht + hr)**2)**0.5
    los = (distance**2 + (ht - hr)**2)**0.5
    phi = 2 * pi * (reflect - los) / lambd
    flat = distance[:ht]
    decline = distance[ht:(dc + 1)]
    steep = distance[dc:]

    for i in range(len(gr)):
        temp = gl**0.5 / los + r * (gr[i]**0.5) * np.exp(phi * -1J) / reflect
        pr = (lambd / 4 / pi)**2 * (abs(temp)**2)
        plt.subplot(220 + i + 1)
        plt.plot(10*log(distance),10*log(pr)-10*log10(pr[0]),'b', \
                10*log(flat), np.zeros(len(flat)), 'y', \
                10*log(decline),-20*log(decline),'g', 10*log(steep),-40*log(steep),'r')
        plt.axvline(x=10 * log10(ht), linestyle='-.')
        plt.axvline(x=10 * log10(dc), linestyle='-.')
        plt.title("Gr = %s" % gr[i])

    plt.show()


if __name__ == "__main__":
    main()
