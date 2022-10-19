# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) ,
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место
# и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций.
# И далее в конце опять вывести на экран как таблицу.


import random


def check_int(text: str):
    """Check that the input is a number"""
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError as e:
            print(e)


def create_matrix():
    """creates a matrix of the specified dimension"""
    number_rows = check_int('Please enter the number of rows in the array: ')
    number_columns = check_int('Please enter the number of columns in the array: ')
    if number_rows * number_columns % 2 != 0:
        print('Sorry...The number of array elements must be even!')
        return create_matrix()
    return [[random.randint(1, 100) for _ in range(number_columns)] for _ in range(number_rows)]


def mix_matrix(matrix: list):
    """shuffles the matrix"""
    number_column = len(matrix[0])
    number_row = len(matrix)
    size_matrix = len(matrix[0]) * len(matrix)
    unpack_matrix = [el for row in matrix for el in row]
    second_part_index = list(range(int(size_matrix / 2), size_matrix))
    count_iter = 0
    for i, el in enumerate(unpack_matrix[:int(size_matrix / 2)]):
        second_el_index = random.choice(second_part_index)
        second_part_index.remove(second_el_index)
        unpack_matrix[i], unpack_matrix[second_el_index] = unpack_matrix[second_el_index], unpack_matrix[i]
        count_iter += 1
    unpack_matrix = iter(unpack_matrix)
    print(f'number of iterations = {count_iter}')
    return [[next(unpack_matrix) for _ in range(number_column)] for _ in range(number_row)]


my_matrix = create_matrix()
for row in my_matrix:
    print(row)
print("*" * 15)
for row in mix_matrix(my_matrix):
    print(row)
