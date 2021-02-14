"""
5. Реализовать класс Stationery (канцелярская принадлежность).

• определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
• создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
• в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
• создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        """
        constructor
        :param title: string - name
        """
        self.title = title

    def draw(self):
        """
        based method for printing rendering result
        :return: None
        """
        print('Start rendering')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """
        override parent method
        :return: None
        """
        print('Pen draws')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """
        override parent method
        :return: None
        """
        print('Pencil draws')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """
        override parent method
        :return: None
        """
        print('Handle draws')


# test list for checking objects method
stationery_list = [
    Pen("Pen"),
    Pencil("Pencil"),
    Handle("Handle")
]

# check and view result
for el in stationery_list:
    el.draw()
