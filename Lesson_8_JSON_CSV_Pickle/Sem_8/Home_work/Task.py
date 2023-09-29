'''
Задание
📌 Решить задачи, которые не успели решить на семинаре.
📌 Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
📌 Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.
'''

import os 
import json
import pickle
import csv

BACKSLASH_CHAR = '\\' # Пришлось прибегнуть к использованию такой конструкции для поиска пути в некоторых моментах
CSV_FILE = 'Info.csv'
JSON_FILE = 'Info.json'
PICKLE_FILE = 'Info.pickle'

def create_info_file_CSV(lst: list, result_file: str = CSV_FILE):
    if os.path.exists(result_file): operation = 'a'
    else: operation = 'w'
    
    with open(result_file, operation, encoding='UTF-8') as file_csv:
        csv_writer = csv.writer(file_csv, dialect='excel', delimiter='|', lineterminator='\n')
        match operation:
            case 'a':
                csv_writer.writerows(lst)
            case 'w':
                csv_writer.writerow(['Объект', "Имя", "размер"])
                csv_writer.writerows(lst)
                
                
def create_info_file_JSON(lst: list, result_file: str = JSON_FILE):
    if os.path.exists(result_file): operation = 'a'
    else: operation = 'w'
    
    with open(result_file, operation, encoding='UTF-8') as file_json:    
        for item in lst:
            dict_ = {}
            dict_[item[0]] = item[1:]
            json.dump(dict_, file_json, indent=4, ensure_ascii=False)
            
            
def create_info_file_PICKLE(lst: list, result_file: str = PICKLE_FILE):
    if os.path.exists(result_file): operation = 'ab'
    else: operation = 'wb'
    
    with open(result_file, operation) as file_pickle:
        pickle.dump(lst, file_pickle)
    

def tree_files(path: str = os.getcwd()):
    files = list(os.walk(path))
    for root, dirs, file in files:
        result = []

        # Нахождение имени и размера папки
        name_folder = os.path.basename(root)
        summ_elemnts = sum(os.path.getsize(os.path.join(root, obj)) for obj in file)
        print(name_folder, summ_elemnts, "- байт")
        result.append(['Папка', name_folder, summ_elemnts])
        
        # Вывод родительской папки
        if len(root.split(BACKSLASH_CHAR)) > 1: parent_folder = root.rsplit(BACKSLASH_CHAR)[::-1][1]
        else: parent_folder = os.getcwd().split(BACKSLASH_CHAR)[::-1][0]    
        print('parent_folder:', parent_folder)
        result.append(["Родительский каталог", parent_folder])
        
        # Вывод папок в деректории
        if dirs:
            for dir_ in dirs:
                print('sub_folder:', dir_)
                result.append(['Дочерняя папка', dir_])
        # Вывод файлов в директории
        if file:
            for obj in file:
                name_obj = obj
                size_obj = os.path.getsize(os.path.join(root, obj))
                print('file -', name_obj, size_obj, "- байт")
                result.append(['Файл', name_obj, size_obj])
        result.append(['-' * 50])
        print('-' * 50)
        
        create_info_file_CSV(result)
        create_info_file_JSON(result)
        create_info_file_PICKLE(result)

        
            



# tree_files('Lesson_8_JSON_CSV_Pickle')
tree_files()
