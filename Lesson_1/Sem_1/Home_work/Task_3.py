# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempt = 10
winner = 'компьютер'

print(f'В этой игре вам нужно отгадать число, которое загадал \
компьютер в диапазоне {LOWER_LIMIT} - {UPPER_LIMIT}. У вас {attempt} попыток')

number = randint(LOWER_LIMIT, UPPER_LIMIT)
while attempt != 0:
    user_number = int(input('Введите число '))
    if user_number == number:
        winner = 'игрок'
        break
    elif user_number > number:
        print('Меньше')
    else:
        print('Больше')
    attempt -= 1
    print(f'Осталось {attempt} попыток')
print(f'Победил {winner}')

