from functions import create_folder, delete_file_folder, view_content
from os import path, mkdir, rmdir
import os


def test_make_directory():
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






