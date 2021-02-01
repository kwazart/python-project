# try string to int
while True:
    number = input('Input integer digital: ')

    try:
        number = int(number)
        break
    except ValueError:
        print('NOT INT. Try again')

double_number = number * 10 + number;
triple_number = number * 100 + double_number

print(number + double_number + triple_number)
