"""Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
Через строку нельзя решать.

*Пример:*

- 6782 -> 23
- 0,56 -> 11"""

from decimal import Decimal


def check_digit():
    """Check that the input is a number"""
    while True:
        try:
            number = float(input('Please enter a number: '))
            return number
        except ValueError as e:
            print(e)


def sum_digits(number):
    number = Decimal(number).quantize(Decimal('1.00000000000'))
    result = 0
    while number - int(number) != 0:
        number *= 10

    while number // 10 != 0:
        result += number % 10
        number //= 10

    return int(result + number)


my_number = check_digit()
print(sum_digits(my_number))





