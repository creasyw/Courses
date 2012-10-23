import numpy as np
from math import pi
import matplotlib.pyplot as plt

def MQAM_for_MRC():
    # The known variables
    m = [1,2,4,8]
    g = 0.1
    snr_db = np.arange(5,20.01,0.01)
    snr = np.power(10, snr_db/10)
    step = 0.001
    # let phi begin from 0.001 to prevent "divide by 0" in MGF
    phi1 = np.arange(0.001, pi/2, step)
    phi2 = np.arange(0.001, pi/4, step)
    pb = np.zeros((len(m),len(snr)))

    # calculate integral
    for i in range(len(m)):
        for j in range(len(snr)):
            mrs1 = np.power((1+(g*snr[j])/(np.power(np.sin(phi1),2))),(-m[i]))
            mrs2 = np.power((1+(g*snr[j])/(np.power(np.sin(phi2),2))),(-m[i]))
            pb[i,j] = (4/pi)*0.75*sum(mrs1)-(4/pi)*(0.75**2)*sum(mrs2)
    # plot pb
    plt.plot(snr_db, np.log10(pb[0])-3, 'b-', label="M=1")
    plt.plot(snr_db, np.log10(pb[1])-3, 'y--', label="M=2")
    plt.plot(snr_db, np.log10(pb[2])-3, 'g-.', label="M=4")
    plt.plot(snr_db, np.log10(pb[3])-3, 'r:', label="M=8")
    plt.legend(title="Diversity degree", loc='best')
    plt.xlabel("SNR (db)")
    plt.ylabel("Bit error rate (db)")
    plt.xlim(5,20)
    plt.show()

if __name__ == "__main__":
    MQAM_for_MRC()

