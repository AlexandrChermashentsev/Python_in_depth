# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
from pprint import pp
from random import randint
from time import sleep

baggage = {"Зубная щетка": 1, 
           "Кружка": 2, 
           "Спички": 1, 
           "Ложка": 1, 
           "Спальный мешок": 4, 
           "Палатка": 5,
           "Аптечка": 3, 
           "Сменная одежда": 3, 
           "Коврик(пенка)": 2, 
           "Налобный фонарик": 2, 
           "Туалетная бумага": 2,
           "Фляга с водой": 4, 
           "Средство от насекомых": 2, 
           "Средства личной гигиены": 3, 
           "Трекинговые палки": 2}
baggage_list = []
backpack = []
weight = 0
MAX_WEIGHT_BACKPACK = 25 #int(input('Введите грузоподъемность вашего рюкзака(в условных еденицах): '))


for item in baggage.items():
    baggage_list.append(item)

thing = randint(0, len(baggage_list) - 1)
backpack.append(baggage_list[thing])
baggage_list.pop(thing)

while weight != MAX_WEIGHT_BACKPACK:
    weight = sum(item[1] for item in backpack)
    print(f'Рюкзак щаполнен на {weight} из {MAX_WEIGHT_BACKPACK}')

    if weight > MAX_WEIGHT_BACKPACK: # Если вес рюкзака больше допустимого то выкладываем
        thing = randint(0, len(backpack) - 1)
        baggage_list.append(backpack[thing])
        print(f'Из рюкзака достали {backpack[thing]}')
        backpack.pop(thing)
    elif weight < MAX_WEIGHT_BACKPACK: # Если меньше, то добираем
        thing = randint(0, len(baggage_list) - 1)
        backpack.append(baggage_list[thing])
        print(f'В рюкзак положили {baggage_list[thing]}')
        baggage_list.pop(thing)

    sleep(1)

pp(backpack)
