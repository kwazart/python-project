"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

from task_utils import get_int


def function_division():
    val_1 = get_int()
    while True:
        val_2 = get_int()
        if val_2 == 0:
            print("Incorrect value. Cannot division by zero. Try again")
            continue
        break
    print("%.3f" % (val_1 / val_2))


function_division()
