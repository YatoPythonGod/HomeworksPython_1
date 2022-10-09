# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот
# день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def check_weekend():
    number = input('Please enter number: ')
    if number.isdigit():
        number = int(number)
        if 0 < number < 8:
            if number in [6, 7]:
                print('да')
            else:
                print('нет')
        else:
            print('The number should be in the range from 1 to 7')
            check_weekend()
    else:
        print('Enter an integer from 1 to 7')
        check_weekend()


check_weekend()
