"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

a = 5
b = 6
print(f'Побитовое И между {a} и {b} = {a & b}')
print(f'Побитовое ИЛИ между {a} и {b} = {a | b}')
print(f'Сдвиг влево числа {a} на 2 знака = {a << 2}')
print(f'Сдвиг вправо числа {a} на 2 знака = {a >> 2}')