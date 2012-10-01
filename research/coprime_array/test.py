import gen_signal as gs
import coprime_sampling as cs
import matplotlib.pyplot as plt

fs = 8000
test = gs.generate_signal(fs, 10, 0, 2000, 5, 'quadratic')

plt.subplot(411)
gs.spectrogram(test, fs)

plt.subplot(412)
y, f, t = cs.main(test, fs, 512, 19, 17)
z = abs(y)
plt.contourf(t, f, z)

plt.subplot(413)
y, f, t = cs.main(test, fs, 512, 13, 11)
z = abs(y)
plt.contourf(t, f, z)

plt.subplot(414)
y, f, t = cs.main(test, fs, 512, 9, 7)
z = abs(y)
plt.contourf(t, f, z)

plt.show()


