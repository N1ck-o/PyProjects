import math


def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Комплексные корни.')
    elif d == 0:
        print(f'x = {-b / (2 * a)}')
    else:
        print(f'x1 = {(-b + math.sqrt(d)) / (2 * a)} x2 = {(-b - math.sqrt(d)) / (2 * a)}')


while True:
    try:
        a = float(input('Введите коэффицент a: '))
        b = float(input('Введите коэффицент b: '))
        c = float(input('Введите коэффицент c: '))
        solve(a, b, c)
        while True:
            print('Ещё раз? (y,n)')
            s = str(input().strip().lower())
            if s == 'y':
                break
            if s == 'n':
                exit()
    except ValueError:
        print('Некорректно.')
