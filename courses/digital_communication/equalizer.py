import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats.distributions import norm
# for viterbi enumerating possible combinations
from itertools import product

tap1 = np.array([0.227, 0.45, 0.7, 0.45, 0.227])
tap2 = np.array([0.41, 0.815, 0.41])

def awgn(nsample, nvar):
    """
    Generate noise with standard normal distribution.
    nsample: the length of noise
    nvar: N0, the variance of the noise.
    """
    return np.random.normal(loc=0, scale=sqrt(nvar), size=nsample)

def binary_pam(nsample):
    """ Generate PAM symbols with equal probability. """
    return np.array(map(lambda x: -1 if x==0 else x, np.random.randint(2, size=nsample)))

# 1st version of signal generation
#def channel(signal, tap, snr):
#    """ Construct the effect of ISI and AWGN. """
#    L = len(signal)
#    output = awgn(L, 10**(-snr/10.))
#    output = np.zeros(L, dtype=float)
#    for n in range(L):
#        for k in range(len(tap)):
#            if n-k >= 0: output[n] += tap[k]*signal[n-k]
#    return output

def channel(signal, tap, snr):
    """ Construct the effect of ISI and AWGN. """
    L = len(tap)
    output = awgn(len(signal), 10**(-snr/10.))
    for n in range(len(signal)):
        if n < L-1:
            current_in_loop = np.array([0]*(L-n-1)+list(signal[:(n+1)]))
        else:
            current_in_loop = (signal[:(n+1)])[-L:]
        output[n] += sum(current_in_loop*(tap[::-1]))
    return output

def zero_forcing_coeff(tap, nzf):
    """ Calculate the coefficients for zero forcing equalizer """
    index = np.zeros((nzf+len(tap)-1, nzf), dtype=float)
    q = np.zeros(nzf+len(tap)-1, dtype=float)
    q[nzf/2] = 1
    fz = tap
    # Construct the index array for coefficients
    for n in range(len(index)):
        for j in range(n, n-3, -1):
            if j<0 or j>=nzf: continue
            index[n, j] = fz[n-j]
    # Solve the linear function using least square linear solver
    coeff,_,_,_ =  np.linalg.lstsq(index, q)
    return coeff

def lmmse_coeff(fz, nzf, snr):
    """ Calculate the coefficients for Linear Minimum MSE equalizer """
    r = np.zeros((nzf, nzf), dtype=float)
    for l in range(nzf):
        # adding noise to the diagnal elements
        r[l, l] = 10**(-snr/10.)
        for j in range(nzf):
            for n in range(len(fz)):
                if 0<n+l-j<len(fz): r[l,j] += np.conjugate(fz[n])*fz[n+l-j]
    # Construct the upsilon and flip it
    upsilon = np.zeros(nzf, dtype=float)
    zero = nzf/2
    upsilon[zero-len(fz)+1:zero+1] = np.conjugate(fz)[::-1]
    return np.array([sum(k) for k in np.linalg.inv(r)*upsilon])

def dfe_coeff(tap, k1, k2, snr):
    """ Calculate the coefficients for Decision Feedback equalizer """
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
    """ Combine the forward and backward estimates together. """
    decision = np.zeros(len(vn), dtype=float)
    forward = np.convolve(vn, cj, mode='same')
    fdec = np.array(map(lambda x: -1 if x<0 else 1, forward))
    backward = np.convolve(fdec, ck, mode='same')
    return np.array(map(lambda x: -1 if x<0 else 1, backward+forward))

def viterbi_function(signal, taps, k, values, known):
    """
    Perform Viterbi decoding.
    taps:   the channel taps. (numpy.ndarray)
    k:      the index that needs to decode. (int)
    values: the possible decoded values. (list)
    known:  the constellations that have already been settled down. (list)
    """
    L = len(taps)
    result = 0
    minimum = float("inf")
    for unknown in product(values, repeat=len(taps)):
        current = known+list(unknown)
        unknown  = np.array(unknown)
        temp = unknown[0]
        if k+L > len(signal):
            # im not sure if the unknow*tap should be added here, though it doesnt matter...
            summation = 0
        else:
            summation = (signal[k+L-1] - sum(unknown*(taps[::-1])))**2
        for i in range(L+k-1):
            # won't look beyond the scope of signal
            if i >= len(signal): continue
            current_in_loop = current[:(i+1)]
            # extend zeros before the unknow values
            if len(current_in_loop) < L:
                current_in_loop = np.array([0]*(L-len(current_in_loop))+current_in_loop)
            else:
                current_in_loop = np.array(current_in_loop[-L:])
            summation += (signal[i] - sum(current_in_loop*(taps[::-1])))**2
        if summation < minimum:
            result = temp
            minimum = summation

    return result

def viterbi(signal, taps):
    result = []
    values = [-1,1]
    for i in range(len(signal)):
        result.append(viterbi_function(signal, taps, i, values, result))

    return result

def equalizer(nchannel, nzf, snrlst, nsample, eqtype):
    """
    Generate SER for given channel and snr.
    nchannel: the channel index. 1 or 2
    nzf: the number of taps that equalizer has
    snrlst: the list of snr values in dB
    nsample: the length of signal
    eqtype: the type flag for different kinds of equalizers
    """
    if nchannel == 1:
        tap = tap1
    elif nchannel == 2:
        tap = tap2
    else:
        raise ValueError("The channel shoudl be either 1 or 2!")
    
    ser = np.zeros(len(snrlst), dtype=float)
    for i in range(len(snrlst)):
        snr = snrlst[i]
        samples = binary_pam(nsample)
        vn = channel(samples, tap, snr)
        if eqtype == "zfir":
            coeff = zero_forcing_coeff(tap, nzf)
        elif eqtype == "lmmse":
            coeff = lmmse_coeff(tap, nzf, snr)
        elif eqtype == "dfe":
            cj, ck = dfe_coeff(tap, nzf, 41, snr)
        elif eqtype == "viterbi":
            estimate = viterbi(vn, tap)
        else:
            raise ValueError("The type of equalizer should be 'zf' (zero-forcing) or\
                    lmmse (Linear Minimumu MSE)!")
        
        if eqtype != "dfe" and eqtype != "viterbi":
            estimate = np.array(map(lambda x: -1 if x<0 else 1, np.convolve(vn, coeff, mode='same')))
        elif eqtype == "dfe":
            estimate = dfe_estimate(vn, cj, ck)
        
        # Compare teh estimates with the original sequence
        ser[i] = sum(1 for i in range(nsample) if samples[i]!=estimate[i])/float(nsample)
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

    # Calculate the theoretical values
    pe = []
    coeff = zero_forcing_coeff(tap2, 41)
    for snr in snrlst:
        delta_square = 10**(-snr/10.)*sum(coeff**2)
        pe.append(1-norm.cdf(sqrt((1-0.41)**2/delta_square)))
    
    plt.semilogy(snrlst,pe,snrlst,equalizer(2,41,snrlst,nsample,'zfir'),"-.")
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
    for snr in snrlst:
        coeff = lmmse_coeff(tap1, 41, snr)
        delta_square = 10**(-snr/10.)*sum(coeff**2)
        pe.append(1-norm.cdf(sqrt((1-0.7)**2/delta_square)))
    plt.semilogy(snrlst,pe,snrlst,equalizer(2,41,snrlst,nsample,'lmmse'),"-.")
    plt.legend(("Theoretical curve", "Simulated curve"), loc='lower left')
    plt.title("Theoretical vs. Simulated performances for Channel 1")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')

    plt.subplot(212)
    pe = []
    for snr in snrlst:
        coeff = lmmse_coeff(tap2, 41, snr)
        delta_square = 10**(-snr/10.)*sum(coeff**2)
        pe.append(1-norm.cdf(sqrt((1-0.41)**2/delta_square)))
    plt.semilogy(snrlst,pe,snrlst, equalizer(2, 41, snrlst, nsample, 'lmmse'), "-.")
    plt.legend(("Theoretical curve", "Simulated curve"), loc='lower left')
    plt.title("Theoretical vs. Simulated performances for Channel 2")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()

def plotdfe1():
    nsample = 10**5
    snrlst = range(0,19)
    nzf = 41
    tap = tap2
    
    plt.semilogy(snrlst, equalizer(2, 41, snrlst, nsample, 'dfe'), \
            snrlst, equalizer(2, 61, snrlst, nsample, 'zfir'), "-.",\
            snrlst, equalizer(2, 41, snrlst, nsample, 'zfir'), "--")
    plt.legend(("MMSE-DF", "Zero-Forcing", "LMMSE"), loc='lower left')
    plt.title("Corss comparison of three equalizers")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()

def plotdfe2():
    nsample = 10**5
    snrlst = range(0,19)
    nzf = 41
    tap = tap2
    
    pe = []
    for snr in snrlst:
        cj,_ = dfe_coeff(tap, nzf, 41, snr)
        f = [0]*(len(cj)-len(tap)) + list(tap)[::-1]
        jmin = 1-sum(np.array(f)*cj)
        gamma = (1-jmin)/jmin
        pe.append(1-norm.cdf(sqrt(gamma)))
    plt.semilogy(snrlst,pe,snrlst, equalizer(2, 41, snrlst, nsample, 'dfe'), "-.")
    plt.legend(("Theoretical curve", "Simulated curve"), loc='lower left')
    plt.title("Theoretical vs. Simulated performances for Channel 1")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()

def plotviterbi_1():
    nsample = 10**5
    snrlst = range(0,19)
    nzf = 41
    tap = tap2
    
    plt.semilogy(snrlst,equalizer(2, 10, snrlst, nsample, 'viterbi'),\
            snrlst, equalizer(2, 41, snrlst, nsample, 'dfe'), "-.")
    plt.legend(("ML viterbi", "MLSE-MF"), loc='lower left')
    plt.title("ML Viterbi vs. MLSE-MF performances comparison")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()

def plotviterbi_2():
    nsample = 10**5
    snrlst = range(0,19)
    nzf = 41
    tap = tap2
    
    plt.semilogy(snrlst,equalizer(2, 10, snrlst, nsample, 'viterbi'),\
            snrlst, equalizer(2, 10, snrlst, nsample, 'viterbi'), "--")
    plt.legend(("Channel 1", "Channel 2"), loc='lower left')
    plt.title("ML Viterbi performances for two channels")
    plt.xlabel("SNR (dB)")
    plt.ylabel("SER (dB)")
    plt.grid(True, which='both')
    plt.show()


if __name__=="__main__":
    plotzf()
    plotzfe()
    plotlmmse()
    plotdfe1()
    plotdfe2()
    plotviterbi_1()
    plotviterbi_2()
