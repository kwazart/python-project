"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""


def generate_list_multiple_20_or_21(a, b):
    return [i for i in range(a, b+1) if (i % 20 == 0 or i % 21 == 0)]


print(generate_list_multiple_20_or_21(20, 240))
