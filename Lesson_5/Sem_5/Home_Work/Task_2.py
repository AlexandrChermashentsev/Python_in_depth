# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def parsing_path(path: str) -> tuple:
    path_file = path[:path.rfind('/')]
    name_file = path[path.rfind('/')+1 : path.rfind('.')]
    format_file = path[path.rfind('.')+1:]
    return path_file, name_file, format_file
    
        
path = 'MyComputer/Program Files/Test folder/test_file.txt'
print(parsing_path(path))