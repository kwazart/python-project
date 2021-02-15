"""
3) Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, nucleus_quantity):
        if self.__check_nucleus_quantity(nucleus_quantity):
            self.nucleus_quantity = nucleus_quantity

    def __add__(self, other):
        return Cell(self.nucleus_quantity + other.nucleus_quantity)

    def __sub__(self, other):
        if self.nucleus_quantity > other.nucleus_quantity:
            return Cell(self.nucleus_quantity - other.nucleus_quantity)
        else:
            print(f'The number of cells in the first cell ({self.nucleus_quantity} '
                  f'is less than the second ({other.nucleus_quantity})')

    def __mul__(self, other):
        return Cell(self.nucleus_quantity * other.nucleus_quantity)

    def __truediv__(self, other):
        return Cell(self.nucleus_quantity // other.nucleus_quantity)

    @staticmethod
    def __check_nucleus_quantity(nucleus_quantity):
        """
        chech quantity cell nucleus. if <= 0  - error and don't create object
        :param nucleus_quantity:  quantity cell nucleus
        :return: boolean result
        """
        if nucleus_quantity <= 0:
            Cell.__print_negative_creation()
            return False
        return True

    @staticmethod
    def __print_negative_creation():
        print(f'A cell cannot have a negative cell count or zero')

    def make_order(self, quantity_in_a_row):
        """
        create new string with '*' characters equals quantity cell nucleus
        :param quantity_in_a_row: users parameter - integer
        :return: string
        """
        result_line = ""
        for i in range(self.nucleus_quantity):
            if i % quantity_in_a_row == 0 and i != 0:
                result_line += '\n'
            result_line += '*'

        return result_line


# test
cell1 = Cell(23)
cell2 = Cell(5)
print(cell1.make_order(7))

i = 0
cell3 = cell1 + cell2
print(f'test (add)#{i+1}:\n{cell3.make_order(5)}\n')
i += 1
cell3 = cell1 - cell2
print(f'test (sub)#{i+1}:\n{cell3.make_order(5)}\n')
i += 1
cell3 = cell1 * cell2
print(f'test (mult)#{i+1}:\n{cell3.make_order(20)}\n')
i += 1
cell3 = cell1 / cell2
print(f'test (div)#{i+1}:\n{cell3.make_order(3)}\n')
