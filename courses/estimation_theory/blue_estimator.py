import numpy as np
from numpy import dot
from numpy.linalg import inv
import matplotlib.pyplot as plt

def source_localization(xn, yn, loc, noise_power):
    """input: loc -- array of locations of sensors"""
    xs = 10
    ys = 20

    def trigonometric(xi, yi):
        rn = ((xn-xi)**2+(yn-yi)**2)**0.5
        return (xn-xi)/rn, (yn-yi)/rn
    
    angle = np.array([list(trigonometric(i[0],i[1])) for i in loc])
    
    c = 3*10**8
    N = len(loc)
    A = np.zeros((N-1, N))
    H = np.zeros((N-1, 2))
    noise = np.random.normal(0, noise_power**0.5, N)
    Ep = np.zeros((N-1, 1))
    for i in range(N-1):
        A[i,i] = -1
        A[i,i+1] = 1
        H[i,0] = (angle[i+1,0]-angle[i,0])/c
        H[i,1] = (angle[i+1,1]-angle[i,1])/c
        Ep[i] = H[i,0]*(xs-xn)+H[i,1]*(ys-yn)+noise[i+1]-noise[i]
    C = noise_power*dot(A, A.T)
    return dot(dot(dot(inv(dot(dot(H.T,inv(C)),H)),H.T),inv(C)),Ep).flatten()


def generate_sensor(num, upper):
    return np.random.random(size=(num, 2))*upper

def main():
    xn = 10
    yn = 10
    nvar = 0.01
    high_snr = []
    for N in range(3,31):
        estimation = np.zeros((100,2))
        for run in range(100):
            loc = generate_sensor(N, 25)
            estimation[run] = source_localization(xn, yn, loc, nvar)
        mean = np.mean(estimation,0)
        high_snr.append(((mean[0]-10)**2+(mean[1]-20)**2)**0.5)
    low_snr = []
    for N in range(3,31):
        estimation = np.zeros((100,2))
        for run in range(100):
            loc = generate_sensor(N, 25)
            estimation[run] = source_localization(xn, yn, loc, nvar)
        mean = np.mean(estimation,0)
        low_snr.append(((mean[0]-10)**2+(mean[1]-20)**2)**0.5)
    plt.plot(high_snr)
    plt.plot(low_snr)
    plt.show()

if __name__=="__main__":
    main()
