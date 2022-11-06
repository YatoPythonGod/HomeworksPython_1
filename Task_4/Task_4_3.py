# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
from itertools import zip_longest


def create_file(text: str, file_name: str):
    """creates a file"""
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)


def read_file(file_name: str):
    """reads the file"""
    with open(file_name, encoding='utf-8') as f:
        return f.read()


def create_polynomial(degree):
    """creates a random polynomial of the entered degree"""
    coefficients = (str(randint(0, 100)) if i != 0 else str(randint(1, 100)) for i in range(degree))
    polynomials = (f'x**{i}' if i != 1 else 'x' for i in range(degree, 0, -1))
    return ' + '.join(
        [f'{coefficient}*{polynomials}' if coefficient != '1' else polynomials for coefficient, polynomials in
         zip_longest(coefficients, polynomials, fillvalue='') if coefficient != '0']) + f' + {str(randint(1, 100))} = 0'


user_polynomial = create_polynomial(10)
print(user_polynomial)

create_file(user_polynomial, 'task_4_3.txt')
print('READ:', read_file('task_4_3.txt'), sep='\n')
