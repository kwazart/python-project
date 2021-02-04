"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def sum_of_two_max_elements(a, b, c):
    max1 = max(a, b)
    if a == max1:
        max2 = max(b, c)
    else:
        max2 = max(a, c)
    return max1 + max2

