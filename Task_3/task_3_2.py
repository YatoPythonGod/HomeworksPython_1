# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil


def get_lst_sum(lst: list):
    """returns a list consisting of the sum of the first and last elements of the input list"""
    return [lst[i] * lst[-1 - i] for i in range(ceil(len(lst) / 2))]


print(get_lst_sum([2, 3, 4, 5, 6]))
print(get_lst_sum([2, 3, 5, 6]))
