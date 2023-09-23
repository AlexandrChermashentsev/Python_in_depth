'''
Напишите функцию группового переименования файлов. Она должна:
    - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    - принимать параметр количество цифр в порядковом номере.
    - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    - принимать параметр расширение конечного файла.
    - принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано, 
далее счётчик файлов и расширение.
'''

from pathlib import Path
from string import ascii_lowercase
import os
import random as rnd
from time import sleep

def start_menu():
    return 'Введите через пробел:\n\tФормат файлов которые хотите поменять\
        \n\tВ какой формат хотите перевести\n\
        (необязательно) Желаемое имя файлов\n\
        Количество цифр в порядковом номере (Если введено новое имя для файлов)\n\
        Диапазон сохраняемого имени в формате 1-3 (Если введено новое имя для файлов)\n-> '


def random_name():
    vowels = set('euioay')
    consonants = set(ascii_lowercase).difference(vowels)
    len_name = rnd.randint(4, 10)
    name = ''
    for i in range(len_name):
        name += rnd.choice(list(vowels)) if i % 2 else rnd.choice(list(consonants))
    return name.title()


def to_string_count(amount_symb: int, count: str):
    if amount_symb <= len(count):
        return count
    else:
        return (amount_symb - len(count)) * '0' + count


 # Изначальная версия программы, которая взаимодействует с пользователем (мне так больше нравится)
def rename_files():
    cnt_files = 1
    p = Path(Path.cwd())
    for obj in p.iterdir():
        print(obj) # выводим список объектов в папке
    print('-' * 30)
    old_format, new_format, *args = input(start_menu()).split()

    for obj in p.iterdir():
        if obj.is_file() and str(obj)[len(str(obj)) - len(old_format):] == old_format:
# проверяем объект - файл? & последние символы названия совпадают с форматом который мы хотим изменить?
            old_name = os.path.basename(str(obj))
            tmp_name = old_name
            tmp_name = tmp_name[:len(tmp_name) - (len(old_format) + 1)]
            if len(args) == 3:
                name, cnt_numbers, range_symbols = args
                range_symbols = [int(i) for i in range_symbols.split('-')]
                cnt_numbers = int(cnt_numbers)
                tmp_name = tmp_name[range_symbols[0]-1:range_symbols[1]-1]
                new_name_file = tmp_name + name + "_" + to_string_count(cnt_numbers, str(cnt_files)) + "." + new_format
                cnt_files +=1
                os.rename(old_name, new_name_file)
            elif len(args) == 0:
                new_name_file = tmp_name + '.' + new_format
                os.rename(old_name, new_name_file)


 # Версия программы, которую требуют в условии задачи
def rename_files_v2(old_format: str, new_format: str, *args):
    cnt_files = 1
    p = Path(Path.cwd())
    for obj in p.iterdir():
        if obj.is_file() and str(obj)[len(str(obj)) - len(old_format):] == old_format:
            old_name = os.path.basename(str(obj))
            tmp_name = old_name
            tmp_name = tmp_name[:len(tmp_name) - (len(old_format) + 1)]
            if len(args) == 3:
                name, cnt_numbers, range_symbols = args
                range_symbols = [int(i) for i in range_symbols.split('-')]
                cnt_numbers = int(cnt_numbers)
                tmp_name = tmp_name[range_symbols[0]-1:range_symbols[1]-1]
                new_name_file = tmp_name + name + "_" + to_string_count(cnt_numbers, str(cnt_files)) + "." + new_format
                cnt_files +=1
                os.rename(old_name, new_name_file)
            elif len(args) == 0:
                new_name_file = tmp_name + '.' + new_format
                os.rename(old_name, new_name_file)


if __name__ == '__main__':
    # создадим файлы для тестирования
    FORMAT_ = 'txt'
    COUNT_NEW_FILES = 5
    for _ in range(COUNT_NEW_FILES):
        with open(f'{random_name()}.{FORMAT_}', 'w', encoding='utf-8') as f:
            f.write(f'{random_name()}\n' * rnd.randint(1, 10))

    sleep(5) # Чтобы пользователь смог найти новые файлы в директории
    rename_files_v2('txt', 'py', '_new_file', '3', '1-5')
    sleep(5) # Чтобы пользователь смог заметить изменения в файлах
    rename_files_v2('py', 'txt')