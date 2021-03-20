import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

# cProfile.run('fib(15)')
# 1976 function calls (4 primitive calls) in 0.001 seconds
# 1973/1    0.001    0.000    0.001    0.001 theory_2.py:10(fib)

# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.005 seconds
# 21891/1    0.005    0.000    0.005    0.005 theory_2.py:10(fib)

# test_fib(fib)

# python -m timeit -n 1000 -s "import theory_2" "theory_2.fib(10)"

# "theory_2.fib(10)"
# 1000 loops, best of 5: 12.9 usec per loop

# "import theory_2" "theory_2.fib(15)"
# 1000 loops, best of 5: 136 usec per loop

# "theory_2.fib(20)"
# 1000 loops, best of 5: 1.53 msec per loop

# "theory_2.fib(25)"
# 1000 loops, best of 5: 17 msec per loop
