"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""

import task_utils


def add_left_space(data):
    return "%15s" % data


def get_user_data():
    name = input("Enter name: ").capitalize()
    last_name = input("Enter surname: ").capitalize()
    year = task_utils.get_int("Enter birth year: ")
    while year < 1910:
        print("Incorrect birth year. Try again")
        year = task_utils.get_int("Enter birth year: ")
    city = input("Enter city: ").capitalize()
    email = task_utils.get_email()
    phone = task_utils.get_phone()

    print(
        f'{add_left_space("Name")}: {name}'
        f'\n{add_left_space("Surname")}: {last_name}'
        f'\n{add_left_space("Birth year")}: {year}'
        f'\n{add_left_space("City")}: {city}'
        f'\n{add_left_space("E-mail")}: {email}'
        f'\n{add_left_space("Phone")}: {phone}'
        )


get_user_data()
