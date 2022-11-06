# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь. например,
# 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения.
# Предусмотреть все варианты, сделать обработку исключений

import re
from math import sqrt


def solv_quad_equat(quadratic_equations: str):
    """Returns the roots of a quadratic equation in the form of a dictionary"""
    pattern = r'(\-?\d+(?:[.,]{1}\d+)?)\*x\^2[+-]?(\d+(?:[.,]{1}\d+)?)?\*?x?[+-]?(\d+(?:[.,]{1}\d+)?)?\=0'
    match = re.search(pattern, quadratic_equations)
    if match:
        a = float(match.group(1).replace(',', '.'))
        b = float(match.group(2).replace(',', '.')) if match.group(2) else 0
        c = float(match.group(3).replace(',', '.')) if match.group(3) else 0
        if not b and not c:
            return {'x': 0}
        elif b and not c:
            return {'x1': 0, 'x2': -(round(b / a, 2))}
        elif not b and c:
            return {'x1': sqrt(-(c / a)), 'x2': -(sqrt(-(c / a)))} if -(c / a) > 0 else \
                f'The quadratic equation: {quadratic_equations} - has no real roots'
        else:
            d = b ** 2 - 4 * a * c
            if d < 0:
                print(f'The quadratic equation: {quadratic_equations} - has no real roots')
                return None
            elif d == 0:
                return {'x': round(-(b / 2 * a), 2)}
            else:
                return {'x1': round((-b + sqrt(d)) / (2 * a), 2), 'x2': round((-b - sqrt(d)) / (2 * a), 2)}
    else:
        print(solv_quad_equat(input('Please inter quadratic equations (format: 6*x^2+5*x+6=0): ').lower()))


# user_quadratic_equations = input('Please enter quadratic equations: ').lower()
# print(solv_quad_equat(user_quadratic_equations))

print(solv_quad_equat('3.1*x^2+5*x+2=0'))
print(solv_quad_equat('5,4*x^2+5*x=0'))
print(solv_quad_equat('10*x^2=0'))
