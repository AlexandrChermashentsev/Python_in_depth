# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

# def simple_or_composite_number(x: int) -> bool:
#     for i in range(2, x):
#         if not x % i:
#             return False
#     return True

def gen_func_simple_numbers(num: int):
    simple_numbers = []
    for simpl_num in range(2, num + 1):
        for j in simple_numbers:
            if not simpl_num % j:
                break
        else:
            simple_numbers.append(simpl_num)
            yield simpl_num


x = gen_func_simple_numbers(100)
for i in x:
    print(i, end=' ')

