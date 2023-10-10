# Напишите функцию для транспонирования матрицы
# from time import sleep
# def transpose_matrix(matrix: list) -> list:
#     result_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             result_matrix[j][i] = matrix[i][j]
#             print(result_matrix)
#             sleep(1)
#     return result_matrix

# matrix_3x2 = [[1,2,3], [4,5,6]]
# matrix_3x3 = [[1,2,3], [4,5,6], [7,8,9]]
# matrix_2x5 = [[1,2], [3,4], [5,6], [7,8], [9,10]]

# print(f'First matrix - {transpose_matrix(matrix_3x2)}')
# print(f'Second matrix - {transpose_matrix(matrix_3x3)}')
# print(f'Third matrix - {transpose_matrix(matrix_2x5)}')

from random import randint
        
class Matrix:
    def __init__(self, rows, lines):
        self.rows = rows
        self.lines = lines
        
    def create_matrix(self):
        return [[randint(0,10) for _ in range(self.rows)] for _ in range(self.lines)]
    
    def transpose_matrix(matrix):
        result_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result_matrix[j][i] = matrix[i][j]
        return result_matrix
    

        
    
matrix_3x2 = Matrix(3,2).create_matrix()
matrix_3x3 = Matrix(3,3).create_matrix()
matrix_2x5 = Matrix(2,5).create_matrix()

for matrix in [matrix_3x2, matrix_3x3, matrix_2x5]:
    print(matrix)
    matrix = Matrix.transpose_matrix(matrix)
    print(matrix)
    print('-' * 50)
