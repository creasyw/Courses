from scipy.stats.distributions import norm
from math import exp, pi


def q_func(x):
    return 1 - norm.cdf(x)


def core_function(y):
    return (q_func((5 + 8 * (2**0.5) * y) / 8 / (2**0.5)))**2 * exp(-y**2 / 2)


def main():
    lower = -100
    upper = 100
    interval = 0.01
    steps = int((upper - lower) / interval)
    result = 0
    for i in range(steps):
        result += core_function(lower + i * interval) * interval
    print result / ((2 * pi)**0.5)


if __name__ == "__main__":
    main()
