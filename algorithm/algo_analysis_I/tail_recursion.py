def fac(n):
    def f(n, acc):
        return acc if n < 2 else lambda: f(n - 1, acc * n)

    t = f(n, 1)
    while callable(t):
        t = t()
    return t


def fac2(n):
    def f(n):
        acc = 1
        for i in xrange(1, n + 1):
            acc = acc * i
            yield acc

    t = f(n)
    for i in xrange(n - 1):
        t.next()
    return t.next()


def fac3(n):
    return reduce(lambda x, y: x * y, xrange(1, n + 1))


def test(n):
    print fac3(n)


if __name__ == "__main__":
    test(3000)
