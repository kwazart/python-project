"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]


def add_score(score):
    if score in my_list:
        index = my_list.index(score)
        my_list.insert(index, score)
    else:
        if score > my_list[0]:
            my_list.insert(0, score)
        else:
            for i in range(len(my_list)):
                if score < my_list[i]:
                    if i == len(my_list)-1:
                        my_list.append(score)
                    continue
                else:
                    my_list.insert(i, score)
                break


while True:
    print(my_list, end="\n")
    new_score = input('Input new score value (0 - exit): ')

    try:
        new_score = int(new_score)
        if new_score == 0:
            break
        add_score(new_score)
    except ValueError:
        print('NOT INT. Try again')
