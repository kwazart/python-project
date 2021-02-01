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
new_list = list()

is_even = len(data_list) % 2 == 0
length = len(data_list) if is_even else len(data_list) - 1

# copy changed elements to new list, but if old list is not even - > pass last element
for i in range(length):
    if isPass:
        new_list.append(data_list[i + 1])
        new_list.append(data_list[i])
        isPass = False
    else:
        isPass = True

if not is_even:
    new_list.append(data_list[len(data_list) - 1])

print(new_list)
