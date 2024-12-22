import random
number_generated_anecdotes = 30 # Число генерируемых анекдотов
number_funny_anecdotes = 15 # Число смешных анекдотов

# Привет Борис

def main():
    anecdotes = random_anecdote()
    list_of_anecdotes = full_list_of_anecdotes(anecdotes)
    funny_anecdotes = random_funny_anecdote()
    funny_anecdotes_checking = set(funny_anecdotes)
    list_of_funny_anecdotes = list_of_anecdotes.copy()
    full_list_of_funny_anecdotes(funny_anecdotes, list_of_funny_anecdotes)
    print('\nВечер в хату, новенький. Знаю, ты боишься стать опущенным, а потому тебе потребуются навыки профессионального рассказчика анекдотов.')
    print('Если природа обделила тебя умом и сообразительностью, то не отчаивайся. Я здесь, чтобы помочь тебе.')
    user_answer_choice = start()
    while user_answer_choice in count_list_of_answers_3():
        if user_answer_choice == '1':
            show_full_list_of_anecdotes(list_of_anecdotes)
            user_full_list_of_anecdotes = user_choice_full_anecdote_list()
            if user_full_list_of_anecdotes == '1':
                add_anecdote(list_of_anecdotes, list_of_funny_anecdotes, funny_anecdotes_checking)
                user_answer_choice = '1'
            elif user_full_list_of_anecdotes == '2':
                remove_anecdote(list_of_anecdotes, funny_anecdotes_checking, list_of_funny_anecdotes)
                user_answer_choice = '1'
            elif user_full_list_of_anecdotes == '3':
                user_answer_choice = start()
        elif user_answer_choice == '2':
            show_full_list_of_funny_anecdotes(list_of_funny_anecdotes)
            user_full_list_of_funny_anecdotes = user_choice_full_anecdote_funny_list()
            if user_full_list_of_funny_anecdotes == '1':
                add_funny_anecdote(list_of_funny_anecdotes, list_of_anecdotes, funny_anecdotes_checking)
                user_answer_choice = '2'
            elif user_full_list_of_funny_anecdotes == '2':
                remove_funny_anecdote(list_of_anecdotes, funny_anecdotes_checking, list_of_funny_anecdotes)
                user_answer_choice = '2'
            elif user_full_list_of_funny_anecdotes == '3':
                user_answer_choice = start()
    if user_answer_choice == '4':
        print('\nСкатертью дорога.')

def start():
    user_choice = None
    while user_choice not in count_list_of_answers_4():
        user_choice = input('\nВоспользовавшись командами, представленными ниже, ты легко сможешь:\n\t1. Просмотреть список всех анекдотов и их порядковых номеров.\n\t2. Просмотреть список всех смешных анекдотов.\n\t3. Просмотреть ТОП-10 анекдотов всех времен и народов.\n\t4. Закончить упражнения.\nНомер команды: ')
        if user_choice not in count_list_of_answers_4():
            print('\nЯ тебя не понял, повтори ввод команды.')
    return user_choice

def count_list_of_answers_3():
    count = 1
    list_of_answers = []
    for answer in range(3):
        list_of_answers.append(str(count))
        count +=1
    return list_of_answers

def count_list_of_answers_4():
    count = 1
    list_of_answers = []
    for answer in range(4):
        list_of_answers.append(str(count))
        count +=1
    return list_of_answers

def random_anecdote():
    anecdotes = list(range(101))
    del anecdotes[0]
    anecdotes = random.sample(anecdotes, number_generated_anecdotes)
    return anecdotes

def random_funny_anecdote():
    funny_anecdote = number_generated_anecdotes + 1
    funny_anecdotes = list(range(funny_anecdote))
    del funny_anecdotes[0]
    funny_anecdotes = random.sample(funny_anecdotes, number_funny_anecdotes)
    return funny_anecdotes

def full_list_of_anecdotes(anecdotes):
    number = 1
    list_of_anecdotes = {}
    for count in range(len(anecdotes)):
        list_of_anecdotes[str(number)] = f'Анекдот про число {str(anecdotes.pop())}'
        number += 1
    return list_of_anecdotes

def full_list_of_funny_anecdotes(funny_anecdotes, list_of_funny_anecdotes):
    for anec in range(number_funny_anecdotes):
        funny_anecdote = funny_anecdotes.pop()
        list_of_funny_anecdotes[str(funny_anecdote)] = f'{list_of_funny_anecdotes[str(funny_anecdote)]} *СМЕШНОЙ АНЕКДОТ*'
    return list_of_funny_anecdotes

def show_full_list_of_anecdotes(list_of_anecdotes):
    print('')
    keys = list(map(int, list_of_anecdotes.keys()))
    keys.sort()
    show_list_of_anecdotes = {str(i): list_of_anecdotes[str(i)] for i in keys}
    for number_anecdote, anecdote in show_list_of_anecdotes.items():
        print(f'Анекдот номер {number_anecdote} - {anecdote}')

def show_full_list_of_funny_anecdotes(list_of_funny_anecdotes):
    print('')
    for number_anecdote, anecdote in list_of_funny_anecdotes.items():
        print(f'Анекдот номер {number_anecdote} - {anecdote}')

def user_choice_full_anecdote_list():
    user_choice = None
    while user_choice not in count_list_of_answers_3():
        user_choice = input('\nСписок доступных команд:\n\t1. Добавить/заменить анекдот.\n\t2. Удалить анекдот.\n\t3. Вернуться назад.\nНомер команды: ')
        if user_choice not in count_list_of_answers_3():
            print('\nЯ тебя не понял, повтори ввод команды.')
    return user_choice

def user_choice_full_anecdote_funny_list():
    user_choice = None
    while user_choice not in count_list_of_answers_3():
        user_choice = input('\nСписок доступных команд:\n\t1. Добавить анекдот в список смешных анекдотов.\n\t2. Удалить анекдот из списка смешных анекдотов.\n\t3. Вернуться назад.\nНомер команды: ')
        if user_choice not in count_list_of_answers_3():
            print('\nЯ тебя не понял, повтори ввод команды.')
    return user_choice

def add_anecdote(list_of_anecdotes, list_of_funny_anecdotes, funny_anecdotes_checking):
    a = True
    anecdote_number = None
    while a == True:
        user_choice = None
        b = True
        while b == True:
            try:
                anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
                if anecdote_number < 1:
                    raise Exception('\nПорядковый номер анекдота должен начинаться с единицы.')
                anecdote = input('Введите анекдот: ')
                funny_anecdotes_checking.discard(anecdote_number)
                list_of_anecdotes[str(anecdote_number)] = f'{anecdote}'
                list_of_funny_anecdotes[str(anecdote_number)] = f'{anecdote}'
                b = False
            except ValueError:
                print('\nДолжно быть введено число.')
            except Exception:
                print('\nПорядковый номер анекдота должен начинаться с единицы.')
        while not (user_choice == 'да' or user_choice == 'нет'):
            user_choice = input('\nЖелаешь еще изменить/добавить анекдот? (да/нет): ').lower()
            if user_choice == 'да':
                a = True
            elif user_choice == 'нет':
                a = False
            else:
                print('\nЯ тебя не понял, повтори ввод команды.')

def add_funny_anecdote(list_of_funny_anecdotes, list_of_anecdotes, funny_anecdotes_checking):
    all_numbers = []
    for key in list_of_anecdotes.keys():
        all_numbers.append(int(key))
    a = True
    anecdote_number = None
    while a == True:
        user_choice = None
        b = True
        while b == True:
            try:
                anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
                if anecdote_number not in all_numbers:
                    raise Exception('\nДолжен быть введен существующий порядковый номер.')
                if anecdote_number in funny_anecdotes_checking:
                    print('\nАнекдот уже находится в списке смешных анекдотов.')
                else:
                    funny_anecdotes_checking.add(anecdote_number)
                    list_of_funny_anecdotes[str(anecdote_number)] = f'{list_of_funny_anecdotes[str(anecdote_number)]} *СМЕШНОЙ АНЕКДОТ*'
                b = False
            except ValueError:
                print('\nДолжно быть введено число.')
            except Exception:
                print('\nДолжен быть введен существующий порядковый номер.')
        while not (user_choice == 'да' or user_choice == 'нет'):
            user_choice = input('\nЖелашь еще добавить анекдот в список смешных анекдотов? (да/нет): ').lower()
            if user_choice == 'да':
                a = True
            elif user_choice == 'нет':
                a = False
            else:
                print('\nЯ тебя не понял, повтори ввод команды.')

def remove_anecdote(list_of_anecdotes, funny_anecdotes_checking, list_of_funny_anecdotes):
    a = True
    anecdote_number = None
    while a == True:
        all_numbers = []
        for key in list_of_anecdotes.keys():
            all_numbers.append(int(key))
        user_choice = None
        b = True
        while b == True:
            try:
                anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
                if anecdote_number not in all_numbers:
                    raise Exception('\nДолжен быть введен существующий порядковый номер.')
                del list_of_anecdotes[str(anecdote_number)]
                del list_of_funny_anecdotes[str(anecdote_number)]
                funny_anecdotes_checking.discard(anecdote_number)
                b = False
            except ValueError:
                print('\nДолжно быть введено число.')
            except Exception:
                print('\nДолжен быть введен существующий порядковый номер.')
        while not (user_choice == 'да' or user_choice == 'нет'):
            user_choice = input('\nЖелаешь еще удалить анекдот? (да/нет): ').lower()
            if user_choice == 'да':
                a = True
            elif user_choice == 'нет':
                a = False
            else:
                print('\nЯ тебя не понял, повтори ввод команды.')    

def remove_funny_anecdote(list_of_anecdotes, funny_anecdotes_checking, list_of_funny_anecdotes):
    all_numbers = []
    for key in list_of_anecdotes.keys():
        all_numbers.append(int(key))
    a = True
    anecdote_number = None
    while a == True:
        user_choice = None
        b = True
        while b == True:
            try:
                anecdote_number = int(input('\nВведи порядковый номер анекдота: '))
                if anecdote_number not in all_numbers:
                    raise Exception('\nДолжен быть введен существующий порядковый номер.')
                if anecdote_number not in funny_anecdotes_checking:
                    print('\nАнекдот не находится в списке смешных анекдотов.')
                else:
                    funny_anecdotes_checking.discard(anecdote_number)
                    list_of_funny_anecdotes[str(anecdote_number)] = list_of_anecdotes[str(anecdote_number)]
                b = False
            except ValueError:
                print('\nДолжно быть введено число.')
            except Exception:
                print('\nДолжен быть введен существующий порядковый номер.')
        while not (user_choice == 'да' or user_choice == 'нет'):
            user_choice = input('\nЖелаешь еще удалить анекдот из списка смешных анекдотов? (да/нет): ').lower()
            if user_choice == 'да':
                a = True
            elif user_choice == 'нет':
                a = False
            else:
                print('\nЯ тебя не понял, повтори ввод команды.')    


if __name__ == "__main__":
     main()