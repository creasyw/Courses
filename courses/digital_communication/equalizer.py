import numpy as np
from math import sqrt

tap1 = np.array([0.227, 0.45, 0.7, 0.45, 0.227])
tap2 = np.array([0.41, 0.815, 0.41])

def awgn(nsample, nvar):
    return np.random.normal(loc=0, scale=sqrt(nvar), size=nsample)

def binary_pam(nsample):
    return np.array(map(lambda x: -1 if x==0 else x, np.random.randint(2, size=nsample)))

def channel(signal, tap, snr):
    L = len(signal)
    output = awgn(L, 10**(-snr/10.))
    for n in range(L):
        for k in range(len(tap)):
            if n-k >= 0: output[n] += tap[k]*signal[n-k]
    return output

def zero_forcing_coeff(tap, nzf):
    index = np.zeros((nzf+len(tap), nzf), dtype=float)
    q = np.zeros(nzf+len(tap), dtype=float)
    q[nzf/2] = 1
    fz = np.fft.fft(tap)

    for n in range(len(index)):
        for j in range(n, n-3, -1):
            if j<0 or j>=nzf: continue
            index[n, j] = fz[n-j]
    #index = np.vstack((index[:nzf/2], index[nzf/2+1:]))
    coeff,_,_,_ =  np.linalg.lstsq(index, q)
    return np.fft.ifft(coeff)

def zero_forcing_eq(nchannel, nzf, snrlst, nsample):
    if nchannel == 1:
        tap = tap1
    elif nchannel == 2:
        tap = tap2
    else:
        raise ValueError("The channel shoudl be either 1 or 2!")
    
    ser = []
    for snr in snrlst:
        samples = binary_pam(nsample)
        vn = channel(samples, tap, snr)
        coeff = zero_forcing_coeff(tap, nzf)
        estimate = np.array(map(lambda x: -1 if x<0 else 1, np.convolve(vn, coeff)[:nsample]))
        ser = append(sum(1 for i in range(nsample) if samples[i]!=estimate[i])/float(nsample))
    return ser



def lmmse_coeff(tap, nzf, snr):
    fz = np.fft.fft(tap)

    r = np.ones((nzf, nzf), dtype=float)*10**(-snr/10.)
    for l in range(nzf):
        for j in range(nzf):
            for n in range(len(tap)):
                if 0<n+l-j<len(tap): r[l,j] += np.conjugate(fz[n])*fz[n+l-j]
    
    upsilon = np.zeros(nzf, dtype=complex)
    zero = nzf/2+1
    upsilon[zero-len(tap)+1:zero+1] = np.conjugate(fz)[::-1]

    c = np.fft.ifft(np.linalg.inv(r)*upsilon)
    print abs(c)


