"""
2. Реализовать класс Road (дорога).

• определить атрибуты: length (длина), width (ширина);
• значения атрибутов должны передаваться при создании экземпляра класса;
• атрибуты сделать защищёнными;
• определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
• использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
• проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:

    def __init__(self, length, width):
        """
        constructor
        :param length: integer value (road length) from user
        :param width: integer value (road width) from user
        """
        self._length = length
        self._width = width

    def mass_calculation(self):
        """
        Calculation of the total mass of asphalt taking into account the length and width of the road.
        asphalt_mass_to_cover_one_sq_meter - local value
        road_bed_thickness - local value
        :return: integer value - multiplication of data from user and local data
        """
        asphalt_mass_to_cover_one_sq_meter = 25
        road_bed_thickness = 5
        return self._length * self._width * asphalt_mass_to_cover_one_sq_meter * road_bed_thickness


# test
road_1 = Road(10, 20)
road_2 = Road(30, 50)
road_3 = Road(20, 5000)

print(road_1.mass_calculation())
print(road_2.mass_calculation())
print(road_3.mass_calculation())

