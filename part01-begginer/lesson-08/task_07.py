"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, valid_part, imaginary_part: str):
        self.valid_part = valid_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        valid_part = self.valid_part + other.valid_part
        imaginary_part = str(int(self.imaginary_part[0: self.imaginary_part.find("i")]) + int(other.imaginary_part[0: other.imaginary_part.find("i")]))
        return ComplexNumber(valid_part, imaginary_part + "i")

    def __mul__(self, other):
        first_elem = self.valid_part + other.valid_part
        second_elem = self.valid_part * int(other.imaginary_part[0: other.imaginary_part.find("i")])
        third_elem = int(self.imaginary_part[0: self.imaginary_part.find("i")]) * other.valid_part
        fourth_elem = int(self.imaginary_part[0: self.imaginary_part.find("i")]) * int(other.imaginary_part[0: other.imaginary_part.find("i")])
        return ComplexNumber(first_elem + fourth_elem, str(second_elem + third_elem) + "i")

    def __str__(self):
        return f'{self.valid_part} + {self.imaginary_part}'


cn1 = ComplexNumber(2, "3i")
cn2 = ComplexNumber(2, "3i")
print(cn1 + cn2)
print(cn1 * cn2)
