a = 2
b = 3.5
c = "4"
d = True
e = [5, "6", "7.0"]
f = (8, "9", 10.1)
g = {"11": 12, "12": 13}

print(a, b, c, d, e, f, g)

# standard input is string always
user_var1 = input('Input string: ')
print('Of course. Always it is string')

# try string to int
while True:
    user_var2 = input('Input int: ')

    try:
        user_var = int(user_var2)
        print('Well done. This is int. Buy')
        break
    except ValueError:
        print('NOT INT. Try again')
