"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

from functools import reduce

with open("task05-example.txt", "w") as f:
    # writing
    for i in range(20, 1000, 4):
        f.write(str(i) + " ")

with open("task05-example.txt", "r") as f:
    # reading
    for line in f:
        # lambda: string covert to integer ->  lambda: sum calculate
        print(reduce((lambda a, b: a + b), list(map(lambda x: int(x), line.strip().split(" ")))))


