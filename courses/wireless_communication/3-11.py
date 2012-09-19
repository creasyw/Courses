from math import pi, cos, sin, log10
from random import uniform
import numpy as np
import matplotlib.pyplot as plt

def log(num):
    """Calculate the log10() for list"""
    result = np.zeros(len(num))
    for i in range(len(num)):
        result[i] = log10(num[i])
    return result

# Referring to the algorightm generating Rayleigh fading in Wikipedia, which is
# based on summing sinusoids (http://en.wikipedia.org/wiki/Rayleigh_fading#Jakes.27_model)
def jakes_model (fd, N):
    """
    Simulate the Rayleigh fading channel via Jakes' Model
    Input: fd--maximum doppler frequency, N--array of the sample points
    Output: the amplitude of the Rayleigh fading channel
    """
    # Assume there are 10 multipath transmisson
    M = 7
    # Generate the uniformly distributed angles for the transmissions"
    alpha = [uniform(0,2*pi) for k in range(M)]
    beta = [uniform(0,2*pi) for k in range(M)]
    theta = [uniform(0,2*pi) for k in range(M)]
    fn = [fd*cos(((2.*k+1)*pi+alpha[k])/(4*M)) for k in range(M)]
    r = np.zeros(len(N))
    for i in range(len(N)):
        # the in-phase amplitude of the PSD
        r_i = 1/(M**0.5)*sum([cos(2*pi*fn[k]*N[i]+theta[k]) for k in range(M)])
        # the quadrature amplitude of the PSD
        r_q = 1/(M**0.5)*sum([sin(2*pi*fn[k]*N[i]+beta[k]) for k in range(M)])
        # the amplitude of the channel
        r[i] = (r_i**2+r_q**2)**0.5
    return r

def main():
    # prerequisite of the question
    fd = [1,10,100]
    Ts = 1./1000
    # set the amount of sample in the plot
    Sample = np.arange(0,3000,1)
    T = Sample*Ts
    # calculate and plot
    for i in range(3):
        r = jakes_model(fd[i],T)
        plt.subplot(311+i)
        plt.subplots_adjust(hspace=0.8)
        plt.plot(T, 10*log(r))
        plt.title("Doppler Frequency fd=%sHz"%fd[i])
        plt.xlabel("Time (second)")
        plt.ylabel("Amplitude (dB)")
    plt.show()

if __name__ == "__main__":
    main()

