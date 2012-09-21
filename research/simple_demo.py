from math import pi, sin
import matplotlib.pyplot as plt

def generate_signal():
    Fs = 16000
    w = 
    return [sin(2*pi*t/20.) for t in xrange(20000)]

def spectrogram(signal, fs):
    window_size = 128
    hamming = np.hamming(window_size)
    Pxx, freqs, bins = plt.specgram(signal, NFFT=window_size, Fs=fs, window=hamming, noverlap=64)

