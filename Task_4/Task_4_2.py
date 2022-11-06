# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

lst_1 = [1, 2, 3, 3, 4, 4, 777, 999, 0]


def get_uniq_el(lst: list):
    """returns a list of non-repeating elements of the source list"""
    uniq_el = set()
    repeat_el = set()
    for el in lst:
        if el in repeat_el:
            continue
        elif el in uniq_el:
            uniq_el.discard(el)
            repeat_el.add(el)
            continue
        uniq_el.add(el)

    return list(uniq_el)


print(get_uniq_el([1, 2, 3, 3, 4, 4, 777, 999, 0]))
