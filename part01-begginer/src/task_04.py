# try string to int
while True:
    number = input('Input integer digital greater than 0: ')

    try:
        number = int(number)
        if number <= 0:
            continue
        break
    except ValueError:
        print('NOT INT. Try again')

isNextNumber = True
max_num = 0
while isNextNumber:
    if max_num < number % 10:
        max_num = number % 10
    number = number // 10
    if number == 0:
        break

print("max digital = " + str(max_num))
