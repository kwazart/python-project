"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, text_error):
        self.text_error = text_error


def test_foo():
    data_list = [int(elem) for elem in input("Input values for division with space: ").split()]
    try:
        if data_list[1] == 0:
            raise MyException("Exception: division by zero")
        return data_list[0] / data_list[1]
    except MyException as my_exp:
        print(my_exp.text_error)
    return 0


print(test_foo())

