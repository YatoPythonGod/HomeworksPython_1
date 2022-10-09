# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция"
# "второе число") и выводит результат на экран.
#
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
#
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#
# Обратите внимание, что на вход программе приходят вещественные числа.

def check_digit():
    """Check that the input is a number"""
    while True:
        try:
            number = float(input('Введите число: '))
            return number
        except ValueError as e:
            print(e)


def calc(num1, num2, symbol):
    """a simple calculator that supports operations +, -, /, *, mod, pow, div"""
    calc_dict = {'+': num1 + num2, '-': num1 - num2, '/': num1 / num2, '*': num1 * num2, 'mod': num1 % num2,
                 'pow': num1 ** num2, 'div': num1 // num2}
    while symbol not in calc_dict:
        print('Поддерживаемые операции: +, -, /, *, mod, pow, div')
        symbol = input('Введите операцию: ')
    return calc_dict[symbol]


number1 = check_digit()
number2 = check_digit()
operation = input('Введите операцию: ')

try:
    print(calc(number1, number2, operation))
except ZeroDivisionError:
    print("Деление на 0!")