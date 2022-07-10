import random2

def victory():

    dr_celebrity = {
                    'Да Винчи': '15.04.1452',
                    'Владимир Ленин': '22.04.1870',
                    'Владимир Путин': '07.10.1952',
                    'Жан Кусто': '08.05.1938',
                    'Георгий Жуков': '01.12.1896',
                    'Никола Тесла': '10.07.1856',
                    'Олег Попов': '31.07.1930',
                    'Брюс Ли': '27.11.1940',
                    'Александр Засс': '23.02.1888',
                    'Константин Циалковский': '17.09.1857',
    }

    months = {
         '01' : 'января',
         '02' : 'февраля',
         '03' : 'марта',
         '04' :  'апреля',
         '05' : 'мая',
         '06' : 'июня',
         '07' : 'июля',
         '08' :  'августа',
         '09' : 'сентября',
         '10' :  'октября',
         '11' :  'ноября',
         '12' : 'декабря',
    }

    days = {
         '01' : 'первого',
         '02' : 'второго',
         '03' : 'третьего',
         '04' : 'четвертого',
         '05' : 'пятого',
         '06' : 'шестого',
         '07' : 'седьмого',
         '08' : 'восьмого',
         '09' : 'девятого',
         '10' : 'десятого',
         '11' : 'одиннадцатого',
         '12' : 'двенадцатого',
         '13' : 'тринадцатого',
         '14' : 'четырнадцатого',
         '15' : 'пятнадцатого',
         '16' : 'шестнадцатого',
         '17' : 'семнадцатого',
         '18' : 'восемнадцатого',
         '19' : 'девятнадцатого',
         '20' : 'двадцатого',
         '21' : 'двадцать первого',
         '22' : 'двадцать второго',
         '23' : 'двадцать третьего',
         '24' : 'двадцать четвертого',
         '25' : 'двадцать пятого',
         '26' : 'двадцать шестого',
         '27' : 'двадцать седьмого',
         '28' : 'двадцать восьмого',
         '29' : 'двадцать деватого',
         '30' : 'тридцатого',
         '31' : 'тридцать первого',
    }

    while True: # Пока является истиной:
        rand_free5 = random2.sample(dr_celebrity.keys(), 5)   #  Всего вопросов
        true_otvet = 0 # Всего правильных ответов
        false_otvet = 0 # Всего не правильных ответов
        print()
        print("ВИКТОРИНА")
        print()



        for name in rand_free5:
             # проверка корректности ввода
            vvod = False

            while not vvod:
                vopros = input(f'Введите дату рождения для {name} в формате день.месяц.год: ')

                if len(vopros) == 10:
                    if '.' in vopros:
                        if vopros.count('.') == 2:
                                f_data = vopros.split('.')
                                if len(f_data[0]) == len(f_data[1]) == 2 and len(f_data[2]) == 4:
                                    if f_data[0].isdigit() and f_data[1].isdigit() and f_data[2].isdigit():
                                        vvod = True
                                    else:
                                        print('Вы ввели не число!')
                                else:
                                    print(' Длина чисел даты введена не правильно!')
                        else:
                                print('В дате должны быть только две разделительные точки!')
                    else:
                        print('Дата разделяется только точками!')
                else:
                    print(f'Неверный формат даты рождения! {name} машет вам кулаком!')

            if vopros == dr_celebrity[name]:
                true_otvet += 1
                print('Верно!)')
            else:
                false_otvet += 1
                day, month, year = dr_celebrity[name].split('.')
                print(  f'Вы ошиблись... {name} родился',  days[day], months[month], year, 'года')

        print()
        print("Итоги вашей викторины:")
        print()
        print("Правильных ответов:   ", true_otvet)
        print("Ошибочных:   ",  false_otvet)

        vopros = input("Хотите пройти викторину заново (Да/Нет) ?")
        if not ((vopros == "Да") or (vopros == "да")): # Если ответ НЕ  Да или да
            break  # Выходим из программы