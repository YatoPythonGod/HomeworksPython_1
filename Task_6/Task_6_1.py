# 1 - Создайте программу для игры в ""Крестики-нолики"".

import time
import random


class Board:
    DECODE_MARK = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}

    def __init__(self):
        self.board_plate = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def __str__(self):
        return str(self.board_plate)

    def show_board(self):
        for i, v in enumerate(self.board_plate):
            print(f'  {v[0]} | {v[1]} | {v[2]}  ')
            print(' ___ ___ ___' if i < 2 else '')

    def change_board(self, number, mark):
        decode_num = Board.DECODE_MARK[number]
        while self.board_plate[decode_num[0]][decode_num[1]] in ('X', 'O'):
            print('Sorry this field is already occupied')
            decode_num = Board.DECODE_MARK[int(input('Please enter the field number: '))]
        self.board_plate[decode_num[0]][decode_num[1]] = mark

    def check_win(self):
        for i in range(3):
            if self.board_plate[i].count(self.board_plate[i][0]) == len(self.board_plate[i]):
                return True
        for i in range(3):
            if self.board_plate[0][i] == self.board_plate[1][i] == self.board_plate[2][i]:
                return True
        if self.board_plate[0][0] == self.board_plate[1][1] == self.board_plate[2][2] or self.board_plate[0][2] == \
                self.board_plate[1][1] == self.board_plate[2][0]:
            return True


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


def ai_mind(board: list):
    for i in range(3):
        if board[i].count('O') == 2 and 'X' not in board[i]:
            for el in board[i]:
                if el != 'O':
                    return el
    for i in range(3):
        if board[i].count('X') == 2 and 'O' not in board[i]:
            for el in board[i]:
                if el != 'X':
                    return el
    for i in range(3):
        column = [board[0][i], board[1][i], board[2][i]]
        if column.count('O') == 2 and 'X' not in column:
            for el in column:
                if el != 'O':
                    return el
    for i in range(3):
        if column.count('X') == 2 and 'O' not in column:
            for el in column:
                if el != 'X':
                    return el
    diagonal_line_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_line_2 = [board[0][2], board[1][1], board[2][0]]
    for mark in ['O', 'X']:
        if diagonal_line_1.count(mark) == 2 and ('X' if mark == 'O' else 'O') not in diagonal_line_1:
            for el in diagonal_line_1:
                if el != mark:
                    return el
        elif diagonal_line_2.count(mark) == 2 and ('X' if mark == 'O' else 'O') not in diagonal_line_2:
            for el in diagonal_line_1:
                if el != mark:
                    return el
    if board[1][1] == 5:
        return 5
    else:
        pool = [board[i][j] for i in [0, 2] for j in [0, 2] if board[i][j] != 'X' and board[i][j] != 'O']
        if pool:
            return random.choice(pool)
        else:
            pool = [el for line in board for el in line if el.isdigit()]
            return random.choice(pool)


def game(ai='on'):
    new_board = Board()
    if ai == 'on':
        flag = roll(100, player_2='AI')
        new_board.show_board()
        for _ in range(9):
            if flag == 1:
                new_board.change_board(int(input('Please enter the field number: ')), 'X')
                new_board.show_board()
                if new_board.check_win():
                    print('Player win!!!')
                    return
                flag = 2
            else:
                print(f'Step AI: {ai_mind(new_board.board_plate)}\n')
                new_board.change_board(ai_mind(new_board.board_plate), 'O')
                new_board.show_board()
                if new_board.check_win():
                    print('AI win!!!')
                    return
                flag = 1
    else:
        pass


game()
