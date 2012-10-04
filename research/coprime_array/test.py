import gen_signal as gs
import coprime_sampling as cs
import matplotlib.pyplot as plt
import numpy as np

fs = 8000
test = gs.generate_signal(fs, 10, 0, 2000, 2, 'linear')

plt.subplot(411)
gs.spectrogram(test, fs)
plt.title("Original Spectrogram")

plt.subplot(412)
y, f, t = cs.benchmark(test, fs, 512)
plt.contour(t, f, abs(y))
plt.title("Spectrogram via autocorrelation without downsampling")
plt.subplots_adjust(hspace=0.5)

plt.subplot(413)
psd1, f, t = cs.main(test, fs, 512, 19, 17)
plt.contour(t, f, psd1)
plt.title("Spectrogram via autocorrelation with 17/19 coprime sampling")
plt.subplots_adjust(hspace=0.5)

plt.subplot(414)
psd2, f, t = cs.main(test, fs, 512, 13, 11)
psd = psd1*psd2
plt.contour(t, f, psd)
plt.title("Spectrogram via autocorrelation with 2-step coprime sampling")
plt.subplots_adjust(hspace=0.5)

plt.show()

