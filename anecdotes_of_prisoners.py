import repository

def main():
    hello()
    repository.init_1()
    repository.init_2()
    start()
    
    
def hello():
    print('\nВечер в хату, новенький. Знаю, ты боишься стать опущенным, а потому тебе потребуются навыки профессионального рассказчика анекдотов.')
    print('Если природа обделила тебя умом и сообразительностью, то не отчаивайся. Я здесь, чтобы помочь тебе.')
    
def start_print():
    print('\nВоспользовавшись командами, представленными ниже, ты легко сможешь:')
    print('\t1. Просмотреть список всех анекдотов и их порядковых номеров.')
    print('\t2. Просмотреть список всех смешных анекдотов.')
    print('\t3. Просмотреть ТОП-10 анекдотов всех времен и народов.')
    print('\t4. Закончить упражнения.')

def work_with_anecdotes_print():
    print('\nСписок доступных команд:')
    print('\t1. Добавить новый анекдот.')
    print('\t2. Заменить существующий анекдот.')
    print('\t3. Удалить анекдот.')
    print('\t4. Вернуться назад.')

def work_with_funny_anecdotes_print():
    print('\nСписок доступных команд:')
    print('\t1. Добавить анекдот в список смешных анекдотов.')
    print('\t2. Удалить анекдот из списка смешных анекдотов.')
    print('\t3. Вернуться назад.')

def work_with_top_10_print():
    print('\nСписок доступных команд:')
    print('\t1. Отфильтровать ТОП-10 анекдотов по способности запоминания.')
    print('\t2. Отфильтровать ТОП-10 анекдотов по способности рассказывания.')
    print('\t3. Отфильтровать ТОП-10 анекдотов по способностям запоминания и рассказывания.')  
    print('\t4. Вернуться назад.')   

def start():
    start_print()
    user_choice = ask_user(1, 5)
    while user_choice in set(range(1, 4)):
        if user_choice == 1:
            work_with_anecdotes()
            user_choice = ask_user(1, 5)
        if user_choice == 2:
            work_with_funny_anecdotes()
            user_choice = ask_user(1, 5)
        if user_choice == 3:
            work_with_top_10()
            user_choice = ask_user(1, 5)
    if user_choice == 4:
        print('\nСкатертью дорога!')

def ask_user(start, end):
    user_choice = None
    while user_choice not in range(start, end):
        try:
            user_choice = int(input('\nНомер команды: '))
            if user_choice not in range (start, end):
                raise Exception('\nВведен неправильный номер команды!')
        except ValueError:
            print('\nНе понял, попробуй еще раз!')
        except Exception:
            print('\nВведен неправильный номер команды!')
    return user_choice
    
def print_all():
    numbers = repository.get_numbers()
    for anecdote in repository.get_anecdotes():
        print()
        print(f'Анекдот номер {numbers.pop(0)}:\n{anecdote}')

def print_all_funny():
    anecdotes = repository.get_funny_anecdotes()
    for number in repository.get_funny_numbers():
        print()
        print(f'***СМЕШНОЙ*** анекдот номер {number}:\n{anecdotes.pop(0)}')

def print_top(top_list):
    top = top_list.pop()
    top_copy = top_list.pop()
    for key, value in top.items():
        print()
        print(f'МЕСТО НОМЕР {key}\nАнекдот номер {top_copy[key]}:\n{value}')

def get_top_10():
    top_10_list = []
    top_10 = repository.get_top_10()
    top_10_copy = top_10.copy()
    anecdotes = repository.get_funny_anecdotes()
    for number in repository.get_funny_numbers():
        if number in list(top_10.values()):
            for key, value in top_10.items():
                if value == number:
                    top_10[key] = anecdotes.pop(0)
        else:
            anecdotes.pop(0)
    top_10_list.append(top_10_copy)
    top_10_list.append(top_10)
    return(top_10_list)

def number_checking_change_and_remove():
    number_status = False
    numbers = repository.get_numbers()
    while number_status == False:
        try:
            anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
            if anecdote_number not in numbers:
                raise Exception('\nВведенный порядковый номер отсутсвует.')
            number_status = True
        except ValueError:
            print('\nДолжно быть введено число.')
        except Exception:
            print('\nВведенный порядковый номер отсутсвует.')
    return anecdote_number

def number_checking_add():
    number_status = False
    numbers = repository.get_numbers()
    while number_status == False:
        try:
            anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
            if anecdote_number in numbers:
                raise Exception('\nВведенный порядковый номер уже существует.')
            number_status = True
        except ValueError:
            print('\nДолжно быть введено число.')
        except Exception:
            print('\nВведенный порядковый номер уже существует.')
    return anecdote_number

def work_with_anecdotes():
    print_all()
    work_with_anecdotes_print()
    user_choice = ask_user(1, 5)
    while user_choice in set(range(1, 4)):
        if user_choice == 1:
            add_anecdote()
            user_choice = ask_user(1, 5)
        if user_choice == 2:
            change_anecdote()
            user_choice = ask_user(1, 5)
        if user_choice == 3:
            remove_anecdote()
            user_choice = ask_user(1, 5)
    if user_choice == 4:
        start_print()

def add_anecdote():
    number = number_checking_add()
    anecdote = input('\nВведи анекдот:\n')
    repository.add_or_change_anecdote(anecdote, number)
    print_all()
    work_with_anecdotes_print()

def change_anecdote():
    number = number_checking_change_and_remove()
    anecdote = input('\nВведи анекдот:\n')
    repository.add_or_change_anecdote(anecdote, number)
    print_all()
    work_with_anecdotes_print()

def remove_anecdote():
    number = number_checking_change_and_remove()
    repository.remove_anecdote(number)
    print_all()
    work_with_anecdotes_print()

def number_funny_checking_add():
    number_status = False
    amount_all = repository.get_numbers()
    amount_funny = repository.get_funny_numbers()
    while number_status == False:
        try:
            anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
            if anecdote_number not in amount_all:
                raise Exception('Введенный порядковый номер отсутсвует.')
            if anecdote_number in amount_funny:
                raise Exception('Анекдот под введенным порядковым номером уже является смешным.')
            number_status = True
        except ValueError:
            print('\nДолжно быть введено число.')
        except Exception as errors:
            error = errors.args[0]
            print(f'\n{error}')
    return anecdote_number

def number_funny_checking_remove():
    number_status = False
    amount_all = repository.get_numbers()
    amount_funny = repository.get_funny_numbers()
    while number_status == False:
        try:
            anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
            if anecdote_number not in amount_all:
                raise Exception('Введенный порядковый номер отсутсвует.')
            if (anecdote_number not in amount_funny) and (anecdote_number in amount_all):
                raise Exception('Анекдот под введенным порядковым номером не является смешным')
            number_status = True
        except ValueError:
            print('\nДолжно быть введено число.')
        except Exception as errors:
            error = errors.args[0]
            print(f'\n{error}')
    return anecdote_number

def work_with_funny_anecdotes():
    print_all_funny()
    work_with_funny_anecdotes_print()
    user_choice = ask_user(1, 4)
    while user_choice in set(range(1, 3)):
        if user_choice == 1:
            add_funny_anecdote()
            user_choice = ask_user(1, 4)
        if user_choice == 2:
            remove_funny_anecdote()
            user_choice = ask_user(1, 4)
    if user_choice == 3:
        start_print()

def add_funny_anecdote():
    number = number_funny_checking_add()
    repository.add_funny_anecdote(number)
    print_all_funny()
    work_with_funny_anecdotes_print()

def remove_funny_anecdote():
    number = number_funny_checking_remove()
    repository.remove_funny_anecdote(number)
    print_all_funny()
    work_with_funny_anecdotes_print()

def work_with_top_10():
    top_10_list = get_top_10()
    print_top(top_10_list)
    work_with_top_10_print()
    user_choice = ask_user(1, 5)
    while user_choice in set(range(1, 4)):
        if user_choice == 1:
            filter(user_choice)
            user_choice = ask_user(1, 5)
        if user_choice == 2:
            filter(user_choice)
            user_choice = ask_user(1, 5)
        if user_choice == 3:
            filter(user_choice)
            user_choice = ask_user(1, 5)
    if user_choice == 4:
        start_print()

def filter(user_choice):
    if user_choice == 1:
        filter = repository.get_memorization_numbers()
    elif user_choice == 2:
        filter = repository.get_telling_numbers()
    elif user_choice == 3:
        filter = repository.get_memorization_numbers()
        filter_telling = repository.get_telling_numbers()
        for i in filter_telling:
            if i not in filter:
                filter.append(i)
        filter.sort()
    top_list = get_top_10()
    top = top_list.pop()
    top_copy = top_list.pop()
    keys = []
    for number in filter:
        if number in list(top_copy.values()):
            for key, value in top_copy.items():
                if value == number:
                    keys.append(key)
    for key in keys:
        top.pop(key)
        top_copy.pop(key)
    top_list.append(top_copy)
    top_list.append(top)
    print_top(top_list)
    work_with_top_10_print()


if __name__ == "__main__":
     main()