def f(x):
    return x - 1


def g(x):
    return 2 * x


def h(x, y):
    return int(str(x) + str(y))


print(h(g(g(5)), g(g(g(f(f(5)))))))
