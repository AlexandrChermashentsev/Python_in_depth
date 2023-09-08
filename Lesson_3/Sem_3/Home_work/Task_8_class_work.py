# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
from pprint import pp

baggage = {
        "Петр": ("Аптечка", "Кружка", "Ложка", "Спички", "Угли", "Нож"),
        "Иван": ("Палатка", "Коврики(пенки)", "Средство от насекомых", "Аптечка", "Кружка", "Ложка"),
        "Василий": ("Туалетная бумага", "Вода", "Консервы", "Макароны", "Тушенка", "Аптечка", "Кружка", "Ложка")
        }
# ------------------------------------------------------
all_items = list(baggage.values())
must_have_item = set(all_items[0])

print(must_have_item)
for items in all_items:
    must_have_item = must_have_item.intersection(set(items))
print(must_have_item)

uniq_items = {}
for name, items in baggage.items():
    uniq_items[name] = set(items).difference(must_have_item)
pp(uniq_items)
# ---------------------------------------------------------

# flag = True
# while flag:
#     user_input = int(input('Введите:\n\
# "1" - чтобы добавить друга и его вещи\n\
# "2" - вывести ниформацию  по вещам\n\
# "0" - выход\n-> '))
#     match user_input:

#         case 1:
#             name = input("Введите имя друга")
#             things = set(input(f"Введите через пробел, вещи которые взял {name}: ").split())
#             baggage[name] = things

#         case 2:
#             user_input = int(input('Введите\n\
# "1" - посмотреть вещи, которые взяли все друзья\n\
# "2" - вещи уникальные, есть только у одного друга\n\
# "3" - Какие вещи есть у всех друзей кроме одного и имя того, \
# у кого данная вещь отсутствует\n-> '))
#             all_items = list(baggage.values())
#             must_have_item = set(all_items[0])

#             if user_input == 1: # сумма вещей
#                 all_items = list(baggage.values())
#                 pp(all_items)
#             elif user_input == 2: # вещи которые есть у всех
#                 must_have_item = set(all_items[0])
#                 for items in all_items:
#                     must_have_item = must_have_item.intersection(set(items))
#                 pp(must_have_item)
#             elif user_input == 3: # уникальные вещи
#                 uniq_items = {}
#                 for name, items in baggage.items():
#                     uniq_items[name] = set(items).difference(must_have_item)
#                 pp(uniq_items)
#             else: print("Неверная команда")

#         case 0:
#             flag = False

#         case _:
#             print("Неверная команда")