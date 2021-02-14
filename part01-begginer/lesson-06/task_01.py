"""
1. Создать класс TrafficLight (светофор).

• определить у него один атрибут color (цвет) и метод running (запуск);
• атрибут реализовать как приватный;
• в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
• продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
• переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
• проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:

    def __init__(self, color):
        """
        constructor
        :param color: Green or Red
        another color will be changed to red in the method running()
        """
        self.__color = color

    # def running(self):
    #     """
    #     Variant 1
    #     Recursive method to simulate endless traffic lights.
    #     There is a color change from red to green and vice versa
    #     :return: None
    #     """
    #     if self.get_color() == "Red":
    #         print(self.get_color())
    #         time.sleep(7)
    #         print("Yellow")
    #         time.sleep(2)
    #         self.set_color("Green")
    #     elif self.get_color() == "Green":
    #         print(self.get_color())
    #         time.sleep(5)
    #         print("Yellow")
    #         time.sleep(2)
    #         self.set_color("Red")
    #     else:
    #         """
    #         Solving uncertainty when setting yellow
    #         """
    #         self.set_color("Red")
    #     self.running()

    def running(self):
        """
        Variant 2
        Infinite loop method
        :return: None or
        """
        while True:
            if self.get_color() == "Red":
                print(self.get_color())
                time.sleep(7)
                print("Yellow")
                time.sleep(2)
                self.set_color("Green")
            elif self.get_color() == "Green":
                print(self.get_color())
                time.sleep(5)
                print("Yellow")
                time.sleep(2)
                self.set_color("Red")
            else:
                print("Incorrect color sequence")
                return


    def set_color(self, color):
        """
        setter
        :param color: "Green" or "Red
        :return: None
        """
        self.__color = color

    def get_color(self):
        """
        getter
        :return: current color "Red" or "Green"
        """
        return self.__color


tl = TrafficLight("Green")
tl.running()


