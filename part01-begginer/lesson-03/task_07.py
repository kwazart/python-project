"""
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
"""

from task_06 import cap_func


def cap_func_for_line(line):
    line_list = str(line).split(" ")
    for string in line_list:
        print(cap_func(string), end=" ")


