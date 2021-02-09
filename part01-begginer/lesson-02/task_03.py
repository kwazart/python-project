"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
year_periods = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "autumn": [9, 10, 11]
}

while True:
    month_number = input('Input month number (from 1 to 12, 0 - exit): ')

    try:
        month_number = int(month_number)
        if 1 <= month_number <= 12:
            for key in year_periods:
                if month_number in year_periods.get(key):
                    print(key, end="\n\n")
        elif month_number == 0:
            break
        else:
            print("Incorrect choice. Try again.\n")
    except ValueError:
        print('NOT INT. Try again')