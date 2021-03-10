"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_int_date_list(cls, string_date):
        try:
            int_date_list = [int(element) for element in string_date.split("-")]
        except ValueError:
            return None
        return int_date_list

    @staticmethod
    def validate_date(int_date_list):
        if int_date_list is None:
            return False
        day = int_date_list[0]
        month = int_date_list[1]
        year = int_date_list[2]

        # check for negative values
        if day <= 0 or month <= 0 or year < 0:
            return False

        if not ((month == 1 and 1 <= day <= 31) or
                (month == 2 and 1 <= day <= 28) or
                (month == 3 and 1 <= day <= 31) or
                (month == 4 and 1 <= day <= 30) or
                (month == 5 and 1 <= day <= 31) or
                (month == 6 and 1 <= day <= 30) or
                (month == 7 and 1 <= day <= 31) or
                (month == 8 and 1 <= day <= 31) or
                (month == 9 and 1 <= day <= 30) or
                (month == 10 and 1 <= day <= 31) or
                (month == 11 and 1 <= day <= 30) or
                (month == 12 and 1 <= day <= 31)):
            return False
        return True


# test
check_list = [MyDate("32-04-1991"), MyDate("32-04-19fdg91"), MyDate("18-04-2000"), MyDate("10-15-1995"),
              MyDate("07-08-1500"), MyDate("02-06--1999"), MyDate("31-12-1850")]

for i, el in enumerate(check_list):
    print(f'test#{i}: {MyDate.validate_date(MyDate.get_int_date_list(el.date))} - {el.date}')


