import numpy as np

def gen_prime(n):
    candidates = range(n+1)
    fin = int(n**0.5)
    for i in xrange(2,fin+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None]*(n//i-1)
    return [i for i in candidates[2:] if i]

def main():
    #primes = gen_prime(1000)
    #m = primes[2]
    #n = primes[3]
    m = 17
    n = 19
    n1 = np.arange(0, n+1, 1)
    n2 = np.arange(-m+1, m, 1)

    result = []
    for i in n1:
        for j in n2:
            result.append(m*i-n*j)
    result.sort()
    return result

if __name__ == "__main__":
    main()
