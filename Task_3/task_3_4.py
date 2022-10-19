# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def check_int():
    """Check that the input is a number"""
    while True:
        try:
            number = int(input('Please enter a number: '))
            return number
        except ValueError as error:
            print(error)


def make_bin_to_dec(number: int):
    """converts decimal to binary"""
    dec_lst = []
    while True:
        dec_lst.append(str(number % 2))
        number //= 2
        if number == 0:
            break
    return int(''.join(dec_lst[::-1]))


print(make_bin_to_dec(check_int()))