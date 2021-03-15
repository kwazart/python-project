"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

a = [random.choice([i for i in range(-100, 100)]) for j in range(200)]
print(a)

max_negative = -101
idx = 0
for i in range(1, len(a)):
    if 0 > a[i] > max_negative:
        max_negative = a[i]
        idx = i

print(f'id: {idx} - value: {max_negative}')
