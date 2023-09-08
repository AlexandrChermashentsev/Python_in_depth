# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

import random

start_list = [random.randint(0, 5) for _ in range(20)]
print(f'{start_list=}')
result_list = []
for item in start_list:
    if start_list.count(item) > 1:
        result_list.append(item)

print(f'\n{list(set(result_list))=}')
