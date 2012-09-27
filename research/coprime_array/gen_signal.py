import matplotlib.pyplot as plt
from scipy.signal.waveforms import chirp
import numpy as np

def spectrogram(signal, fs, window_size=256):
    hamming = np.hamming(window_size)
    result = plt.specgram(signal, NFFT=window_size, Fs=fs, window=hamming, noverlap=window_size/2.)
    plt.xlabel("Time (second)")
    plt.ylabel("Frequency (Hz)")
    #plt.show()
    return result

def generate_signal(fs, tmax, fmin, fmax, tnorm):
    """
    Generate signal with linear frequency modulation.
    Input:  
            fs: sample rate for discrete-time signal (in Hz)
            tax: the ending time for sampling (in second)
                (the default beginning time is 0)
            # configuration for frequency modulation
            fmin, fmax: The starting and ending frequency for modulation.
            tnorm: the time to achieve the fmax (in second)
    Output: amplitude values in given sample points
    """
    assert tmax > 0 and tnorm > 0, "The ending time should be > zero."
    assert fs>0 and fmin>=0 and fmax>0 and fs>2*fmax, \
            "The freq and sammple rate setup should obey Nyquist theroem"
    ts = np.arange(0, tmax, 1./fs)
    return chirp(ts, f0=fmin, t1=tnorm, f1=fmax)

