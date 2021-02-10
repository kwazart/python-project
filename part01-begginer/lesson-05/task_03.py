"""
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 3.5 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Goodman 3100
Dean 3400
"""

from functools import reduce

employees = dict()
with open("task03-example.txt", "r") as f:
    for line in f:
        words = line.replace("\n", "").split(" ")
        employees.update({words[0]: float(words[1])})

# find the average salary
average_salary = reduce((lambda a, b: a + b), employees.values()) / len(employees)

for k, v in employees.items():
    if v < average_salary:
        print(f'{k} {v}')


