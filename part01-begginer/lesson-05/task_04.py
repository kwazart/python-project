"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open("task04-example.txt", "r") as file, open("task04-example-new.txt", "w") as new_file:
    for line in file:
        if line.__contains__("One"):
            line = line.replace("One", "Один")
        elif line.__contains__("Two"):
            line = line.replace("Two", "Два")
        elif line.__contains__("Three"):
            line = line.replace("Three", "Три")
        elif line.__contains__("Four"):
            line = line.replace("Four", "Четыре")
        new_file.write(line)
