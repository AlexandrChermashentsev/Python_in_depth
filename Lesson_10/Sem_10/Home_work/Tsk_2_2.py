'''
# Задание №8
# 📌 Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# 📌 Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********
'''

class Fir_tree:
    def __init__(self, row):
        self.row = row
        
    def print_fir_tree(self):
        for i in range(self.row):
            print(f'{"*" * (2 * i + 1):^{self.row * 2 + 1}}')
            
fir_tree_1 = Fir_tree(5)
fir_tree_2 = Fir_tree(8)
fir_tree_1.print_fir_tree()
print()
fir_tree_2.print_fir_tree()