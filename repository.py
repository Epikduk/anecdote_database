import anecdotes_reader as reader
import os
import random

anecdotes_path = 'resources/anecdotes'
anecdotes = []
numbers = []
funny_numbers = []
funny_anecdotes = []
memorization_numbers = []
telling_numbers = []
top_anecdotes = []

def init_1():
    global numbers
    numbers = reader.read_numbers()
    generate_funny_numbers()
    create_funny_anecdotes()
    top_anecdotes_init()
    generate_memorization_and_telling_numbers()

def init_2():
    global anecdotes, numbers
    numbers = reader.read_numbers()
    anecdotes = reader.read_anecdotes()

def get_anecdotes():
    return anecdotes.copy()

def get_numbers():
    return numbers.copy()

def get_funny_numbers():
    return funny_numbers.copy()

def generate_funny_numbers():
    global funny_numbers
    for number in numbers:
        i = random.randint(1, 3)
        if i == 1:
            funny_numbers.append(number)

def create_funny_anecdotes():
    global funny_anecdotes
    funny_anecdotes = []
    for number in funny_numbers:
        with open(f'resources/anecdotes/anec{number}.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            funny_anecdotes.append(content)

def get_funny_anecdotes():
    return funny_anecdotes.copy()

def add_or_change_anecdote(anecdote, number):
    anecdotes_path = f'resources/anecdotes/anec{number}.txt'
    with open(anecdotes_path, 'w', encoding='utf-8') as file:
        file.write(anecdote)
    memorization_and_telling_add(number)
    init_2()
    
def remove_anecdote(number):
    anecdotes_path = f'resources/anecdotes/anec{number}.txt'
    os.remove(anecdotes_path)
    memorization_and_telling_remove(number)
    remove_funny_anecdote(number)
    init_2()

def add_funny_anecdote(number):
    global funny_numbers
    funny_numbers.append(number)
    funny_numbers.sort()
    create_funny_anecdotes()
    top_anecdotes_add(number)

def remove_funny_anecdote(number):
    global funny_numbers
    if number in funny_numbers:
        funny_numbers.remove(number)
        funny_numbers.sort()
    create_funny_anecdotes()
    top_anecdotes_remove(number)

def generate_memorization_and_telling_numbers():
    global memorization_numbers, telling_numbers
    for number in numbers:
        i = random.randint(1, 2)
        j = random.randint(1, 2)
        if i == 1:
            memorization_numbers.append(number)
        if j == 1:
            telling_numbers.append(number)

def memorization_and_telling_add(number):
    global telling_numbers, memorization_numbers
    i = random.randint(1, 2)
    j = random.randint(1, 2)
    if i == 1:
        if number not in memorization_numbers:
            memorization_numbers.append(number)
            memorization_numbers.sort()
    if j == 1:
        if number not in telling_numbers:
            telling_numbers.append(number)
            telling_numbers.sort()

def memorization_and_telling_remove(number):
    global telling_numbers, memorization_numbers
    if number in telling_numbers:
        telling_numbers.remove(number)
        telling_numbers.sort()
    if number in memorization_numbers:
        memorization_numbers.remove(number)
        memorization_numbers.sort()

def top_anecdotes_init():
    global top_anecdotes
    top_anecdotes = random.sample(funny_numbers, len(funny_numbers))

def top_anecdotes_add(number):
    global top_anecdotes
    i = random.randint(0, len(funny_numbers))
    top_anecdotes.insert(i, number)

def top_anecdotes_remove(number):
    global top_anecdotes
    if number in top_anecdotes:
        top_anecdotes.remove(number)

def get_top_10():
    top_10 = {}
    k = 1
    for i in range(10):
        try:
            top_10[k] = top_anecdotes[i]
            k += 1
        except:
            continue
    return top_10

def get_memorization_numbers():
    return memorization_numbers.copy()

def get_telling_numbers():
    return telling_numbers.copy()