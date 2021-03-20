import timeit


# x = 2 + 2
# print(timeit.timeit("x = 2 + 2"))
# print(timeit.timeit('x = sum(range(10))'))


def foo():
    s = 0
    for i in range(10000000):
        s += i
    return s


print(timeit.timeit('x = foo()'))
# python -m timeit -n 100 -s "import theory"
