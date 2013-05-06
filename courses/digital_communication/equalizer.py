import numpy as np
from math import sqrt

tap1 = np.array([0.227, 0.45, 0.7, 0.45, 0.227])
tap2 = np.array([0.41, 0.815, 0.41])

def awgn(nsample, nvar):
    return np.random.normal(loc=0, scale=sqrt(nvar), size=nsample)

def binary_pam(nsample):
    return np.array(map(lambda x: -1 if x==0 else x, np.random.randint(2, size=nsample)))

def channel(signal, tap):
    L = len(signal)
    noise = awgn(L)
    output = np.zeros(L)
    for n in range(L):
        output[n] += noise[n]
        for k in range(len(tap)):
            if n-k >= 0: output[n] += tap[k]*signal[n-k]
    return output

def zero_forcing(nchannel, nsample, nzf, snr):
    if nchannel == 1:
        tap = tap1
    elif nchannel == 2:
        tap = tap2
    else:
        raise ValueError("The channel shoudl be either 1 or 2!")
    
    index = np.zeros((nzf, nzf), dtype=float)
    q = np.zeros(nzf, dtype=float)
    q[nzf/2+1] = 1

    for n in range(len(index)):
        for j in range(n, n-3, -1):
            if j<0 or j>=nzf: continue
            index[n, j] = tap[n-j]
    print np.linalg.solve(index, q)


