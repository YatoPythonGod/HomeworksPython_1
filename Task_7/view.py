from easygui import msgbox
from easygui import buttonbox
from easygui import textbox
from logger import logger_main_choice


@logger_main_choice
def main_choice_window():
    title_txt = 'Simple calc'
    msg_txt = 'Выберете опцию: '

    btn1 = 'Калькулятор'
    btn2 = 'Калькулятор комплексных чисел'
    btn3 = 'Журнал логов'
    btn4 = 'Выйти'

    btn_list = []
    btn_list.append(btn1)
    btn_list.append(btn2)
    btn_list.append(btn3)
    btn_list.append(btn4)

    images_path = ('C:\\Projects\\HomeworksPython_1\\Task_7\\icons\\calc.png',
                   'C:\\Projects\\HomeworksPython_1\\Task_7\\icons\\complex.png',
                   'C:\\Projects\\HomeworksPython_1\\Task_7\\icons\\log.png',
                   'C:\\Projects\\HomeworksPython_1\\Task_7\\icons\\exit.png')

    choise_dict = dict(zip(images_path, btn_list))

    user_choice = buttonbox(msg=msg_txt, title=title_txt, choices=btn_list, image=images_path)
    return choise_dict[user_choice] if user_choice in choise_dict else user_choice


def result_window(title_txt, msg_txt):
    result = msgbox(title=title_txt, msg=msg_txt)
    return result


def exit_window():
    title_txt = 'Simple calc'
    msg_txt = 'До новых встреч!'
    msgbox(title=title_txt, msg=msg_txt)


def log_window():
    title_txt = 'Файл логов'
    msg_txt = 'Ну что, посмотрим логи?'
    with open('C:\Projects\HomeworksPython_1\Task_7\calc_log.log') as f:
        file_content = f.read()
        textbox(msg=msg_txt, title=title_txt, text=file_content)



