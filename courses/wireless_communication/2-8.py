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
    hr = 15
    f = 900*10**6
    c = 3*10**8
    gr = [1, 0.316, 0.1, 0.01]
    gl = 1
    r = -1
    
    distance = np.arange(1,100001,1,dtype=float)
    lambd = c/float(f)
    dc = 4*ht*hr/lambd
    reflect = (distance**2+(ht+hr)**2)**0.5
    los = (distance**2+(ht-hr)**2)**0.5
    phi = 2*pi*(reflect-los)/lambd
    dright = distance[int(dc)-1:]

    for i in range(len(gr)):
        temp = gl/los+r*gr[i]*np.exp(phi*-1J)/reflect
        pr = (lambd/4/pi)**2*(abs(temp)**2)
        plt.subplot(220+i+1)
        plt.plot(10*log(distance),10*log(pr),'b', 10*log(dright),-20*log(dright),'g', 10*log(dright),-40*log(dright),'r')
        plt.title("Gr = %s"%gr[i])

    plt.show()

if __name__ == "__main__":
    main()

