"""
6. Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

data_subject_dict = dict()
with open("task06-example.txt", "r") as file:
    for line in file:
        # find the name of the subject
        subject = line.strip().split(":")
        subject_name = subject[0]

        # find existing classes
        lessons = subject[1].strip().replace("   ", " ").split(" ")

        # add items not equal to the dash
        common_lessons = 0
        for el in lessons:
            if el != "-":
                common_lessons += int(el[0:el.find("(")])
        data_subject_dict.update({subject_name: common_lessons})

print(data_subject_dict)
