# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N,
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

def check_int(text: str):
    """Check that the input is integer"""
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError as error:
            print(error)


def check_digit(text: str):
    """Check that the input is a number"""
    while True:
        try:
            number = float(input(text))
            return number
        except ValueError as e:
            print(e)


def distance(n: int):
    """Returns the length of the segment in n-dimensional space"""
    first_point = []
    second_point = []
    for i in range(1, n + 1):
        first_point.append(check_digit(f'Please enter the coordinate {i} of the first point: '))
        second_point.append(check_digit(f'Please enter the coordinate {i} of the second point: '))
    result = 0
    for one, two in zip(first_point, second_point):
        result += (one - two) ** 2

    return result ** 0.5


print(distance(check_int('Please enter dimension N-dimensional space: ')))
