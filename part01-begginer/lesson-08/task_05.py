"""
Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
"""


class OfficeEquipment:
    def __init__(self, item_name, cost, brand_name):
        """
        constructor. common params
        :param item_name: item title
        :param cost: cost by 1 item
        :param brand_name: company brand title
        """
        self.item_name = item_name
        self.cost = cost
        self.brand = brand_name


class Printer(OfficeEquipment):
    def __init__(self, item_name, cost, brand_name, is_laser: bool, is_colored: bool, speed):
        """
        constructor child class. unique params
        :param item_name: parent class
        :param cost: parent class
        :param brand_name: parent class
        :param is_laser: bool (printer has laser, but has not jet function)
        :param is_colored: bool (printer has color print, not only B/W )
        :param speed: number (print speed)
        """
        self.is_laser = is_laser
        self.is_colored = is_colored
        self.speed = speed
        super().__init__(item_name, cost, brand_name)


class Scanner(OfficeEquipment):
    def __init__(self, item_name, cost, brand_name, is_colored: bool, speed, resolution):
        """
        constructor child class. unique params
        :param item_name: parent class
        :param cost: parent class
        :param brand_name: parent class
        :param is_colored: is_colored: bool (scanner has color scanning, not only B/W )
        :param speed: number (scanning speed)
        :param resolution: width and height
        """
        self.is_colored = is_colored
        self.speed = speed
        self.resolution = resolution
        super().__init__(item_name, cost, brand_name)


class Xerox(OfficeEquipment):
    def __init__(self, item_name, cost, brand_name,  resolution):
        """
        constructor child class. unique params
        :param item_name: parent class
        :param cost: parent class
        :param brand_name: parent class
        :param resolution: width and height
        """
        self.resolution = resolution
        super().__init__(item_name, cost, brand_name)


class Warehouse:
    def __init__(self):
        self.office_equipment_list = dict()

    def add_item(self, item: OfficeEquipment, item_count=1):
        """
        adding item and quantity, default quantity equals 1
        :param item: item object (one of child OfficeEquipment class)
        :param item_count: number (quantity)
        :return: None
        """
        self.office_equipment_list[item] = item_count

    def send_item(self, item: OfficeEquipment, item_count=1):
        """
        sending items + reducing the number of items. do not delete object from dictionary
        only quantity reducing if we can
        :param item: item object (one of child OfficeEquipment class)
        :param item_count: number (quantity)
        :return: None
        """
        if self.office_equipment_list.get(item) >= item_count:
            self.office_equipment_list[item] = self.office_equipment_list.get(item) - item_count
        else:
            print(f"There is not enough product balance. "
                  f"Current balance: {self.office_equipment_list[item]}"
                  f"Try send: {item_count}")
