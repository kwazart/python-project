"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве
знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать
об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль,
если он ввел его в качестве делителя.
"""

while True:
    a = int(input("Введите 1ое число: "))
    b = int(input("Введите 2ое число: "))
    sign = input("Введите знак ('+', '-', '*', '/': ")
    if sign == '0':
        break
    if sign != '+' and sign != '-' and sign != '*' and sign != '/':
        print("Ошибка ввода знака. Повторите еще раз.")
    else:
        print(f'{a} {sign} {b} = ', end='')
        if sign == '+':
            print(a + b)
        elif sign == '-':
            print(a - b)
        elif sign == '*':
            print(a * b)
        else:
            print(a / b)

print("Конец программы")
