import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


# с использованием декоратора
@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


#  "theory_4_2.fib(10)"
# 1000 loops, best of 5: 72.7 nsec per loop

# "theory_4_2.fib(100)"
# 1000 loops, best of 5: 77 nsec per loop

