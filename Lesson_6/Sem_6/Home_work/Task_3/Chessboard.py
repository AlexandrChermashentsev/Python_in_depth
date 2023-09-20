'''
Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, 
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, 
каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
'''
from time import sleep
def print_chessboard(lines: list[list]):
    for i in lines:
        for j in i:
            print(f'[{j}]', end='')
        print()

def create_chessboard():
    lines = []
    for _ in range(8):
        line = []
        for _2 in range(8):
            line.append(0)
        lines.append(line)
    return lines

def transpose_matrix(matrix: list) -> list:
    result_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[j][i] = matrix[i][j]
    return result_matrix

def can_put(coordinate: str, board: list) -> bool:
    y, x = list(map(int, coordinate.split()))
    y, x = y-1, x-1

    if 1 in board[x] or 1 in transpose_matrix(board)[y]:
        return False
    return True

def can_put_diagonals(coordinate: str, board: list) -> bool:
    result = True
    point = list(map(int, coordinate.split()))
    x, y = point[0] - 1, point[1] - 1

    if board[y][x] == 1:
        return False
    while True:
        if x == -1 or  y == -1:
            break
        else:
            if board[y][x] == 1:
                # result = False
                return False
            x, y = x-1, y-1

    x, y = point[0] - 1, point[1] - 1
    while True:
        if x == 8 or y == 8:
            break
        else:
            if board[y][x] == 1:
                # result = False
                return False
                
            x, y = x+1, y+1

    x, y = point[0] - 1, point[1] - 1
    while True:
        if x == -1 or y == 8:
            break
        else:
            if board[y][x] == 1:
                # result = False
                return False
            x, y = x-1, y+1


    x, y = point[0] - 1, point[1] - 1
    while True:
        if x == 8 or y == -1:
            break
        else:
            if board[y][x] == 1:
                # result = False
                return False
            x, y = x + 1, y - 1

    return result

def can_put_diagonals_v2(coordinate: str, board: list) -> bool:
    point = list(map(int, coordinate.split()))
    x, y = point[0] - 1, point[1] - 1
    trends = ['left_up', 'right_down', 'left_down', 'right_up']
    if board[y][x] == 1:
        return False
    
    while trends:
        trend = trends[0]
        match trend:
            case 'left_up':
                if x == -1 or  y == -1:
                    trends.pop(0)
                    x, y = point[0] - 1, point[1] - 1
                else:
                    if board[y][x] == 1:
                        return False
                    x, y = x-1, y-1

            case 'right_up':
                if x == 8 or y == 8:
                    trends.pop(0)
                    x, y = point[0] - 1, point[1] - 1
                else:
                    if board[y][x] == 1:
                        return False
                    x, y = x+1, y+1  

            case 'left_down':
                if x == -1 or y == 8:
                    trends.pop(0)
                    x, y = point[0] - 1, point[1] - 1
                else:
                    if board[y][x] == 1:
                        return False
                    x, y = x-1, y+1

            case 'right_down':
                if x == 8 or y == -1:
                    trends.pop(0)
                    x, y = point[0] - 1, point[1] - 1
                else:
                    if board[y][x] == 1:
                        return False
                    x, y = x+1, y-1
    return True

def add_figure(coordinate: str, board: list) -> list:
    y, x = list(map(int, coordinate.split()))
    y, x = y-1, x-1
    board[x][y] = 1
    return board

if __name__ == '__main__':
    chessboard = create_chessboard()
    count_fugures = 0
    while count_fugures != 8:
        print_chessboard(chessboard)
        coordinate = input('На какую ячейку добавить фигуру?(координату писать в формате "0 0")\n-> ')

        if can_put_diagonals(coordinate, chessboard) and can_put(coordinate, chessboard):
            add_figure(coordinate, chessboard)
            count_fugures += 1
        else: 
            print('Сюда ставить фигуру нельзя')
        sleep(1)
        print(f'Осталось расставить {8 - count_fugures} фигур')