"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора .
Второй — более сложная реализация без оператора , предусматривающая использование цикла.
"""


def digit_elevate(a, b):
    if a == 1 or b == 0:
        return 1
    if a == 0:
        return 0
    result = 1
    for i in range(abs(b)):
        result /= a
    return result


print("test#1 - " + str(digit_elevate(4, -2) == 4**(-2)))
print("test#2 - " + str(digit_elevate(4, -1) == 4**(-1)))
print("test#3 - " + str(digit_elevate(14, -3) == 14**(-3)))
print("test#4 - " + str(digit_elevate(50, -3) == 50**(-3)))
print("test#5 - " + str(digit_elevate(45, 0) == 45**0))
print("test#6 - " + str(digit_elevate(1, 20) == 1**20))
print("test#7 - " + str(digit_elevate(0, 10) == 0**10))
print("test#7 - " + str(digit_elevate(0, 0) == 0**0))

