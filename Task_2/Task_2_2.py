# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def check_int():
    """Check that the input is a number"""
    while True:
        try:
            number = int(input('Please enter a number: '))
            return number
        except ValueError as error:
            print(error)


def get_factorial_list(count):
    """Creates a sequence of factorials"""
    a = 1
    result = []
    for i in range(1, count + 1):
        if i != 1:
            a += a * (i - 1)
        result.append(a)
    return result


print(get_factorial_list(check_int()))
