# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


num = int(input('Enter the number: '))
BASE = 16
original_number = num
arr_base_16 = ['a', 'b', 'c', 'd', 'e', 'f']
result_number = ''

while num:
    symbol = num % BASE
    if symbol > 9:
        symbol = arr_base_16[symbol - 10]
    result_number = str(symbol) + result_number
    num //= BASE

print(f'Число {original_number} в {BASE} - ичной системе счисления будет: {result_number}')
print(f'hex_original = {hex(original_number)[2:]}')

