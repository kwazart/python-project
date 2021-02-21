"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
"""

from functools import reduce


def generate_list_with_even_digital(a, b):
    return [i for i in range(a, b+1) if i % 2 == 0]


# easy-test
print(reduce(lambda a, b: a*b, generate_list_with_even_digital(1, 10)))  # result - 3840 = 2 * 4 * 6 * 8 * 10
print(reduce(lambda a, b: a*b, generate_list_with_even_digital(100, 1000)))
