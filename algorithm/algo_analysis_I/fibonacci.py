def fib(n):
    temp = [1, 1, 2]
    if n < 3:
        return temp[n]
    else:
        for i in range(3, n):
            index = i % 3
            temp[index] = temp[(i + 1) % 3] + temp[(i + 2) % 3]
        return temp[index]
