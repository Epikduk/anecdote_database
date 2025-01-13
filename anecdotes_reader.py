import os
import repository as repository

anecdotes_path = 'resources/anecdotes'

def read_anecdotes():
    anecdotes = []
    number = 1
    while len(anecdotes) != len(os.listdir(anecdotes_path)):
        anecdotes_path_number = f'resources/anecdotes/anec{number}.txt'
        try:
            with open(anecdotes_path_number, 'r', encoding='utf-8') as file:
                content = file.read()
                anecdotes.append(content)
            number += 1
        except FileNotFoundError:
            number += 1
    return anecdotes

def read_numbers():
    numbers = []
    number = 1
    while len(numbers) != len(os.listdir(anecdotes_path)):
        anecdotes_path_number = f'resources/anecdotes/anec{number}.txt'
        try:
            open(anecdotes_path_number, 'r', encoding='utf-8')
            numbers.append(number)
            number += 1
        except FileNotFoundError:
            number += 1
    return numbers


