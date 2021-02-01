# try string to int
while True:
    first_distance = input('Input first distance : ')
    total_distance = input('Input total distance : ')

    try:
        first_distance = float(first_distance)
        total_distance = float(total_distance)
        break
    except ValueError:
        print('NOT FLOAT OR INT. Try again')

i = 1
print(f'{i}-day: %.2f' % first_distance)
while first_distance <= total_distance:
    i += 1
    first_distance = first_distance * 1.1
    print(f'{i}-day: %.2f' % first_distance)

print(f"On the {i} day, the athlete achieved a result of at least {total_distance} km.")