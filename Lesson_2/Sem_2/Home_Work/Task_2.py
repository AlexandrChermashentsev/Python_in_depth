# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions.
import fractions

def my_inference(fract: str):
    fract = fract.split('/')
    a, b = int(fract[0]), int(fract[1])
    devider = 2
    while devider <= min(a, b):
        if a % devider == 0 and b % devider == 0:
            a = a // devider
            b = b // devider
            devider = 2
        else: devider += 1
    fract[0], fract[1] = a, b

    if b == 1:
        fract = a
    elif a > b:
        int_part = 0
        print(f'Без определения целой части: {str(a)}/{str(b)}')
        while a >= b:
            int_part += 1
            a -= b
        fract = str(int_part) + ' + ' + str(a) + '/' + str(b)
    else:
        fract = str(a) + '/' + str(b)
    
    return fract

def sum_fractions(fra_1: str, fra_2: str):
    fra_1, fra_2 = fra_1.split('/'), fra_2.split('/')
    for i in range(len(fra_1)):
        fra_1[i] = int(fra_1[i])
        fra_2[i] = int(fra_2[i])

    if fra_1[1] == fra_2[1]: # Если знаменатели равны
        summ = str(fra_1[0] + fra_2[0]) + '/' + str(fra_1[1])
    else:
        fra_1[0] *= fra_2[1]
        fra_2[0] *= fra_1[1]
        summ = str(fra_1[0] + fra_2[0]) + '/' + str(fra_1[1] * fra_2[1])
    return summ

def multiplication_fractions(fraction_1: str, fraction_2: str):
    fraction_1, fraction_2 = fraction_1.split('/'), fraction_2.split('/')
    for i in range(len(fraction_1)):
        fraction_1[i] = int(fraction_1[i])
        fraction_2[i] = int(fraction_2[i])
    multiplication = str(fraction_1[0] * fraction_2[0]) + '/' + str(fraction_1[1] * fraction_2[1])
    return multiplication


fraction_1 = input('Введите первую дробь: ' )
fraction_2 = input('Введите вторую дробь: ' )
print('-' * 20)
summ = my_inference(sum_fractions(fraction_1, fraction_2))
print('summ = ', summ)
print('-' * 20)

multi = my_inference(multiplication_fractions(fraction_1, fraction_2))
print('multi = ', multi)
print('-' * 20)

f1 = fractions.Fraction(int(fraction_1.split('/')[0]), int(fraction_1.split('/')[1]))
f2 = fractions.Fraction(int(fraction_2.split('/')[0]), int(fraction_2.split('/')[1]))
print(f'Проверка суммы: {f1 + f2}\nПроверка умножения: {f1 * f2}')


