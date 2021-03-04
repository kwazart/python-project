"""
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например,
если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

left_int = int(input('Введите левую целочисленную границу: '))
right_int = int(input('Введите правую целочисленную границу: '))
result_int = random.randint(left_int, right_int)
print(f"Случайное значение между {left_int} и {right_int} = {result_int}\n")

left_float = float(input('Введите левую вещественную границу: '))
right_float = float(input('Введите правую вещественную границу: '))
result_float = random.uniform(left_float, right_float)
print(f"Случайное значение между {left_float} и {right_float} = {result_float}\n")

left_char = ord(input('Введите левую символьную границу: '))
right_char = ord(input('Введите правую символьную границу: '))
result_char = chr(random.randint(left_char, right_char))
print(f"Случайное значение между '{chr(left_char)}' и '{chr(right_char)}' = '{result_char}'")
