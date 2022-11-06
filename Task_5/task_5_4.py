# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
#
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2 + 6*x + 3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

import re


def polynomial_to_dict(polynomial):
    pattern = r"(?:\s?([+-])\s?)?(\d+(?:[.,]{1}\d+)?)\*?(x\^?\d?\d?)?"
    list_polynomial = re.findall(pattern, polynomial)
    return {el[2]: int(el[1]) * -1 if el[0] == '-' else int(el[1]) for el in list_polynomial}


def add_polynomials(polynomial_1, polynomial_2):
    polynomial_1 = polynomial_to_dict(polynomial_1)
    polynomial_2 = polynomial_to_dict(polynomial_2)
    result = {}
    for key, value in polynomial_1.items():
        if key in polynomial_2:
            result[key] = value + polynomial_2.get(key)
        else:
            result[key] = value
    for key, value in polynomial_2.items():
        if key not in polynomial_1:
            result[key] = value
    add_polynomial = ''
    for i, el in enumerate(sorted(result.items(), key=lambda x: x[0], reverse=True)):
        if i == 0:
            if el[1] == 0:
                continue
            add_polynomial += f'{el[1]}*{el[0]}'
        else:
            if el[0]:
                if el[1] == 0:
                    continue
                elif el[1] > 0:
                    add_polynomial += f' + {el[1]}*{el[0]}'
                else:
                    add_polynomial += f' - {-1 * el[1]}*{el[0]}'
            else:
                if el[1]:
                    if el[1] > 0:
                        add_polynomial += f' + {el[1]}'
                    else:
                        add_polynomial += f' - {-1 * el[1]}'

    return add_polynomial


print(add_polynomials('5*x^99 - 7*x^2 + 6', '7*x^2 - 6*x - 3'))
