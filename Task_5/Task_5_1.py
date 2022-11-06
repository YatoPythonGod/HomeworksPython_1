# задача 1. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

import time
import random


def check_int(message='Please enter a number: '):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError as error:
            print(error)


def roll(count, player_1='Player 1', player_2='Player 2'):
    print('_' * 40, 'The lot will decide who goes first!', '_' * 40, sep='\n')
    time.sleep(0.5)
    roll_player_1 = random.randint(0, count)
    print(f'{player_1} rolls the dice: {roll_player_1}')
    time.sleep(1)
    roll_player_2 = random.randint(0, count)
    print(f'{player_2} rolls the dice: {roll_player_2}')
    time.sleep(0.5)
    if roll_player_1 > roll_player_2:
        print(f'{player_1} win, your move is the first!')
        return 1
    elif roll_player_2 > roll_player_1:
        print(f'{player_2} win, your move is the first!')
        return 2
    else:
        print('Incredibly its a draw, lets try again!')
        time.sleep(1)
        roll(count)


def candy(opponent='player', bank=2021, step=28):
    if opponent == 'player':
        active = roll(100)
        while bank != 1:
            player_step = check_int(f'Player {active} please enter a number from 1 to {step}: ')
            while step < player_step or player_step < 1 or bank - player_step < 1:
                print(f'Player{active} you are not playing by the rules!')
                player_step = check_int(f'Player {active} please enter a number from 1 to {step}: ')
            bank -= player_step
            print('_' * 40, f'| There are {bank} candies left in the box |', '_' * 40, sep='\n')
            active = 2 if active == 1 else 1
        active = 2 if active == 1 else 1
        print(f'!!! Player{active} win !!!')

    if opponent == 'AI':
        active = roll(100, player_2='AI')
        while bank != 1:
            if active == 1:
                player_step = check_int(f'Player {active} please enter a number from 1 to {step}: ')
                while step < player_step or player_step < 1 or bank - player_step < 1:
                    print(f'Player{active} you are not playing by the rules!')
                    player_step = check_int(f'Player {active} please enter a number from 1 to {step}: ')
                bank -= player_step
                print('_' * 40, f'| There are {bank} candies left in the box |', '_' * 40, sep='\n')
                active = 2 if active == 1 else 1
            else:
                player_step = bank % (step + 2) if bank > step + 2 else bank - 1
                if player_step == 0:
                    player_step = 1
                print(f'AI took {player_step} candies from the box')
                bank -= player_step
                print('_' * 40, f'| There are {bank} candies left in the box |', '_' * 40, sep='\n')
                active = 2 if active == 1 else 1
        print('!!! Player 1 win !!!' if active == 2 else '!!! AI win !!!')


if __name__ == '__main__':
    candy(opponent='AI')