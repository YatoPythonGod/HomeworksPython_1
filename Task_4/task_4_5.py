# Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа. Тема чат-бота любая.
# Просьба - постараться не использовать простой одномерный список или простой одномерный словарь.

import requests
import json
from bs4 import BeautifulSoup

link_dict = {'str': 'https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html',
             'list': 'https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html',
             'dict': 'https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html',
             'set': 'https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html'}


def save():
    # сохранить в json
    with open('link_dict.json', 'x', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(link_dict,
                            ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
    print('БД успещно сохранена')


def load():
    # загрузить из json
    with open('link_dict.json', 'r', encoding='utf-8') as f:  # открываем файл на чтение
        BD_local = json.load(f)  # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local


def get_methods(key: str):
    """Возвращает методы введеного типа данных в python"""
    if key in link_dict:
        if requests.get(link_dict[key]):
            content = requests.get(link_dict[key]).text
            soup = BeautifulSoup(content, "lxml")
            if key in ('str', 'list'):
                methods = soup.find("div", class_="table-wrapper").find_all('td')
                result = {v.text: methods[i].text for i, v in enumerate(methods, start=1) if i % 2 != 0}
                for k, v in result.items():
                    print(f'{k} - {v}')
                get_methods(input('Введите команду: ').lower())
            elif key == 'dict':
                methods = soup.find("div", class_="section").find_all('p')
                for el in methods:
                    print(el.text)
                get_methods(input('Введите команду: ').lower())
            else:
                methods = soup.find("div", class_="entry-content").find_all('li')
                for el in methods:
                    print(el.text)
                get_methods(input('Введите команду: ').lower())
        else:
            print('Упс.. Что-то пошло не так... Попробуйте запустить боты через некоторое время!')
            get_methods(input('Введите команду: ').lower())
    elif key == 'help':
        print(
            'Список комманд:\n- help - показать все команды\n- stop - выключить бота\n- str - методы строк'
            '\n- list - методы списков\n- dict - методы словарей\n- set - методы множеств')
        get_methods(input('Введите команду: ').lower())
    elif key == 'stop':
        print('Еще увидимся!')
        return
    else:
        print('Команда не найдена!')
        print(
            'Список комманд:\n- help - показать все команды\n- stop - выключить бота\n- str - методы строк'
            '\n- list - методы списков\n- dict - методы словарей\n- set - методы множеств')
        get_methods(input('Введите команду: ').lower())


try:
    save()
except FileExistsError:
    pass

link_dict = load()

print('Привет я бот, который умеет показывать методы разных типов данных!')
user_command = input('Введите команду: ').lower()
get_methods(user_command)
