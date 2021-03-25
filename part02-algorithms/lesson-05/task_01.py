"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple
import statistics

Company = namedtuple('Company', 'name, kv_1, kv_2, kv_3, kv_4')
c_1 = Company('name-1', 100, 200, 300, 400)
c_2 = Company('name-2', 110, 210, 310, 410)
c_3 = Company('name-3', 120, 220, 320, 420)
c_4 = Company('name-4', 130, 230, 330, 430)
c_5 = Company('name-5', 140, 240, 340, 440)

list_company = [c_1, c_2, c_3, c_4, c_5]
dict_company = dict()
for el in list_company:
    dict_company[el[0]] = sum(el[1:])

average_profit = statistics.mean(dict_company.values())
print(f'Средняя прибыль - {average_profit}')

comp_plus_profit = list()
comp_minus_profit = list()

for k, v in dict_company.items():
    if v > average_profit:
        comp_plus_profit.append(k)
    else:
        comp_minus_profit.append(k)

print(f'Компании с прибылью меньше средней: {" ".join(comp_minus_profit)}')
print(f'Компании с прибылью выше средней: {" ".join(comp_plus_profit)}')
