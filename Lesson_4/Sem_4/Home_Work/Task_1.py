# Напишите функцию для транспонирования матрицы
from time import sleep
def transpose_matrix(matrix: list) -> list:
    result_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[j][i] = matrix[i][j]
            print(result_matrix)
            sleep(1)
    return result_matrix

matrix_3x2 = [[1,2,3], [4,5,6]]
matrix_3x3 = [[1,2,3], [4,5,6], [7,8,9]]
matrix_2x5 = [[1,2], [3,4], [5,6], [7,8], [9,10]]

print(f'First matrix - {transpose_matrix(matrix_3x2)}')
print(f'Second matrix - {transpose_matrix(matrix_3x3)}')
print(f'Third matrix - {transpose_matrix(matrix_2x5)}')
