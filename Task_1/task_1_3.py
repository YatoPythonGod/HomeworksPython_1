# Напишите программу, которая принимает на вход координаты точки (X и Y) и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def get_quarter(x, y):
    if x == 0 and y == 0:
        print('Оху')
    elif x == 0 or y == 0:
        print('Coordinate axis X' if x == 0 else 'Coordinate axis Y')
    elif x > 0:
        print('I' if y > 0 else 'IV')
    else:
        print('II' if y > 0 else 'III')


get_quarter(0, 0)
