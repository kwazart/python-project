# try string to float
while True:
    proceeds = input('Input proceeds : ')
    outgoings = input('Input outgoings: ')

    try:
        proceeds = float(proceeds)
        outgoings = float(outgoings)
        break
    except ValueError:
        print('NOT FLOAT OR INT. Try again')

# profit
profit = proceeds - outgoings
if profit > 0:
    print('The firm has a profit')
    print('profitability - ' + str(round(profit / proceeds, 2)))

    while True:
        employees = input('Input employees (integer) : ')
        try:
            employees = int(employees)
            break
        except ValueError:
            print('NOT INT. Try again')

    print('profit by a employee - ' + str(round(profit / employees, 3)))

elif profit < 0:
    print('The firm has not a profit')
else:
    print('Smooth work')