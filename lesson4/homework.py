# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__

import inspect


def open_browser(arg1, arg2='name'):
    pass


def go_to_companyname_homepage(arg3, arg4, arg5):
    pass


def find_registration_button_on_login_page(arg6, arg7, arg8):
    pass


def print_func_name(*args):
    num_of_func = 1  # Порядковый номер функции в итоговом выводе
    for func in args:
        arguments = inspect.signature(func)  # Или мб inspect.getargs(func.__code__)
        print(f'Имя {num_of_func} функции: "{func.__name__}", а это её аргументы в виде кортежа:', arguments)
        num_of_func += 1

print_func_name(open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)

