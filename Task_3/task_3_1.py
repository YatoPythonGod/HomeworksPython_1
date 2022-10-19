# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# *Пример:*
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def get_sum_odd(lst: list):
    """returns the sum of the odd numbers in the list"""
    return sum([v for i, v in enumerate(lst) if i % 2 != 0])


print(get_sum_odd([2, 3, 5, 9, 3]))