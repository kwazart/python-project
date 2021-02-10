"""
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

f = open('text.txt', 'w')

print("Record line into file. Exit - empty line")

while True:
    line = input("Add line: ")
    if line == "":
        break
    f.write(line + "\n")
f.close()
