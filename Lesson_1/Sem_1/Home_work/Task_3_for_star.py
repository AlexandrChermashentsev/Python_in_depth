# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
# Задание со звездочкой * -> Пусть компьютер отгадывает, а игрок загадывает число.

from random import randint
from time import sleep

lower_limit = 0
upper_limit = 1000
winner = 'игрок'
attempt = 10

flag = True
while flag:
    print(f'Загадайте число от {lower_limit} - {upper_limit}: ')
    num = int(input())
    if num >= lower_limit and num < upper_limit:
        flag = False
    else:
        print('Введено число не в заданном диапазоне. Попробуйте ещё раз')


while attempt != 0:
    computer_number = randint(lower_limit, upper_limit)
    print(f'компьютер выбрал число {computer_number}')
    if computer_number == num:
        winner = 'компьютер'
        break
    elif computer_number > num:
        upper_limit = computer_number
    else:
        lower_limit = computer_number
    attempt -= 1
    print(f'осталось {attempt} попыток')
    print(f'lower_limit -> {lower_limit} || upper_limit -> {upper_limit}')
    sleep(1)
    print()
print(f'Победил {winner}')