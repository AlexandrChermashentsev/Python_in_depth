'''        
📌Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
📌Соберите информацию о содержимом в виде объектов namedtuple.
📌Каждый объект хранит: ○ имя файла без расширения или название каталога, ○ расширение, если это файл, ○ флаг каталога, ○ название родительского каталога.
📌В процессе сбора сохраните данные в текстовый файл используя логирование
'''
import logging
import os
from collections import namedtuple
import argparse


def tree_files(path: str = os.getcwd()):
    Dir_ = namedtuple('Dirs_', 'name format root')
    File_ = namedtuple('File_', 'name format root')

    logger = logging.getLogger(__name__)
    FORMAT_MY = '{msg}'
    logging.basicConfig(filename='task_log.log',
                        filemode='a',
                        encoding='utf-8',
                        level=logging.INFO,
                        style='{',
                        format=FORMAT_MY)
    
    files = list(os.walk(path))
    for root, dirs, files in files:
        if files:
            for file in files:
                if '.' in file:
                    logging.info(msg=f'{File_(file.rsplit(".")[0], file.rsplit(".")[1], root)}')
                else:
                    logging.info(msg=f'{File_(file, "unknown", root)}')
 
        if dirs:
            for dir in dirs:
                logging.info(msg=f'{Dir_(dir, "directory", root)}')        

def create_parser():
    parser = argparse.ArgumentParser(description='Создает спсиок файлов и папок в файле "task_log.log"')
    parser.add_argument('path', type=str, nargs='*', help='Введите абсолютный пыть к папке')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    
    if namespace.path:
        tree_files(*namespace.path)
    else:
        tree_files()
