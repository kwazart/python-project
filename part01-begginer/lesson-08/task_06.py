"""
6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
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
        self.item_type = "Printer"
        super().__init__(item_name, cost, brand_name)

    def __str__(self):
        return f'Type: {self.item_type}\n' \
               f'Company: {self.brand}\n' \
               f'Model: {self.item_name}\n' \
               f'Laser: {self.is_laser == True if "Yes" else "No"}\n' \
               f'Color: {self.is_colored == True if "Yes" else "No"}\n' \
               f'Speed: {self.speed} per minutes'


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
        self.item_type = "Scanner"
        super().__init__(item_name, cost, brand_name)

    def __str__(self):
        return f'Type: {self.item_type}\n' \
               f'Company: {self.brand}\n' \
               f'Model: {self.item_name}\n' \
               f'Color: {self.is_colored == True if "Yes" else "No"}\n' \
               f'Speed: {self.speed} per minutes\n' \
               f'Resolution: {self.resolution}'


class Xerox(OfficeEquipment):
    def __init__(self, item_name, cost, brand_name, resolution):
        """
        constructor child class. unique params
        :param item_name: parent class
        :param cost: parent class
        :param brand_name: parent class
        :param resolution: width and height
        """
        self.resolution = resolution
        self.item_type = "Xerox"
        super().__init__(item_name, cost, brand_name)

    def __str__(self):
        return f'Type: {self.item_type}\n' \
               f'Company: {self.brand}\n' \
               f'Model: {self.item_name}\n' \
               f'Resolution: {self.resolution}'


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
        print("ADDING")
        # validate example
        if item in self.office_equipment_list:
            self.office_equipment_list[item] += item_count
        else:
            self.office_equipment_list[item] = item_count
        print(f'{item_count} {item.item_type} was added\n'
              f'---------------------')

    def send_item(self, item: OfficeEquipment, item_count=1):
        """
        sending items + reducing the number of items. do not delete object from dictionary
        only quantity reducing if we can
        :param item: item object (one of child OfficeEquipment class)
        :param item_count: number (quantity)
        :return: None
        """
        print("SENDING")
        if self.office_equipment_list.get(item) >= item_count:
            self.office_equipment_list[item] = self.office_equipment_list.get(item) - item_count
        else:
            print(f"There is not enough product balance. "
                  f"Current balance: {self.office_equipment_list[item]} "
                  f"Try send: {item_count}\n"
                  f"---------------------")

    def display_items(self):
        print("Item name Quantity")
        for k, v in self.office_equipment_list.items():
            print(f'{k}\nQuantity: {v}\n---------------------')


# test. fill in the code
printer = Printer("Model1", 1200, "Canon", True, False, 24)
scanner = Scanner("Model1", 1000, "HP", True, 20, "1920x1080")

warehouse = Warehouse()
warehouse.add_item(printer, 3)
warehouse.add_item(scanner, 5)
warehouse.send_item(printer, 4)
warehouse.display_items()
