import random
import sys
from datetime import datetime, timedelta, date


def generate_dates(least, greatest, cnt):
    dates = []
    start_day = datetime(least, 1, 1)
    end_day = datetime(greatest, 12, 31)
    diff = (end_day-start_day).days
    for _ in range(cnt):
        random_diff = random.randint(0, diff)
        random_date = (start_day + timedelta(days=random_diff)).date()
        dates.append(random_date)
    return dates


def check_dates(*dates):
    today = date.today()
    next_dates = []
    for d in dates:
        if d > today:
            next_dates.append(d)
    return sorted(dates), next_dates, len(dates)


try:
    count = int(input('Введите количество дат: '))
    if count <= 0:
        print('Количество дат не может быть меньше или равно нулю.')
        sys.exit()
    least_date = int(input('Введите минимальный год: '))
    greatest_date = int(input('Введите максимальный год: '))
    if least_date > greatest_date:
        print('Минимальный год не может быть больше максимального.')
        sys.exit()
    generated = generate_dates(least_date, greatest_date, count)
    list_dates, list_next_dates, cnt = check_dates(*generated)
    print(f"Количество дат: {cnt}"
          f"\nМинимальная дата: {list_dates[0].strftime('%d.%m.%#Y')}"
          f"\nМаксимальная дата: {list_dates[-1].strftime('%d.%m.%#Y')}")
    print('Все даты:')
    for d in list_dates:
        print(d.strftime('%d.%m.%#Y'))
    print('Будущие даты:')
    for d in list_next_dates:
        print(d.strftime('%d.%m.%#Y'))
except ValueError:
    print('Некорректно.')
