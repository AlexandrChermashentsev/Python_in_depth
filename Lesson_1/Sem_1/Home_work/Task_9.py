# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def function_my(m, n):
    for j in range(m, n):
        result = j * i
        if result < 10:
            print(f'{j} x {i} = {j * i}   ', end='')
        elif i == 10:
            print(f'{j} x{i} = {j * i}  ', end='')
        else:
            print(f'{j} x {i} = {j * i}  ', end='')
    print()


for i in range(2, 11):
    function_my(2, 6)
print()
for i in range(2, 11):
    function_my(6, 10)
