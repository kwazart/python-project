import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_loop(n):
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second


# test_fib(fib_loop)

# timeit
#  "theory_4.fib_loop(10)"
# 1000 loops, best of 5: 622 nsec per loop

# "theory_4.fib_loop(50)"
# 1000 loops, best of 5: 2.31 usec per loop

# "theory_4.fib_loop(100)"
# 1000 loops, best of 5: 4.78 usec per loop

# "theory_4.fib_loop(500)"
# 1000 loops, best of 5: 25.6 usec per loop

#  "theory_4.fib_loop(1000)"
# 1000 loops, best of 5: 50.6 usec per loop

# "theory_4.fib_loop(50000)"
# 1000 loops, best of 5: 22.8 msec per loop


# cProfile.run('fib_loop(1000)')
# 4 function calls in 0.000 seconds - 10
# 4 function calls in 0.000 seconds - 1000