import numpy as np

# Recursion
fib = lambda n: fib(n-1)+fib(n-2) if n > 2 else 1

# Memoization
def fib_memo(n):
    register = {0: 0, 1: 1}
    def helper(count):
        if count in register:
            return register[count]
        register[count] = helper(count-1)+helper(count-2)
        return register[count]
    return helper(n)

# Dynamic Programming
def fib_dp(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

# Math of Golden Ratio
def fib_math(n):
    phi = (1+np.sqrt(5))/2
    return int(phi**n/np.sqrt(5)+0.5)

# Matrix Algebra
def fib_matrix(n):
    return np.dot(np.linalg.matrix_power(np.array([[1,1],[1,0]], dtype=object),\
            (n-1)), np.array([1,0], dtype=object))[0]
# The dtype=object is necessary in order to force numpy to use python integers.
# Refer to http://bit.ly/1tURmVR for more info.
