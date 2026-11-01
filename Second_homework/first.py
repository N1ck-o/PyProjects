import sys
import random
import numpy as np


def generate_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([random.randint(-100,100) for _ in range(n)])
    return matrix


def search_in_matrix(matrix, n):
    points = []
    print(np.array(matrix))
    for r in range(n):
        index_column, value = min(enumerate(matrix[r]), key=lambda x: x[1])
        for row in range(n):
            if value < matrix[row][index_column]:
                break
            if row == n-1:
                points.append([matrix[r][index_column], r+1, index_column+1])
    return points


try:
    n = int(input('Введите размер матрицы: '))
    if n <= 0:
        print('Матрица не может быть <=0')
        sys.exit()
    answer = search_in_matrix((generate_matrix(n)), n)
    if answer:
        print(f'Значение: {answer[0][0]}. Индексы: i = {answer[0][1]}, j = {answer[0][2]}')
    else:
        print('Седловых точек нет.')
except ValueError:
    print('Некорректно.')