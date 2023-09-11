# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, 
# а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def func_kwargs(**kwargs) -> dict:
    dct = {}
    for key, value in kwargs.items():
        if isinstance(value, list | dict | set):
            value = str(value)
            dct[value] = key
        else: 
            dct[value] = key
        
    return dct


print(func_kwargs(a=None, b=[1,2,3], c=23, d='D', e=True))
# dct = func_kwargs(a=1, b=[1,2,3,4], qwerty=(1,2,3,['one', 'two'], {'five': 5}))
# print(dct)
