import os
import shutil
import json

from decorators import print_info_and_save_to_file


@print_info_and_save_to_file
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        return 'Папка создана'
    except FileExistsError:
        return 'Папка с таким именем уже существует - пожалуйста, придумайте другое имя!'


# Предыдущий вариант функции
# def create_folder(folder_name): # - создать папку
#     if not os.path.exists(folder_name): #  если не существует  файл (или папка)
#         os.mkdir(folder_name)
#         return 'Папка создана'
#     else:
#         return 'Папка с таким именем уже существует - пожалуйста, придумайте другое имя!'


@print_info_and_save_to_file
def delete_file_folder(del_name):
    try:
        shutil.rmtree(del_name)
    except FileNotFoundError:
        return 'Такого файла/папки не существует, введите другое название!'
    else:
        return ('Выбранные файл или папка не удалены!' if os.path.exists(del_name) else 'Файл(папка) успешно удален(а)!')


# Предыдущий вариант функции
# def delete_file_folder(del_name): # - удалить (файл/папку)
#     while os.path.exists(del_name) != True:
#         print('Такого файла/папки не существует, введите другое название!')
#         del_name = input('Введите имя удаляемого файла или папки:')
#     if os.path.exists(del_name):
#         if os.path.isdir(del_name):
#             os.rmdir(del_name) # удаляем папку
#             return 'Папка удалена!'
#         elif os.path.isfile(del_name):
#             os.remove(del_name) # удаляем файл
#             return 'Файл удален!'
#     else:
#         return 'Выбранные файл или папка не удалены!'



@print_info_and_save_to_file
def copy_file_folder():
    do = input('Введите название файла или папки для копирования: ')
    try:
        posle = input('Введите название файла или папки для копирования): ')
        if do == posle:
            print('Имена должны быть разными! Введите оригинальное название для нового файла/папки.')
        else:
            try:
                shutil.copy(do, posle) if os.path.isfile(do) else shutil.copytree(do, posle)
            except FileExistsError:
                print('Объект с таким именем уже существует. Введите другое имя для нового файла/папки.')
            else:
                print('Объект успешно скопирован' if os.path.exists(posle) else 'Невозможно скопировать объект!')
    except FileNotFoundError:
        print('Исходного объекта не существует, введите другое имяназвание!')

# Предыдущий вариант функции
# def copy_file_folder(): # - копировать (файл/папку)
#     do = input('Введите название  файла или папки для копирования: ')
#     while os.path.exists(do) != True:
#         print('Такого файла/папки не существует, введите другое название!')
#         do = input('Введите название  файла или папки для копирования: ')
#     posle = input('Введите новое название для копии файла(папки): ')
#     while do == posle:
#         print('Имена должны быть разными! Введите оригинальное название для нового файла/папки.')
#         posle = input('Введите новое название для копии файла(папки): ')
#     while os.path.exists(posle) == True :
#             print('Объект с таким именем уже существует. Введите другое имя для нового файла/папки')
#             posle = input('Введите новое название для копии файла(папки): ')
#     shutil.copy(do, posle) # Копируем файл или папку с помощью функции copy() модуля shutil
#     if os.path.exists(posle):
#         print('Объект успешно скопирован')
#     else:
#         print('Невозможно скопировать объект!')


@print_info_and_save_to_file
def view_content(smena):

    try:
        os.chdir(smena)
    except FileNotFoundError:
        return 'Такой директории не существует! Попробуйте еще раз.'
    else:
        return f'Вы находитесь в директории: {os.getcwd()}'

# Предыдущий вариант функции
# def view_content(smena): # - смена рабочей директории (*необязательный пункт)
#     if os.path.exists(smena): # После ввода - проверка, существует ли данная директория
#         os.chdir(smena) # Смена
#         return os.getcwd()
#     else:
#         return 'Такой директории не существует! Попробуйте еще раз.'




@print_info_and_save_to_file
def save_listdir():
    f_listdir = {
        'files': [],
        'dirs': [],
    }
    d_l = os.listdir(os.getcwd())
    for item in d_l:
        f_listdir['files'].append(item) if os.path.isfile(item) else f_listdir['dirs'].append(item)
    with open('listdir', 'w', encoding='utf-8') as f:
        f.write(json.dumps(f_listdir))
    with open('listdir', 'r', encoding='utf-8') as f:
        # f.read(json.dumps(dirlist_data))
        return ('Содержимое директории успешно записано в файл listdir' if json.load(f) == f_listdir else 'Ошибка сохранения в файл')



# Предыдущий вариант функции
# def save_listdir():
#     f_listdir = {
#         'files': [],
#         'dirs': [],
#     }
#     d_l = os.listdir(os.getcwd())
#     for i in d_l:
#         if os.path.isfile(i):
#             f_listdir['files'].append(i)
#         else:
#             f_listdir['dirs'].append(i)
#
#     with open('listdir', 'w', encoding='utf-8') as f:
#         f.write(json.dumps(f_listdir))
#     with open('listdir', 'r', encoding='utf-8') as f:
#         if json.load(f) == f_listdir:
#             return 'Содержимое директории успешно записано в файл listdir'
#         else:
#             return 'Ошибка сохранения в файл'








