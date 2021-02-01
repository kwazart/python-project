"""
* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

# main variables
name = "name"
cost = "cost"
quantity = "quantity"
value = "value"
things = "th."

items_list = []
items_statistics = {
    name: [],
    cost: [],
    quantity: [],
    value: []
}

item_counter = 1
main_list = []


def add_new_item():
    item_name = input("\nEnter item name: ")

    while True:
        item_cost = input('Enter item cost: ')
        try:
            item_cost = float(item_cost)
            break
        except ValueError:
            print('NOT number. Try again')

    while True:
        item_quantity = input('Enter quantity: ')
        try:
            item_quantity = int(item_quantity)
            break
        except ValueError:
            print('NOT int. Try again')

    item = {name: item_name, cost: item_cost, quantity: item_quantity, value: things}
    return item


def fill_statistics():
    for item in main_list:
        items_statistics.get(name).append(item[1].get(name))
        items_statistics.get(cost).append(item[1].get(cost))
        items_statistics.get(quantity).append(item[1].get(quantity))
        items_statistics.get(value).append(item[1].get(value))


def print_statistic():
    for key, val in items_statistics.items():
        print("%15s" % key.upper(), end=" ")
        for i in val:
            print("|%15s" % i, end="")
        print("\n" + "-"*64)


while True:
    action = input("\n1 - Add items\n0 - Exit\nSelect variant: ")
    if action == "0":
        break
    elif action != "1":
        print("Incorrect choice. Try again")
        continue
    main_list.append((item_counter, add_new_item()))
    item_counter += 1

print(main_list)
fill_statistics()
print_statistic()
