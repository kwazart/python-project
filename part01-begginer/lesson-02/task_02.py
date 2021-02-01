"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

print("Fill the new list\nEnter \'STOP\' for finish.\n")

data_list = []

while True:
    element = input('Add: ')
    if element == 'STOP':
        break
    elif element == '':
        # or change to None
        print('Empty line.')
        continue
    data_list.append(element)

print(data_list)

# flag for passing iterator index
isPass = True

is_even = len(data_list) % 2 == 0
length = len(data_list) if is_even else len(data_list) - 1

for i in range(length):
    if isPass:
        data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
        isPass = False
    else:
        isPass = True

print(data_list)
