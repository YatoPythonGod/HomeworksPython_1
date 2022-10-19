# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def get_diff_decimal_v2(lst: list):
    """returns the difference between the maximum and minimum values of the fractional part of the elements"""
    new_lst = [i - int(i) for i in lst if i - int(i) != 0]
    return round(max(new_lst) - min(new_lst), 2)


print(get_diff_decimal_v2([1.1, 1.2, 3.1, 5, 10.01]))
