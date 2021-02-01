"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

data_list = [1, 2.0, "three", [4, 5], ("5", "6"), {7.0, 8.0}, dict(key9=10, key11="11")]


def print_list(data):
    print(f'Max size list is {len(data)}.')
    for i in data:
        print(i)


def select_id(list_len):
    while True:
        try:
            variant = int(input('\nEnter correct variant for view element type (0 - exit): '))
            if type(variant) == int and 0 <= variant <= list_len:
                return variant
        except ValueError:
            print('NOT INT. Try again')


print_list(data_list)

while True:
    list_id = select_id(len(data_list))
    if list_id == 0:
        break
    print(str(type(data_list[list_id - 1])) + "\n")
