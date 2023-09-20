'''
Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''


from Task_3.Chessboard import print_chessboard
from Task_3.Chessboard import create_chessboard
from Task_3.Chessboard import can_put
from Task_3.Chessboard import can_put_diagonals_v2
from Task_3.Chessboard import add_figure
import random



if __name__ == '__main__':
    count_figures = 0
    chessboard = create_chessboard()
    temp_count = 0
    succes_chessboard = 0

    while succes_chessboard != 4:
        if count_figures == 8:
            print(f'{count_figures = }')
            print_chessboard(chessboard)
            succes_chessboard += 1
            chessboard = create_chessboard()
            temp_count, count_figures = 0, 0
            print('-' * 30)
        elif temp_count == 10000:
            chessboard = create_chessboard()
            temp_count, count_figures = 0, 0
        else:
            coordinate = f'{random.randint(1, 8)} {random.randint(1, 8)}'
            if can_put_diagonals_v2(coordinate, chessboard) and can_put(coordinate, chessboard):
                add_figure(coordinate, chessboard)
                count_figures += 1
        temp_count += 1            

