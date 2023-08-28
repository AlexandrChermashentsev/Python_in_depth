# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

answer = 'simple'
LOWER_LIMIT = 0
UPPER_LIMIT = 100000

print(f'Enter the number in range {LOWER_LIMIT} - {UPPER_LIMIT}: ')
num = int(input())

if num > LOWER_LIMIT and num < UPPER_LIMIT:
    for i in range(2, num):
        if num % i == 0:
            answer = 'composite'
            break     
else:
    print('Try again')
print(answer)