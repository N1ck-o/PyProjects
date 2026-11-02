import statistics
import random


def stats_calculator(*args, mode='basic'):
    results = {
        'Максимум:': max(args),
        'Минимум:': min(args),
        'Среднее:': statistics.mean(args)
    }
    if mode in ['advanced', 'scientific']:
        results['Медиана:'] = statistics.median(args)
        results['Мода:'] = statistics.mode(args)
    if mode == 'scientific':
        if any(x < 0 for x in args):
            results['Среднее геометрическое:'] = 'Есть число меньше нуля. Посчитать невозможно'
        else:
<<<<<<< HEAD
            results['Среднее геометрическое:'] = statistics.geometric_mean(args)
        if 0 in args:
            results['Среднее гармоническое:'] = 'Есть ноль. Посчитать невозможно'
=======
            print('Среднее геометрическое:', statistics.geometric_mean(args))
        if 0 in args:
            print('Ноль в числах. Среднее гармоническое найти не получилось.')
>>>>>>> 456ad1744c7c9d9d6e507de5cf153a058e7187c8
        else:
            results['Среднее гармоническое:'] = statistics.harmonic_mean(args)
    return results


def print_results(results):
    for key, value in results.items():
        if isinstance(value, float):
            print(f'{key} {value:.4f}')
        else:
            print(f'{key} {value}')


while True:
    try:
        counts = int(input('Введите количество чисел: '))
        if counts <= 0:
            print('Количество чисел не может быть меньше или равно нулю.')
            exit()
        mode = input('Введите уровень вычислений (basic, advanced, scientific) или оставьте пустым: ')
        if mode not in ['basic', 'advanced', 'scientific']:
            if mode == '':
                mode = 'basic'
            else:
                print('Введён некорректный уровень вычислений.')
                exit()
        lower_generate = int(input('Ввведите нижнюю границу: '))
        upper_generate = int(input('Введите верхнюю границу: '))
        if lower_generate > upper_generate:
            print('Нижняя граница не может быть больше верхней.')
            exit()
    except ValueError:
        print('Введены некорректные данные')
        exit()
    numbers = [random.randint(lower_generate, upper_generate) for _ in range(counts)]
    print_results(stats_calculator(*numbers, mode=mode))
    while True:
        print('Ещё раз? (y,n)')
        s = input().strip().lower()
        if s == 'y':
            break
        else:
            exit()
