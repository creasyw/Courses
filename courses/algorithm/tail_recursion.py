def fac(n):
    def f(n, acc):
        return acc if n<2 else lambda: f(n-1, acc*n)
    t = f(n, 1)
    while callable(t):
        t = t()
    return t

def fac2(n):
    return reduce(lambda x, y: x*y, xrange(1,num))

def test(n):
    print fac(n)

if __name__ == "__main__":
    test(3000)
