import numpy as np
from math import cos, sin, pi, log

def signal_generation(Es):
    """
    Generating received signal from 8-PSK modulation.
    Assuming that the input signal is uniformly random distributed.
    Besides, the length of signal is also given and hard-coded.
    The input variable is the energy of the signal.
    """
    size = 3*10**5
    low = 1; high = 9

    rint = np.random.randint(low, high, size)
    signal = np.zeros((size, 2))
    # Mapping, regardless of the grey coding
    signal[:,0] = map(lambda m: (Es)**0.5*cos(2*pi*m/8), rint)
    signal[:,1] = map(lambda m: (Es)**0.5*sin(2*pi*m/8), rint)
    return signal

def transfer_in_channel (signal, Es, snr):
    """
    The only input variable is the SNR value in LINEAR unit.
    """
    # Generate Gaussian noise with certain constraints
    awgn = np.random.normal(loc=0.0, scale=(Es/log(3,2)/snr/2)**0.5, size=len(signal))
    noise = (np.vstack((awgn, awgn))).T
    return signal+noise




