# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
#
# *Пример:*
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
#
#     [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]
# Рекомендация на каникулы - посмотреть библиотеку EasyGUI, БД SQLite.


def max_seq(array):
    uniq_el = set(array)
    array_set = set(array)
    sum_seq = []
    while uniq_el:
        sub_lst = []
        min_num = min(uniq_el)
        if min_num + 1 in array_set:
            sub_lst.append(min_num)
            for i in range(len(array_set)):
                if min_num + 1 in array_set:
                    sub_lst.append(min_num + 1)
                    min_num += 1
                else:
                    break
            sum_seq.append(sub_lst)
        uniq_el.discard(min(uniq_el))
    result = sorted(sum_seq, key=lambda x: len(x))
    return [result[-1][0], result[-1][-1]]


print(max_seq([1, 5, 2, 3, 4, 1, 7, 8, 15, -1, 6, 0]))
