import os
import shutil

def create_folder(folder_name): # - создать папку
    if not os.path.exists(folder_name): #  если не существует  файл (или папка)
        os.mkdir(folder_name)
        return 'Папка создана'
    else:
        return 'Папка с таким именем уже существует - пожалуйста, придумайте другое имя!'


def delete_file_folder(del_name): # - удалить (файл/папку)
    while os.path.exists(del_name) != True:
        print('Такого файла/папки не существует, введите другое название!')
        del_name = input('Введите имя удаляемого файла или папки:')
    if os.path.exists(del_name):
        if os.path.isdir(del_name):
            os.rmdir(del_name) # удаляем папку
            return 'Папка удалена!'
        elif os.path.isfile(del_name):
            os.remove(del_name) # удаляем файл
            return 'Файл удален!'
    else:
        return 'Выбранные файл или папка не удалены!'






def copy_file_folder(): # - копировать (файл/папку)
    do = input('Введите название  файла или папки для копирования: ')
    while os.path.exists(do) != True:
        print('Такого файла/папки не существует, введите другое название!')
        do = input('Введите название  файла или папки для копирования: ')
    posle = input('Введите новое название для копии файла(папки): ')
    while do == posle:
        print('Имена должны быть разными! Введите оригинальное название для нового файла/папки.')
        posle = input('Введите новое название для копии файла(папки): ')
    while os.path.exists(posle) == True :
            print('Объект с таким именем уже существует. Введите другое имя для нового файла/папки')
            posle = input('Введите новое название для копии файла(папки): ')
    shutil.copy(do, posle) # Копируем файл или папку с помощью функции copy() модуля shutil
    if os.path.exists(posle):
        print('Объект успешно скопирован')
    else:
        print('Невозможно скопировать объект!')


def view_content(smena): # - смена рабочей директории (*необязательный пункт)
    if os.path.exists(smena): # После ввода - проверка, существует ли данная директория
        os.chdir(smena) # Смена
        return os.getcwd()
    else:
        return 'Такой директории не существует! Попробуйте еще раз.'







