import numpy as np
import matplotlib.pyplot as plt

def mle(x, r):
    """ Input: x -- data sequence, r -- initial guess """
    N = len(x)
    def guess(rk):
        # formula 7.31
        return rk-sum((x[i]-rk**i)*i*(rk**(i-1)) for i in range(N))/sum(i*(rk**(i-2))*((i-1)*x[i]-(2*i-1)*(rk**i)) for i in range(N))

    previous = r
    current = guess(r)
    while abs(current-previous) >=0.001:
        previous = current
        current = guess(current)

    return current

