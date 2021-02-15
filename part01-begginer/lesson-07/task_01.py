"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31  22
37  43
51  86

3   5   32
2   4   6
-1  64  -8

3   5   8   3
8   3   7   1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    """
    Matrix class with an arbitrary number of elements
    """
    def __init__(self, data_list):
        """
        Override constuctor
        :param data_list: list included lists
        """
        self.data_list = data_list

    def __str__(self):
        """
        print matrix with condition
        Each row on a new line
        Each column with tabulation
        :return:
        """
        data_string = ""
        for list_el in self.data_list:
            for inner_list_el in list_el:
                data_string += str(inner_list_el)
                data_string += "\t"
            data_string += "\n"
        return data_string

    def __add__(self, other_matrix):
        """
        additional matrix to another matrix
        :param other_matrix:
        :return: new matrix with length based matrix
        """
        # flag - length matrix1 == length matrix2
        hasError = False
        # check lengths
        if len(self.data_list) != len(other_matrix.data_list):
            hasError = True
        else:
            for i in range(len(self.data_list)):
                if len(self.data_list[i]) != len(other_matrix.data_list[i]):
                    hasError = True
        if hasError:
            print(f'Matrix length are not equals')
            return 0

        new_data_list = list()
        # adding each items
        for i in range(len(self.data_list)):
            new_inner_data_list = list()
            for j in range(len(data_list[i])):
                new_inner_data_list.append(self.data_list[i][j] + other_matrix.data_list[i][j])
            new_data_list.append(new_inner_data_list)

        return Matrix(new_data_list)


data_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

data_list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(data_list)
matrix1 = Matrix(data_list1)


print(matrix + matrix1)
