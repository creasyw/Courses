
def collatz(x):
    result = []
    while x != 1:
        result.append(x)
        if  x%2 == 0:
            x /= 2
        else:
            x = x*3+1
    print max(result)

collatz(217)
