# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from math import sqrt
from math import ceil


def check_int(text: str):
    """Check that the input is a number"""
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError as e:
            print(e)


def create_lst_simp_divisor(number):
    """returns a list of prime divisors of a given number"""
    result = []
    for i in range(2, ceil(sqrt(number))):
        if number % i == 0:
            for j in range(2, ceil(sqrt(i))):
                if i % j == 0:
                    break
            else:
                result.append(i)
    return result


print(create_lst_simp_divisor(600851475143))
