import random
from operator import itemgetter


def generate_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([random.randint(-100,100) for _ in range(n)])
    for row in range(n):
        print(matrix[row])
    return matrix


def search_in_matrix(matrix, n):
    points = []
    for r in range(n):
        index_column, value = min(enumerate(matrix[r]), key=itemgetter(1))
        if matrix[r].count(value) > 1:
            indices = [x for x, val in enumerate(matrix[r]) if val == value]
            for elem in indices:
                for row in range(n):
                    if value < matrix[row][elem]:
                        break
                    if row == n - 1:
                        points.append([matrix[r][elem], r + 1, elem + 1])
        else:
            for row in range(n):
                if value < matrix[row][index_column]:
                    break
                if row == n-1:
                    points.append([matrix[r][index_column], r+1, index_column+1])
    return points


while True:
    try:
        n = int(input('Введите размер матрицы: '))
        if n <= 0:
            print('Матрица не может быть <=0')
            exit()
    except ValueError:
        print('Некорректно введен размер матрицы.')
        exit()
    answer = search_in_matrix(generate_matrix(n), n)
    if answer:
        for elem in answer:
            print(f'Значение: {elem[0]}. Индексы: i = {elem[1]}, j = {elem[2]}')
    else:
        print('Седловых точек нет.')
    while True:
        print('Ещё раз? (y,n)')
        s = input().strip().lower()
        if s == 'y':
            break
        if s == 'n':
            exit()
