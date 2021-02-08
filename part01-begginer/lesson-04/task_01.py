"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def calculate_salary(parameters):
    if len(argv) == 4:
        file_name, hours, rate, prize = parameters
        try:
            hours = float(hours)
            rate = float(rate)
            prize = float(prize)
        except TypeError:
            return "Wrong parameters type"
        return hours*rate+prize
    else:
        return "Wrong parameters sequence"


def print_greeting_and_result(parameters):

    print('''
        █▀▄ ▄▀▄ █░█ █▀▄ ▄▀▀▄ █░░ █░░ . █▀▀ █░░█ █▄░█ ▄▀▀ ▀█▀ ▀█▀ ▄▀▀▄ █▄░█
        █▀░ █▄█ ▀█▀ █▀▄ █░░█ █░░ █░░ . █▀▀ █░░█ █▀██ █░░ ░█░ ░█░ █░░█ █▀██
        ▀░░ ▀░▀ ░▀░ ▀░▀ ░▀▀░ ▀▀▀ ▀▀▀ . ▀░░ ░▀▀░ ▀░░▀ ░▀▀ ░▀░ ▀▀▀ ░▀▀░ ▀░░▀
    ''')
    print("Monthly salary: " + str(calculate_salary(argv)))


print_greeting_and_result(argv)

