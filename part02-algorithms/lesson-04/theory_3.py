import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


# test_fib(fib_dict) # тесты

# python -m timeit -n 1000 -s "import theory_3" "theory_3.fib_dict(10)"
# "theory_3.fib_dict(10)"
# 1000 loops, best of 5: 3.02 usec per loop

# "theory_3.fib_dict(15)"
# 1000 loops, best of 5: 4.55 usec per loop

# "theory_3.fib_dict(20)"
# 1000 loops, best of 5: 5.78 usec per loop

# "theory_3.fib_dict(25)"
# 1000 loops, best of 5: 7.58 usec per loop

# "theory_3.fib_dict(100)"
# 1000 loops, best of 5: 29.5 usec per loop

# "theory_3.fib_dict(200)"
# 1000 loops, best of 5: 58.9 usec per loop

# "theory_3.fib_dict(500)"
# 1000 loops, best of 5: 166 usec per loop


# cProfile.run('fib_dict(10)')
# 23 function calls (5 primitive calls) in 0.000 seconds
# 19/1    0.000    0.000    0.000    0.000 theory_3.py:14(_fib_dict)

# cProfile.run('fib_dict(15)')
# 33 function calls (5 primitive calls) in 0.000 seconds
# 29/1    0.000    0.000    0.000    0.000 theory_3.py:14(_fib_dict)

cProfile.run('fib_dict(100)')
# 199/1    0.000    0.000    0.000    0.000 theory_3.py:14(_fib_dict)