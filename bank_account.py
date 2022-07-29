def bank_account ():
    from os import path
    import json
    from decorators import print_info_and_save_to_file


    @print_info_and_save_to_file
    def all_summa (account_history, summa):
        while not summa.isnumeric():
            input('\nВведите сумму пополнения. ВНИМАНИЕ! Сумма вводится только целым числом: ')

        account_history['all_summa'] += int(summa)
        print(f"Сумма на вашем счете: {account_history['all_summa']} р.")
        return account_history


    @print_info_and_save_to_file
    def s_pokupki (account_history, summa):

        while not summa.isnumeric():
            summa = input('Введите сумму покупки. ВНИМАНИЕ! Сумма вводится только целым числом:  ')

        summa = int(summa)

        if summa > account_history['all_summa']:
            print('Недостаточно средств на счете!')
        else:
            account_history['all_summa'] -= summa
            account_history[input('Введите название товара: ')] = summa

        return account_history


    @print_info_and_save_to_file
    def history_shopping(account_history):
        if len(account_history) > 1:
            print('\nИстория покупок:')
            for key, s in account_history.items():
                if key != 'all_summa':
                    print(f'{key} --> {s} р.')
        else:
            print('\nСписок ваших покупок пуст!')

    account_history = {
        'all_summa': 0,
    }

    path_bank_file = './account_history'
    if path.exists(path_bank_file):
        with open(path_bank_file, 'r', encoding='utf-8') as f:
            account_history = json.load(f)


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        menu = input('Выберите пункт меню: ')
        if menu == '1':
            account_history = all_summa(account_history, input('\nВведите сумму пополнения: '))
        elif menu == '2':
            account_history = s_pokupki(account_history, input('\nВведите сумму покупки: '))
        elif menu == '3':
            history_shopping(account_history)
        elif menu == '4':
            break
        else:
            print('Неверный пункт меню')

    with open(path_bank_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(account_history))





