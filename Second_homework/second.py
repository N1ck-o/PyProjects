from collections import defaultdict
from itertools import combinations

while True:
    friends = defaultdict(set)
    print('Введите все пары друзей (Иван --- Матвей) или !!! для остановки:')
    while True:
        input_str = input().strip()
        if input_str == "!!!":
            break
        if " --- " in input_str:
            name1, name2 = input_str.split(" --- ")
            name1 = name1.strip()
            name2 = name2.strip()
            friends[name1].add(name2)
            friends[name2].add(name1)
    peoples = list(friends.keys())
    print('Пары друзей с двумя или более общими знакомыми:')
    for n1, n2 in combinations(peoples, 2):
        pairs = friends[n1] & friends[n2]
        if len(pairs) >= 2:
            print(f'{n1} --- {n2}')
    while True:
        print('Ещё раз? (y,n)')
        s = input().strip().lower()
        if s == 'y':
            break
        if s == 'n':
            exit()
