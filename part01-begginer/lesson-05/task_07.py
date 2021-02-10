"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

from functools import reduce
import json

result_data_list = list()
dict_profit = dict()
dict_lesion = dict()
dict_average_profit = dict()

with open("task07-example.txt", "r") as file:
    for line in file:
        firm = line.strip().split("   ")
        firm_dict = {firm[0]: int(firm[2]) - int(firm[3])}
        if firm_dict[firm[0]] >= 0:
            dict_profit[firm[0]] = firm_dict[firm[0]]
        else:
            dict_lesion[firm[0]] = firm_dict[firm[0]]

    dict_average_profit["average_profit"] = reduce(lambda a, b: a + b, list(dict_profit.values())) / len(dict_profit)

result_data_list.append(dict_profit)
result_data_list.append(dict_average_profit)
result_data_list.append(dict_lesion)
print(result_data_list)

with open("firms_data_report.json", "w") as write_f:
    json.dump(result_data_list, write_f)





