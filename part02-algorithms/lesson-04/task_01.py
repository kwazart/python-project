"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Выбрана 3я задача 3го урока
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random


def change_min_max_var_1(n):
    data_list = random.sample(range(n * 100), n)
    min_value = max_value = data_list[0]
    min_idx = max_idx = 0
    for i, el in enumerate(data_list):
        if el > max_value:
            max_value = el
            max_idx = i
        if el < min_value:
            min_value = el
            min_idx = i

    data_list[min_idx], data_list[max_idx] = max_value, min_value

# "task_01.change_min_max_var_1(100)"
# 1000 loops, best of 5: 41.3 usec per loop

# "task_01.change_min_max_var_1(1000)"
# 1000 loops, best of 5: 381 usec per loop

# "task_01.change_min_max_var_1(10000)"
# 1000 loops, best of 5: 3.93 msec per loop


def change_min_max_var_2(n):
    data_list = random.sample(range(n * 100), n)
    min_value = min(data_list)
    max_value = max(data_list)
    count = 0
    for i in range(len(data_list)):
        if data_list[i] == min_value:
            data_list[i] = max_value
            count += 1
        elif data_list[i] == max_value:
            data_list[i] = min_value
            count += 1
        if count == 2:
            break

# "task_01.change_min_max_var_2(100)"
# 1000 loops, best of 5: 44.4 usec per loop

# "task_01.change_min_max_var_2(1000)"
# 1000 loops, best of 5: 398 usec per loop

# "task_01.change_min_max_var_2(10000)"
# 1000 loops, best of 5: 4.16 msec per loop


def change_min_max_var_3(n):
    data_list = random.sample(range(n * 100), n)
    new_data_list = data_list.copy()
    new_data_list.sort()
    min_value = new_data_list[0]
    max_value = new_data_list[len(new_data_list) - 1]
    min_idx = data_list.index(min_value)
    max_idx = data_list.index(max_value)
    data_list[max_idx], data_list[min_idx] = min_value, max_value


# "task_01.change_min_max_var_3(100)"
# 1000 loops, best of 5: 43 usec per loop

# "task_01.change_min_max_var_3(1000)"
# 1000 loops, best of 5: 411 usec per loop

# "task_01.change_min_max_var_3(10000)"
# 1000 loops, best of 5: 4.58 msec per loop

"""
Сравнительная таблица
        Var.1           Var.2           Var.3
100     41.3 usec       44.4 usec       43 usec
1000    381 usec        398 usec        411 usec
1000    4.16 msec       4.16 msec       4.58 mse

Итог: выбран первоначальный 1ый вариант (как был выполнен в 3 ДЗ) 
т.к. никакие дополнительные функции не используются и идет лишь 1 прогон по списку
"""