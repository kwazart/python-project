import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


# test_fib(fib_list)

# "theory_3_2.fib_list(10)"
# 1000 loops, best of 5: 4.9 usec per loop

# "theory_3_2.fib_list(20)"
# 1000 loops, best of 5: 7.81 usec per loop

# "theory_3_2.fib_list(50)"
# 1000 loops, best of 5: 15.5 usec per loop

# "theory_3_2.fib_list(100)"
# 1000 loops, best of 5: 28.2 usec per loop

# "theory_3_2.fib_list(500)"
# 1000 loops, best of 5: 137 usec per loop

cProfile.run('fib_list(500)')
# 19/1    0.000    0.000    0.000    0.000 theory_3_2.py:15(_fib_list) # 10
# 39/1    0.000    0.000    0.000    0.000 theory_3_2.py:15(_fib_list) # 20
# 99/1    0.000    0.000    0.000    0.000 theory_3_2.py:15(_fib_list) # 50
# 199/1    0.000    0.000    0.000    0.000 theory_3_2.py:15(_fib_list) # 100
# 999/1    0.001    0.000    0.001    0.001 theory_3_2.py:15(_fib_list) # 500
