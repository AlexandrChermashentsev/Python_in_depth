'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY.
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) 
действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
'''


def _my_func_year_isleap(year: int) -> bool:
    _result = False
    if year % 4 == 0:
        if year % 100 != 0:
            _result = True
            return _result
        elif year % 400 == 0:
            _result = True
            return _result
    return _result

def date_func(date_input: str) -> bool:
    day, month, year = list(map(int, date_input.split('.')))
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    
    if  1 <= year <= 9999:
        if month in month_31:
            if 1 <= day <= 31:
                return True
        elif month == 2:
            if _my_func_year_isleap(year):
                if 1 <= day <= 29: return True
            elif 1 <= day <= 28: return True
        else:
            if 1 <= day <= 30: return True

    return False

    

if __name__ == '__main__':

    print(date_func('31.10.20000'))
    print(date_func('31.12.2000'))
    print(date_func('29.02.2000'))
    print(date_func('29.02.1999'))
    print(date_func('-1.02.1999'))


    



   
