'''
Напишите следующие функции:
    * Нахождение корней квадратного уравнения
    * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    * Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
    * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
'''

import json
import csv
from random import choice
from typing import Callable


CSV_FILE = 'three_random_numbers.csv'
JSON_FILE = 'three_random_numbers.json'


def decor(func: Callable) -> Callable:    
    def quadratic(data):
        a, b, c = data
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return f'корней нет'
        elif discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            return round(x1, 3), round(x2, 3)
        else:
            x = -b / (2 * a)
            return round(x, 3)
    return quadratic

def csv_creater():
    range_count_lines = range(100, 1000)
    range_a_b_c = range(1, 100)
    result = []
    with open(CSV_FILE, 'w', encoding='UTF-8') as file_csv:
        for _ in range(choice(range_count_lines)):
            first = choice(range_a_b_c)
            second = choice(range_a_b_c)
            third = choice(range_a_b_c)
            result.append([first, second, third])
        csv_writer = csv.writer(file_csv, dialect='excel', delimiter='|', lineterminator='\n')
        csv_writer.writerows(result)

def json_creater(func: Callable) -> Callable:
    def wrapper(*args):
        result = func(*args)

        data = {'params': args,
                'result': result}
        # data = [params, result]
        with open(JSON_FILE, 'a', encoding='UTF-8') as file:
            data = json.dump(data, file, indent=2, ensure_ascii=False)
    return wrapper

def csv_reader() -> list:
    data = []
    with open(CSV_FILE, 'r', encoding='UTF-8') as file:
        data = file.readlines() # -> ['a'|'b'|'c'\n]
    
    for i, items in enumerate(data):
        data[i] = list(map(int, data[i].strip().split('|'))) # -> (a: int, b: int, c: int)
    return data

@json_creater
@decor      
def some_func(a: int=0, b: int=0, c: int=0):
    return a,b,c


if __name__ == '__main__':
    csv_creater()
    data = csv_reader()

    for i in data:
        some_func(i)

    