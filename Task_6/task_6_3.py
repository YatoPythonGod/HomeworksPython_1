# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
# и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

import csv


def int_input(text):
    """checks input for an integer"""
    while True:
        try:
            user_input = int(input(text))
            return user_input
        except ValueError as error:
            print(error)


def create_sum_table(name_table='summary_table.csv'):
    """creates a csv file of the results table"""
    try:
        with open(name_table, 'x', newline='', encoding='utf-8') as file:
            names = ["Команда", "Всего игр", "Побед", "Ничьих", "Поражений", "Всего очков"]
            file_writer = csv.DictWriter(file, fieldnames=names)
            file_writer.writeheader()
    except FileExistsError:
        pass


def table_to_dict(name_table='summary_table.csv'):
    """reads the file - 'name_table' and converts it into a dictionary"""
    with open(name_table, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return {row.pop("Команда"): row for row in reader}


def game_input(count):
    """accepts the number of games the results of games and returns a summary dictionary"""
    create_sum_table()
    summary_table = table_to_dict()
    lose_team = {'Всего игр': '1', 'Побед': '0', 'Ничьих': '0', 'Поражений': '1', 'Всего очков': '0'}
    win_team = {'Всего игр': '1', 'Побед': '1', 'Ничьих': '0', 'Поражений': '0', 'Всего очков': '3'}
    draw = {'Всего игр': '1', 'Побед': '0', 'Ничьих': '1', 'Поражений': '0', 'Всего очков': '1'}

    for _ in range(count):
        team_1, score_1, team_2, score_2 = map(lambda s: s.capitalize(), input('Введите результаты матча в формате - '
                                                                               '"Первая команда;Забито первой командой;'
                                                                               'Вторая команда;Забито второй командой": ').replace(
            ' ', '').split(';'))
        if int(score_1) < int(score_2):
            team_1, team_2 = team_2, team_1

        if int(score_1) == int(score_2):
            for team in [team_1, team_2]:
                if team in summary_table:
                    for key, value in summary_table[team].items():
                        summary_table[team][key] = str(int(value) + int(draw[key]))
                else:
                    summary_table[team] = draw.copy()
        else:
            if team_1 in summary_table:
                for key, value in summary_table[team_1].items():
                    summary_table[team_1][key] = str(int(value) + int(win_team[key]))
            else:
                summary_table[team_1] = win_team.copy()

            if team_2 in summary_table:
                for key, value in summary_table[team_2].items():
                    summary_table[team_2][key] = str(int(value) + int(lose_team[key]))
            else:
                summary_table[team_2] = lose_team.copy()

    return dict(sorted(summary_table.items(), key=lambda x: int(x[1]['Всего очков']), reverse=True))


def update_sum_table(dict_table, name_table='summary_table.csv'):
    """updates the table in the file- name_table"""
    with open(name_table, 'a', encoding='utf-8') as file:
        names = ["Команда", "Всего игр", "Побед", "Ничьих", "Поражений", "Всего очков"]
        file_writer = csv.DictWriter(file, fieldnames=names)
        for k, v in dict_table.items():
            v.update({"Команда": k})
            file_writer.writerow(v)


def show_sum_table(name_table='summary_table.csv'):
    """shows the user a table of results from a file - name_table"""
    with open(name_table, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for i, row in enumerate(reader):
            if i == 0:
                print('\nКоманда      | Всего игр | Побед | Ничьих | Поражений | Всего очков\n')
            print(
                f'{i + 1}. {row["Команда"].ljust(9)} | {row["Всего игр"]} | {row["Побед"]} | {row["Ничьих"]} | {row["Поражений"]} | {row["Всего очков"]}', )


if __name__ == '__main__':
    user_count = int_input('Введите кол-во игр: ')
    sum_table = game_input(user_count)
    update_sum_table(sum_table)
    show_sum_table()
