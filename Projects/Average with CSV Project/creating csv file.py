import csv


data = [
    ['mandana', 5, 7, 3, 15],
    ['hamid', 3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1],
    ['sina', 19, 10, 19, 6, 8, 14, 3],
    ['sara', 0, 5, 20, 14],
    ['soheila', 13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7],
    ['ali', 1, 9],
    ['sarvin', 0, 16, 16, 13, 19, 2, 17, 8],
    ['hamed', 13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7]
]
with open('data.csv', 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

