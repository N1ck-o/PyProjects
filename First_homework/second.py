import statistics
import random
import sys


def stats_calculator(*args, mode='basic'):
    print('Максимум:', max(args))
    print('Минимум:', min(args))
    print('Среднее арифметическое:', statistics.mean(args))
    if mode in ['advanced', 'scientific']:
        print('Медиана:', statistics.median(args))
        print('Мода:', statistics.mode(args))
    if mode == 'scientific':
        print('Геометрическая прогрессия:', statistics.geometric_mean(args))
        print('Гармоническая прогрессия:', statistics.harmonic_mean(args))

while True:
    try:
        counts = int(input('Введите количество чисел: '))
        if counts <= 0:
            print('Количество чисел не может быть меньше или равно нулю.')
            sys.exit()
        mode = str(input('Введите уровень вычислений (basic, advanced, scientific) или оставьте пустым: '))
        if mode not in ['basic', 'advanced', 'scientific']:
            if mode == '':
                mode = 'basic'
            else:
                print('Введён некорректный уровень вычислений.')
                sys.exit()
        lower_generate = int(input('Ввведите нижнюю границу: '))
        upper_generate = int(input('Введите верхнюю границу: '))
        if lower_generate > upper_generate:
            print('Нижняя граница не может быть больше верхней.')
            sys.exit()
        numbers = [random.randint(lower_generate, upper_generate) for _ in range(counts)]
        stats_calculator(*numbers, mode=mode)
        while True:
            print('Ещё раз? (y,n)')
            s = str(input().strip().lower())
            if s == 'y':
                break
            if s == 'n':
                exit()
    except ValueError:
        print('Некорректно.')
