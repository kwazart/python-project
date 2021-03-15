"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

data_list = random.sample(range(1000), 20)
min_value = max_value = data_list[0]
min_idx = max_idx = 0
for i, el in enumerate(data_list):
    if el > max_value:
        max_value = el
        max_idx = i
    if el < min_value:
        min_value = el
        min_idx = i

print(data_list)
print(f'Min element: {data_list[min_idx]} with id: {min_idx}')
print(f'Max element: {data_list[max_idx]} with id: {max_idx}')
data_list[min_idx], data_list[max_idx] = max_value, min_value
print(data_list)
