from math import exp
import numpy as np
from scipy.special import j0

def p_z(z):
    """PDF of Rician fading distribution"""
    return exp(-1-(z**2)*10**8)*j0(2*z*10**4)*z

def cdf_rician(lower, upper, step):
    """Approximate CDF of Rician fading distribution"""
    interval = int((upper-lower)/step)
    result = 0
    for i in range(interval):
        result += step*p_z(lower+i*step)
    return result*2*10**8

def main():
    lower = 0
    upper = 10**(-4)
    step = 10**(-10)
    print cdf_rician(lower, upper, step)

if __name__ == "__main__":
    main()
