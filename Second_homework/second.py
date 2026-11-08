from collections import defaultdict
from itertools import combinations


def search_in_friends(d):
    answer_dict = defaultdict(set)
    names = list(d.keys())
    for n1, n2 in combinations(names, 2):
        pairs = d[n1] & d[n2]
        if len(pairs) >= 2:
            answer_dict[n1].add(n2)
    return answer_dict


def print_answer(ans):
    for key in ans.keys():
        for elem in ans[key]:
            print(f'{key} - {elem}')


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
    print('Пары друзей с двумя и более общими друзьями:')
    print_answer(search_in_friends(friends))
    while True:
        print('Ещё раз? (y,n)')
        s = input().strip().lower()
        if s == 'y':
            break
        if s == 'n':
            exit()
