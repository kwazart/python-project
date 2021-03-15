"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


sum_result = 1
user_count = int(input("Введите количество элементов: "))
for i in range(user_count - 1):
    sum_result /= -2
print(sum_result)
