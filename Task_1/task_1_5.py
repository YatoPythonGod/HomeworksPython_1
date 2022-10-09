# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
#
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
#
# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint


def create_matrix(line: int, column: int):
    return [[randint(1, 100) for _ in range(column)] for _ in range(line)]


def sort_matrix(matrix: list):
    len_matrix = len(matrix)
    len_line = len(matrix[0])
    sort_list = []
    for line in matrix:
        sort_list.extend(line)
    sort_list = iter(sorted(sort_list))

    return [[next(sort_list) for _ in range(len_line)] for _ in range(len_matrix)]


my_matrix = create_matrix(5, 5)

for line in my_matrix:
    print(*line)

print('*' * 20)

for line in sort_matrix(my_matrix):
    print(*line)
