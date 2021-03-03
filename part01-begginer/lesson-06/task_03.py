"""
3. Реализовать базовый класс Worker (работник).

• определить атрибуты: name, surname, position (должность), income (доход);
• последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
• создать класс Position (должность) на базе класса Worker;
• в классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
• проверить работу примера на реальных данных:
создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        """
        constructor
        :param name: first name - string
        :param surname: second name - string
        :param position: worker position
        :param wage: main income part
        :param bonus: next income part
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        """
        constructor based on Worker class constructor
        :param name: first name - string
        :param surname: second name - string
        :param position: worker position
        :param wage: main income part
        :param bonus: next income part
        """
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        """
        getter (name)
        :return: name + surname
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
        getter (income)
        :return: income(wage) + income(bonus)
        """
        return self._income.get("wage") + self._income.get("bonus")


# test
worker_1 = Position("Ivan", "Ivanov", "manager", 10000, 200)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.position)

print('-------------------')

worker_2 = Position("John", "Smith", "top-manager", 30000, 9000)
print(worker_2.get_full_name())
print(worker_2.get_total_income())
print(worker_2.position)
