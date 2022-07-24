from functions import create_folder, delete_file_folder, view_content, save_listdir
from os import path, mkdir, rmdir, getcwd
import os
import json


def test_create_folder():
    assert create_folder('papochka') == 'Папка создана', 'Ошибка!'
    assert path.exists('papochka'), 'Ошибка!'

    rmdir('papochka')

def test_delete_file_folder():
    mkdir('papka')
    assert delete_file_folder('papka') == 'Папка удалена!', 'Ошибка!'
    assert delete_file_folder('file.txt') == 'Файл удален!', 'Ошибка!'

def test_view_content():
    # new_d = os.chdir(r'C:\Users\user\PycharmProjects\Phunkcii')
    assert view_content(r'C:\Users\user\PycharmProjects\Phunkcii') ==  os.getcwd(), 'Ошибка!'

def test_save_listdir():
    if not path.exists(path.join(getcwd(), 'create')):
        mkdir('create')
    assert save_listdir() == 'Содержимое директории успешно записано в файл listdir', 'Failed!'
    if path.exists('listdir'):
        with open('listdir', 'r', encoding='utf-8') as f:
            f_listdir = json.load(f)
    assert 'create' in f_listdir['dirs'], 'Не верно!'
    rmdir('create')






