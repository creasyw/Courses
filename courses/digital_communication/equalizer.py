import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats.distributions import norm

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
    index = np.zeros((nzf+len(tap)-1, nzf), dtype=float)
    q = np.zeros(nzf+len(tap)-1, dtype=float)
    q[nzf/2] = 1
    fz = tap

    for n in range(len(index)):
        for j in range(n, n-3, -1):
            if j<0 or j>=nzf: continue
            index[n, j] = fz[n-j]
    coeff,_,_,_ =  np.linalg.lstsq(index, q)
    return coeff

def lmmse_coeff(fz, nzf, snr):
    r = np.zeros((nzf, nzf), dtype=float)
    for l in range(nzf):
        r[l, l] = 10**(-snr/10.)
        for j in range(nzf):
            for n in range(len(fz)):
                if 0<n+l-j<len(fz): r[l,j] += np.conjugate(fz[n])*fz[n+l-j]
    
    upsilon = np.zeros(nzf, dtype=float)
    zero = nzf/2
    upsilon[zero-len(fz)+1:zero+1] = np.conjugate(fz)[::-1]
    return [sum(k) for k in np.linalg.inv(r)*upsilon]

def dfe_coeff(tap, k1, k2, snr):
    # For feed-forward loop
    r = np.zeros((k1, k1), dtype=float)
    for l in range(k1):
        r[l, l] = 10**(-snr/10.)
        for j in range(k1):
            for n in range(len(tap)):
                if 0<n+l-j<len(tap): r[l,j] += np.conjugate(tap[n])*tap[n+l-j]
    upsilon = np.zeros(k1, dtype=float)
    zero = k1/2
    upsilon[zero-len(tap)+1:zero+1] = np.conjugate(tap)[::-1]
    cj = [sum(k) for k in np.linalg.inv(r)*upsilon]
    # For feed-back loop
    temp = cj[::-1]
    ck = np.zeros(k2, dtype=float)
    for i in range(k2):
        for j in range(k1):
            if 0<=i+j<len(tap):
                ck[i] -= temp[j]*tap[i+j]
    return cj, ck

def dfe_estimate(vn, cj, ck):
    decision = np.zeros(len(vn), dtype=float)
    forward = np.convolve(vn, cj, mode='same')
    fdec = np.array(map(lambda x: -1 if x<0 else 1, forward))
    backward = np.convolve(fdec, ck, mode='same')
    return np.array(map(lambda x: -1 if x<0 else 1, backward+forward))

def equalizer(nchannel, nzf, snrlst, nsample, eqtype):
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
        if eqtype == "zfir":
            coeff = zero_forcing_coeff(tap, nzf)
        elif eqtype == "lmmse":
            coeff = lmmse_coeff(tap, nzf, snr)
        elif eqtype == "dfe":
            cj, ck = dfe_coeff(tap, nzf, 41, snr)
        else:
            raise ValueError("The type of equalizer should be 'zf' (zero-forcing) or\
                    lmmse (Linear Minimumu MSE)!")
        
        if eqtype != "dfe":
            estimate = np.array(map(lambda x: -1 if x<0 else 1, np.convolve(vn, coeff, mode='same')))
        elif eqtype == "dfe":
            estimate = dfe_estimate(vn, cj, ck)

        ser.append(sum(1 for i in range(nsample) if samples[i]!=estimate[i])/float(nsample))
    return ser

def plotzf():
    """ Test Simulation 1-1 
        Plot simulatied zero forcing equalizer with different taps"""
    nsample = 10**5
    snr = range(0,19)
    taps = [13,23,33]
    
    fig1 = plt.figure()
    plt.semilogy(snr, equalizer(2, 13, snr, nsample, 'zfir'),\
            snr, equalizer(2, 23, snr, nsample, 'zfir'), "--", \
            snr, equalizer(2, 33, snr, nsample, 'zfir'), "-.")
    plt.legend(("13 taps", "23 taps", "33 taps"), loc='upper right')
    plt.title("Zero Forcing with different taps")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()

def plotzfe():
    """ Test Simulation 1-2
        Plot theoretical vs. simulated results for zero forcing equalizer."""
    nsample = 10**5
    snrlst = range(0,19)

    pe = []
    coeff = zero_forcing_coeff(tap2, 41)
    for snr in snrlst:
        delta_square = 10**(-snr/10.)*sum(coeff**2)
        pe.append(1-norm.cdf(sqrt((1-0.41)**2/delta_square)))
    plt.semilogy(snrlst, pe,\
            snrlst, equalizer(2, 41, snrlst, nsample, 'zfir'), "-.")
    
    plt.legend(("Theoretical curve", "41 taps simulation"), loc='lower left')
    plt.title("Theoretical vs. Simulated performances")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()

def plotlmmse():
    nsample = 10**5
    snrlst = range(0,19)
    
    plt.subplot(211)
    pe = []
    coeff = zero_forcing_coeff(tap1, 41)
    for snr in snrlst:
        delta_square = 10**(-snr/10.)*sum(coeff**2)
        pe.append(1-norm.cdf(sqrt((1-0.7)**2/delta_square)))
    plt.semilogy(snrlst,pe,snrlst, equalizer(2, 41, snrlst, nsample, 'lmmse'), "-.")
    plt.legend(("Theoretical curve", "Simulated curve"), loc='lower left')
    plt.title("Theoretical vs. Simulated performances for Channel 1")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')

    plt.subplot(212)
    pe = []
    coeff = zero_forcing_coeff(tap2, 41)
    for snr in snrlst:
        delta_square = 10**(-snr/10.)*sum(coeff**2)
        pe.append(1-norm.cdf(sqrt((1-0.41)**2/delta_square)))
    plt.semilogy(snrlst,pe,snrlst, equalizer(2, 41, snrlst, nsample, 'lmmse'), "-.")
    plt.legend(("Theoretical curve", "Simulated curve"), loc='lower left')
    plt.title("Theoretical vs. Simulated performances for Channel 2")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()




if __name__=="__main__":
    #plotzf()
    #plotzfe()
    #plotlmmse()
