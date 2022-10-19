# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, проверяем это утверждение 100 раз,
# с помощью модуля time выводим на экран , сколько времени отработала программа.

from random import choice
from random import randint
from time import perf_counter


def true_or_false():
    """random return True or False"""
    return choice([True, False])


def truth_check():
    """checking the truth of the expression ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z"""
    left = False
    right = False
    for _ in range(randint(5, 25)):
        predicate = true_or_false()
        left = left or predicate
        right = right and not predicate
    return not left == right


start = perf_counter()
for i in range(100):
    print(truth_check())

print(f'Program execution time: {perf_counter() - start}')
