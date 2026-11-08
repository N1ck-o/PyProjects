import random
from datetime import datetime, timedelta, date


def generate_dates(least, greatest, cnt):
    dates = []
    diff = (greatest-least).days
    for _ in range(cnt):
        random_diff = random.randint(0, diff)
        random_date = least + timedelta(days=random_diff)
        dates.append(random_date)
    return dates


def check_dates(*dates):
    today = date.today()
    next_dates = []
    for d in dates:
        if d > today:
            next_dates.append(d)
    return sorted(dates), next_dates, len(dates)


def print_dates(dates, next_dates, n):
    print(f"Количество дат: {n}"
          f"\nМинимальная дата: {dates[0].strftime('%d.%m.%#Y')}"
          f"\nМаксимальная дата: {dates[-1].strftime('%d.%m.%#Y')}")
    print('Все даты:')
    for d in dates:
        print(d.strftime('%d.%m.%#Y'))
    print('Будущие даты:')
    for d in next_dates:
        print(d.strftime('%d.%m.%#Y'))


while True:
    try:
        count = int(input('Введите количество дат: '))
        if count <= 0:
            print('Количество дат не может быть меньше или равно нулю.')
            exit()
        input_start = input("Введите стартовую дату (17.01.2026): ")
        input_finish = input("Введите конечную дату (31.12.2026): ")
        least_date = datetime.strptime(input_start, "%d.%m.%Y").date()
        greatest_date = datetime.strptime(input_finish, "%d.%m.%Y").date()
    except ValueError:
        print('Введены некорректные данные.')
        exit()
    if least_date > greatest_date:
        print('Минимальный год не может быть больше максимального.')
        exit()
    generated = generate_dates(least_date, greatest_date, count)
    list_dates, list_next_dates, cnt = check_dates(*generated)
    print_dates(list_dates, list_next_dates, cnt)
    while True:
        print('Ещё раз? (y,n)')
        s = input().strip().lower()
        if s == 'y':
            break
        if s == 'n':
            exit()
