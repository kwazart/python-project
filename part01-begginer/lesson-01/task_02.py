# try string to int
while True:
    seconds = input('Input seconds as integer digital: ')

    try:
        seconds = int(seconds)
        break
    except ValueError:
        print('NOT INT. Try again')

hours = seconds // (60 * 60)
seconds = seconds % (60 * 60)
minutes = seconds // 60
seconds = seconds % 60

print("{:02d}".format(hours) + ":{:02d}".format(minutes) + ":{:02d}".format(seconds))
