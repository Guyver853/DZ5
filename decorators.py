"""
Выводим на экран и пишем в файл название вызываемых фукнций
"""

def print_info_and_save_to_file(func):

    def inner(*args, **kwargs):
        print(f'\n*** Вызвана функция {func.__name__} ***\n')
        print(f'\n*** Функция {func.__name__} отработала ***\n')
        # Пишем название фукнций в файл
        function_name = func.__name__
        with open('log_func.txt', 'a', encoding='utf-8') as f:
            f.write(f'{function_name}\n')
        result = func(*args, **kwargs)
        return result

    return inner


