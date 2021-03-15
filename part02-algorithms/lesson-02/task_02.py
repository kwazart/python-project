"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

list_odd = list()
list_even = list()
num_value = int(input("Введите целое число: "))

while num_value > 0:
    num = num_value % 10
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)
    num_value //= 10

print(f'{len(list_even)} четные цифры {list_even} и {len(list_odd)} нечетные цифры {list_odd}')
