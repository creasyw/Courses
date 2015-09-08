import numpy as np
import matplotlib.pyplot as plt


def mle(x, r):
    """ Input: x -- data sequence, r -- initial guess """
    N = len(x)

    def guess(rk):
        # formula 7.31
        return rk - sum((x[i] - rk**i) * i * (rk**(i - 1))
                        for i in range(N)) / sum(i * (rk**(i - 2)) * (
                            (i - 1) * x[i] - (2 * i - 1) * (rk**i))
                                                 for i in range(N))

    previous = r
    current = guess(r)
    while abs(current - previous) >= 0.001:
        previous = current
        current = guess(current)

    return current


def data_generation(N, std, r):
    """
    Input: N -- the length of signal, r -- the real value
    Output: sequence of data according to certain distribution
    """
    mr = np.array([r**i for i in range(N)])
    return mr + np.random.normal(0, std, N)


def plotting(mean, var, maxlength):
    ax1 = plt.subplot(211)
    ax1.set_xticklabels(range(50, maxlength, 100))
    plt.plot(mean)
    plt.title("Mean of MLE for " + r'$r=0.5$ and $\sigma^2=0.001$')
    plt.ylabel("Value of the expectation")
    ax2 = plt.subplot(212)
    ax2.set_xticklabels(range(50, maxlength, 100))
    plt.plot(var)
    plt.title("Variance of MLE for " + r'$r=0.5$ and $\sigma^2=0.001$')
    plt.subplots_adjust(hspace=0.35)
    plt.ylabel("Value of the variance")
    plt.xlabel("Length of signal")
    plt.show()


def main():
    # noise variance
    nvar = 10** -3
    batch = 50
    r = 0.5
    maxlength = 1000
    # initial guess
    init = 0.8

    expect = []
    variance = []
    for length in range(50, maxlength, 100):
        result = [mle(data_generation(length,nvar**0.5,r), init) \
                for i in range(batch)]
        expect.append(np.mean(result))
        variance.append(np.var(result))
    plotting(expect, variance, maxlength)


if __name__ == "__main__":
    main()
