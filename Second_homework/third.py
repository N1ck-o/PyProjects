from collections import defaultdict
from itertools import combinations


def search_in_students(d):
    students_names = list(d.keys())
    common_skills = defaultdict(set)
    superset_students = []
    for s1, s2 in combinations(students_names, 2):
        if d[s1] == d[s2]:
            common_skills[s1].add(s2)
        elif d[s1].issubset(d[s2]):
            if s2 not in superset_students:
                superset_students.append(s2)
        elif d[s1].issuperset(d[s2]):
            if s1 not in superset_students:
                superset_students.append(s1)
    return common_skills, superset_students


def maximum_skills(d):
    max_skills = []
    len_skills = 0
    for key, value in d.items():
        current = len(value)
        if current > len_skills:
            len_skills = current
            max_skills = [key]
        elif current == len_skills:
            max_skills.append(key)
    return max_skills


def matrix_students(d):
    names = list(d.keys())
    matrix = [[0.0] * len(names) for _ in range(len(names))]
    i = 0
    for s1 in names:
        j = 0
        for s2 in names:
            s1_skills = d[s1]
            s2_skills = d[s2]
            if len(s1_skills | s2_skills) == 0:
                matrix[i][j] = 0.00
                j += 1
            else:
                matrix[i][j] = round(len(s1_skills & s2_skills) / len(s1_skills | s2_skills),2)
                j += 1
        i += 1
    return matrix


def print_result(a, b, c, d, names):
    print('Студенты с одинаковыми навыками:')
    for key in a.keys():
        for elem in a[key]:
            print(f'{key} - {elem}')
    print('Студенты, чьи навыки надмножества навыков других студентов: ')
    print(*b)
    print('Студенты с наибольшим числом навыков:')
    print(*c)
    print('Матрица коэффициентов Жаккарда:')
    for row in range(len(names)):
        print(d[row])


while True:
    students_skills = defaultdict(set)
    while True:
        name = input('Введите имя студента (!!! - завершить): ').strip()
        if name == '!!!':
            break
        else:
            name = name.strip()
            while True:
                skill = input(f'Ввведите навык студента {name} (Пустая строка - завершить): ').strip()
                if skill == '':
                    break
                else:
                    skill.strip()
                    students_skills[name].add(skill)
    student_names = list(students_skills.keys())
    ans_a, ans_b = search_in_students(students_skills)
    ans_c = maximum_skills(students_skills)
    ans_d = matrix_students(students_skills)
    print_result(ans_a, ans_b, ans_c, ans_d, student_names)
    while True:
        print('Ещё раз? (y,n)')
        s = input().strip().lower()
        if s == 'y':
            break
        if s == 'n':
            exit()
