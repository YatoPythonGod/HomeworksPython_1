from logger import logger_calc

# метод (swap_mark) меняет знак перед цифрой
def swap_mark(expr: str):

    start = ""
    new_expression = ""

    if expr[0].isdigit():
        start = "-"
    elif expr[0] == "+":
        expr = expr[1:]
        start = "-"

    for i, mark in enumerate(expr):
        if mark == "-" and i == 0:
            new_expression += "+"
        elif mark == "-":
            new_expression += "+"
        elif mark == "+" and i != 0:
            new_expression += "-"
        else:
            new_expression += mark

    return start + new_expression


# метод (parenthesis_handling_addition) обрабатывает выражения в скобках. если перед скобками
# стоит знак минус, то в скобках меняются знаки "+" и "-" на противоположные. Пример: -(-4 + 2i) => +(+4 -2i)
def parenthesis_handling_addition(data: str):

    data = data.replace(" ", "")
    start = False
    index_start = None
    result = ""

    for i, mark in enumerate(data):
        if mark == "-" and data[i+1] == "(":
            index_start = i + 2
            start = True
            result += "+("
        elif mark == ")" and start:
            index_end = i
            replacement_data = data[index_start:index_end]
            start = False
            result += swap_mark(replacement_data) + ")"
        elif not start:
            result += mark
    return result


@logger_calc
def complex_calc_func(data):

    # Рабочая часть, если в выражении нет умножения или дееления. Можно считать раные варианты сложения и вычитания
    if "/" not in data and "*" not in data:

        data = parenthesis_handling_addition(data)
        data = data.replace("(", "").replace(")", "").replace(" ", "").replace("-", "+-")
        data = data.split("+")

        reals = []
        nums_i = []

        for num in data:
            if "i" not in num and num != "":
                reals.append(num)
            elif "i" in num:
                nums_i.append(num)

        sum_reals = 0
        for i, num in enumerate(reals):
            sum_reals += int(reals[i])

        sum_nums_i = 0
        for i, num in enumerate(nums_i):
            sum_nums_i += int(num[:-1])

        if sum_nums_i >= 0:
            return f'{sum_reals} + {sum_nums_i}i'
        return f'{sum_reals}{sum_nums_i}i'

    elif "/" in data or "*" in data:
        return "to be continued"

    else:
        return "to be continued"