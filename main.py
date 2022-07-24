import sys
import glob2

from functions import *
from bank_account import *
from victory import *

if __name__ == '__main__':

    while True:
        print('\n1. Создать папку')
        print('2. Удалить (файл/папку)')
        print('3. Копировать (файл/папку)')
        print('4. Просмотр содержимого рабочей директории')
        print('5. Посмотреть только папки')
        print('6. Посмотреть только файлы')
        print('7. Просмотр информации об операционной системе')
        print('8. Создатель этой программы')
        print('9. Мой банковский счет ')
        print('10. Викторина "Дни рождения"')
        print('11. Смена рабочей директории')
        print('12. Найти все csv файлы, которые есть в этой директории')
        print('13. Сохранить содержимое рабочей директории в файл')
        print('0. Выход')

        menu = input('Выберите цифру пункта меню: ')
        if menu == '1':
            print(create_folder(input('Введите название папки: ')))
        elif menu == '2':
            print(delete_file_folder(input('Введите имя удаляемого файла или папки:')))
        elif menu == '3':
            copy_file_folder()
        elif menu == '4':
            print(os.listdir())
        elif menu == '5':
            print([object for object in os.listdir() if os.path.isdir(object)]) #  Получаем список всех файлов и папок, а потом просто отсеиваем из них папки
        elif menu == '6':
            print([object for object in os.listdir() if os.path.isfile(object)]) #  Получаем список всех файлов и папок, а потом просто отсеиваем из них файлы
        elif menu == '7':
            print(os.name)
            print(sys.platform)
        elif menu == '8':
            print('$$$ Creator of the program Igor Chernov $$$')
        elif menu == '9':
            bank_account()
        elif menu == '10':
            victory()
        elif menu == '11':
            print(view_content(input('Введите путь к новой директории: ')))
        elif menu == '12':
            for files in glob2.glob("*.csv"):
                print(files)
        elif menu =='13':
            print(save_listdir())
        elif menu == '0':
            break
        else:
            print('\nНеверный пункт меню\n')