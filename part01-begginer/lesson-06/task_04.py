"""
4. Реализуйте базовый класс Car.

• у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
• опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
• добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
• для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        """
        constructor
        :param speed: number
        :param color: string
        :param name: string
        :param is_police: boolean
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """
        method - car move
        :return: print notification about moving
        """
        print(f"Car [{self.name}] is driving")

    def stop(self):
        """
        method - car stop
        :return: print notification about stop
        """
        print(f"Car [{self.name}] is stopped")

    def turn(self, direction):
        """
        method - car turn on left or rigth
        :param direction:
        :return:
        """
        print(f'Car [{self.name}] turn on {direction}')

    def show_speed(self):
        print(f"Car [{self.name}] has a speed of {self.speed} km/h")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """
        method override
        added
        - new car definition
        - speed check (60 km/h) and notification
        :return: None
        """
        print(f"Town-car [{self.name}] has a speed of {self.speed} km/h")
        if self.speed > 60:
            print(f'Town-car [{self.name}] exceeded speed')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """
        method override
        added
        - new car definition
        - speed check (40 km/h) and notification
        :return: None
        """
        print(f"Work-car [{self.name}] has a speed of {self.speed} km/h")
        if self.speed > 40:
            print(f'Work-car [{self.name}] exceeded speed')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


# test method for trying use objects method
def show_info(current_car):
    current_car.go()
    current_car.turn("left")
    current_car.show_speed()
    current_car.stop()


# test list
car_list = [
    TownCar(180.0, "white", "BMW-X3", False),
    SportCar(360.0, "black", "Audi-TT", False),
    WorkCar(140.0, "grey", "Renault Logan", False),
    PoliceCar(180.0, "white", "Opel Astra", True),
]

# for testing objects
for el in car_list:
    show_info(el)
    print('-----------------')
