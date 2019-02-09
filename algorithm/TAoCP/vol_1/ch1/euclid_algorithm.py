# Algorithm E (Euclid’s algorithm). Given two positive integers m and n, find their greatest common
# divisor, that is, the largest positive integer that evenly divides both m and n.
#
# E1. [Find remainder.] Divide m by n and let r be the remainder. (We will have 0 ≤ r < n.)
# E2. [Is it zero?] If r = 0, the algorithm terminates; n is the answer.
# E3. [Reduce.] Set m ← n, n ← r, and go back to step E1.

def gcd(m, n):
    if m < n:
        m, n = n, m
    while m % n != 0:
        m, n = n, m%n
    return n

print(gcd(15, 5) == 5)
print(gcd(5, 15) == 5)
print(gcd(111, 27) == 3)
