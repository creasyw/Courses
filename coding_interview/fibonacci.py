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
def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]

def identity_power(n):
    i = [[1, 1], [1, 0]]
    def helper(acc, count):
        if count == 0:
            return i
        elif count == 1:
            return acc
        else:
            result = helper(acc, count/2)
            result = matrix_multiply(result, result)
            if count % 2:
                result = matrix_multiply(result, acc)
            return result
    return helper(i, n)

def fib_matrix(n):
    return matrix_multiply(identity_power(n-1), [[1, 0]])[0][0]
