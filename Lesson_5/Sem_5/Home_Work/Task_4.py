# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fib_gen_func():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x+y

fibonacci = fib_gen_func()
count = 20

while count:
    print(next(fibonacci), end=' ')
    count -= 1


