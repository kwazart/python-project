"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""

from collections import OrderedDict

dict_schema = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               "A": 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def find_key(value):
    for k, v in dict_schema.items():
        if v == value:
            return k


command = ''
while True:
    command = input('Введите 1ое число в hex-форме, затем * или +, затем 2ое число. -1 - Выход: ')
    if command.lower() == '-1':
        break

    # создаем последовательный словарь (первое число, знак, второе число) - 3 пары
    dct = OrderedDict.fromkeys(command.split(" "))

    # проверка длины
    if len(dct) != 3:
        print("Неверный ввод. Попробуй еще раз\n")
        continue

    counter = 0
    for k in dct.keys():
        if counter == 0:
            # запоминаем первую переменную пользователя
            f_val_hex = k
            # создаем из ключа словаря список
            f_list = list(k)
            for i in range(len(f_list)):
                # проверяем есть ли элементы списка в шестнадцатеричной системе
                if f_list[i] in dict_schema:
                    # если есть, берем из словаря (общих значений) значение по данному ключу
                    f_list[i] = dict_schema[f_list[i]]
                else:
                    print("Неверный ввод первого значения. Попробуй еще раз\n")
                    continue
        elif counter == 1:
            # проверка знака. должно быть + или *
            if k == '+' or k == '*':
                sign = k
            else:
                print("Неверный ввод знака. Попробуй еще раз\n")
                continue
        elif counter == 2:
            # запоминаем вторую переменную пользователя
            s_val_hex = k
            # создаем из ключа словаря список
            s_list = list(k)
            for i in range(len(s_list)):
                # проверяем есть ли элементы списка в шестнадцатеричной системе
                if s_list[i] in dict_schema:
                    s_list[i] = dict_schema[s_list[i]]
                else:
                    print("Неверный ввод второго значения. Попробуй еще раз\n")
                    continue
        counter += 1

    f_num = 0
    s_num = 0

    # переводим числа из 16ной системы в 10ную
    counter = 0
    for i in reversed(f_list):
        f_num += i * (16 ** counter)
        counter += 1

    counter = 0
    for i in reversed(s_list):
        s_num += i * (16 ** counter)
        counter += 1

    result_10 = f_num * s_num if sign == "*" else f_num + s_num

    print(f'{f_num} {sign} {s_num} = {result_10}')

    # переводим числа из 10ной системы в 16ную
    result_hex = ""
    while result_10 % 16 > 0:
        result_hex = find_key(result_10 % 16) + result_hex
        result_10 = result_10 // 16

    print(f'{f_val_hex} {sign} { s_val_hex} = {result_hex}')

