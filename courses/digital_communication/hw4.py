import numpy as np
from math import cos, sin, pi, log
import matplotlib.pyplot as plt
from scipy.stats import norm

# calculate the norm distance between points
norm = lambda m: (reduce(lambda acc, itr: acc+itr**2, m, 0))**0.5

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
    return rint, signal

def transfer_in_channel (signal, Es, snr):
    """
    Simulate the effect that signal is transferring in the channel.
    Note that the input variable SNR value is in LINEAR unit.
    """
    # Generate Gaussian noise with certain constraints
    awgn = np.random.normal(loc=0.0, scale=(Es/log(3,2)/snr/2)**0.5, size=len(signal))
    noise = (np.vstack((awgn, awgn))).T
    return signal+noise

def detection (receive, Es):
    """ Detect the received signal to symbol with MAP detector."""
    cd = range(1,9)
    # Mapping the codewords to modulation plane
    mapping = (np.vstack((map(lambda m: (Es)**0.5*cos(2*pi*m/8), cd), \
            map(lambda m: (Es)**0.5*sin(2*pi*m/8), cd)))).T
    
    decoded = []
    for i in receive:
        codeword = 0; mindis = float('+inf')
        # Performing nearest neighbor detection
        for j in range(len(mapping)):
            distance = norm(i-mapping[j])
            if distance < mindis:
                mindis = distance
                # j is the index of mapping, the real codeword should be j+1
                codeword = j+1
        assert codeword!=0, "There is something wrong in the decoding process!"
        decoded.append(codeword)
    return decoded

def performance(tx, rx):
    """ Calculate the symbol error rate. """
    count = sum(1 for i in range(len(tx)) if tx[i]==rx[i])
    return 1-float(count)/len(tx)

def plotting(snr, ser, ser_max, ser_min):
    fig = plt.figure()
    plt.semilogy(snr, ser)
    plt.semilogy(snr, ser_max, ls='--')
    plt.semilogy(snr, ser_min, ls="-.")
    plt.grid(True)
    plt.xlabel("Signal-to-Noise Ratio")
    plt.ylabel("Symbol Error Rate")
    plt.title("8-PSK Communication System in AWGN")
    plt.show()

def theoretical(Es, snr):
    q_function = lambda x: 1-norm.cdf(x)
    dmin = norm(np.array([(Es)**0.5*cos(2*pi/8), (Es)**0.5*sin(2*pi/8)]) - np.array([(Es)**0.5, 0]))
    noise = Es/(10**(np.array(snr)/10.))
    # choose the 3rd upper bound of Pe
    ser_max = 7*q_function(dmin/((2*noise)**0.5))
    ser_min = 2/7*q_function(dmin/((2*noise)**0.5))
    return ser_max, ser_min

def main():
    Es = 1
    snr = range(0,19)
    tx, signal = signal_generation(Es)
    result = []
    for i in snr:
        # snr input to transfer_in_channel should be LINEAR.
        rx = transfer_in_channel(signal, Es, 10**(i/10.))
        decoded = detection(rx, Es)
        ser = performance(tx, decoded)
        print "SNR = %s -- SER = %s."%(i, ser)
        result.append(ser)
    ser_max, ser_min = theoretical(Es, snr)
    plotting(snr, result, ser_max, ser_min)

if __name__=="__main__":
    main()

