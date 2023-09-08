# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

from pprint import pp


def count_string_elements(text: str) -> dict(): # Метод подсчета букв в тексте
    my_dict = dict()
    for i in text.lower():
        if i.isalpha():
            my_dict[i] = my_dict.get(i, 0) + 1
    return my_dict

data = 'У лукоморья дуб зелёный;\n\
Златая цепь на дубе том:\n\
И днём и ночью кот учёный\n\
Всё ходит по цепи кругом;\n\
Идёт направо — песнь заводит,\n\
Налево — сказку говорит.\n\
Там чудеса: там леший бродит,\n\
Русалка на ветвях сидит;\n\
Там на неведомых дорожках\n\
Следы невиданных зверей;\n\
Избушка там на курьих ножках\n\
Стоит без окон, без дверей;\n\
Там лес и дол видений полны;\n\
Там о заре прихлынут волны\n\
На брег песчаный и пустой,\n\
И тридцать витязей прекрасных\n\
Чредой из вод выходят ясных,\n\
И с ними дядька их морской;\n\
Там королевич мимоходом\n\
Пленяет грозного царя;\n\
Там в облаках перед народом\n\
Через леса, через моря\n\
Колдун несёт богатыря;\n\
В темнице там царевна тужит,\n\
А бурый волк ей верно служит;\n\
Там ступа с Бабою Ягой\n\
Идёт, бредёт сама собой,\n\
Там царь Кащей над златом чахнет;\n\
Там русский дух… там Русью пахнет!\n\
И там я был, и мёд я пил;\n\
У моря видел дуб зелёный;\n\
Под ним сидел, и кот учёный\n\
Свои мне сказки говорил.'

my_dict = count_string_elements(data)
result_list = []
for item in my_dict.items():
    result_list.append(item)
result_list.sort(key=lambda a: a[1], reverse=True) # Сортировка по второму символу кортежа в списке
print(result_list[:10:])
