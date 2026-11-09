def encode(s):
    s_reverse = ''
    char = s[0]
    count = 0
    for elem in s:
        if elem == char:
            count += 1
        else:
            s_reverse = s_reverse + f'{char}{count}'
            char = elem
            count = 1
    s_reverse += f'{char}{count}'
    return s_reverse


def decode(s_reverse):
    i = 1
    s = ''
    for elem in s_reverse[::2]:
        s += elem*int(s_reverse[i])
        i += 2
    return s


while True:
    input_s = input('Введите строку: ').strip().lower()
    if input_s == '':
        exit('Пустая строка.')
    print(encode(input_s), decode(encode(input_s)))
    while True:
        print('Ещё раз? (y,n)')
        choise = input().strip().lower()
        if choise == 'y':
            break
        if choise == 'n':
            exit()
