"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""


with open("task02-example.txt", "r") as f:
    row = 0
    for line in f:
        row += 1
        print(f'Line {row} has {len(line.split(" "))} words')
print(f'Quantity line is {row}')
