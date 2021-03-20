"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2

Примечание по профилированию кода: для получения достоверных результатов при замере времени
необходимо исключить/заменить функции print() и input() в анализируемом коде.
С ними вы будете замерять время вывода данных в терминал и время, потраченное пользователем,
на ввод данных, а не быстродействие самого алгоритма.
"""


# без решета Эратосфена
def easy_number_var_1(n):
    lst = [2]
    # for i in range(3, n+1, 2):
    i = 1
    while len(lst) < n:
        i += 2
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[len(lst) - 1]

# "task_02.easy_number_var_1(10)"
# 1000 loops, best of 5: 4.51 usec per loop

# "task_02.easy_number_var_1(30)"
# 1000 loops, best of 5: 18.4 usec per loop

# "task_02.easy_number_var_1(50)"
# 1000 loops, best of 5: 40.8 usec per loop

# "task_02.easy_number_var_1(100)"
# 1000 loops, best of 5: 113 usec per loop

# "task_02.easy_number_var_1(500)"
# 1000 loops, best of 5: 1.07 msec per loop

# "task_02.easy_number_var_1(1000)"
# 1000 loops, best of 5: 2.8 msec per loop

# "task_02.easy_number_var_1(2000)"
# 1000 loops, best of 5: 7.48 msec per loop


# при помощи решета Эратосфена
def find_easy_numbers_until_n(n):
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return lst


# оптимизация под наше задачу. мы вводим не границу а конкретный индекс
def easy_number_var_2(n):
    x = n * 4
    temp_list = find_easy_numbers_until_n(x)
    length_list = len(temp_list)
    while length_list < n:
        x *= 4
        temp_list = find_easy_numbers_until_n(x)
        length_list = len(temp_list)
    return temp_list[n - 1]

# "task_02.easy_number_var_2(10)"
# 1000 loops, best of 5: 7.75 usec per loop

# "task_02.easy_number_var_2(30)"
# 1000 loops, best of 5: 19.1 usec per loop

# "task_02.easy_number_var_2(50)"
# 1000 loops, best of 5: 169 usec per loop

# "task_02.easy_number_var_2(100)"
# 1000 loops, best of 5: 357 usec per loop

# "task_02.easy_number_var_2(500)"
# 1000 loops, best of 5: 1.89 msec per loop

# "task_02.easy_number_var_2(1000)"
# 1000 loops, best of 5: 3.97 msec per loop

# "task_02.easy_number_var_2(2000)"
# 1000 loops, best of 5: 7.61 msec per loop


"""
Большее время выполнения алгоритма решета Эратосфена обусловлено тем, что мы не задаем границу поиска, 
а хотим получить определенное число по индексу. Расширение границы поиска в моем случае х4 (проверено
НЕДОЛГИМ эмпирическим путем). Вероятно больший прирост границы поиска даст лучше результат.
Только на больших входящих параметрах начинается уравнивание времени результатов выполнения

Вывод: пользуйтесь алгоритмом эратосфена по назначению, т.е. вводя границы поиска
"""


def erat(a):
    b = a*10
    list1 = [i for i in range(b)]
    list1[1] = 0
    for i in range(2, b):
        if list1[i] != 0:
            j = i * 2
            while j < b:
                list1[j] = 0
                j += i
    result = [i for i in list1 if i != 0]
    num = result[a]
    return num

print(erat(10))
print(erat(100))
print(erat(100))
print(erat(100))
print(erat(100))
