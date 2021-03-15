"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
"""

import random

data_list = random.sample(range(1000), 20)
idx_data_list = list()

for i in range(len(data_list)):
    if data_list[i] % 2 == 0:
        idx_data_list.append(i)

print(data_list)
print(idx_data_list)
