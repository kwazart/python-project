"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

a = [random.choice([i for i in range(100)]) for j in range(200)]
max_count = 1
idx = 0
for i in range(0, len(a) - 1):
    count = 0
    for j in range(1, len(a)):
        if a[i] == a[j]:
            count += 1
    if max_count < count:
        max_count = count
        idx = i

print(a)
print(f'Value: {a[idx]} - {max_count} times')
