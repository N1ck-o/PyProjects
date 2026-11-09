students = {
    'А': [2, 4, 3, 4],
    'B': [5, 5, 3, 4, 3],
    'C': [4, 4, 3],
    'D': [3],
    'F': [3]
}
students_grades = 0


def solve(item):
    global students_grades
    name = item[0]
    grades = item[1]
    if len(grades) == 0:
        avg = 0
    else:
        students_grades += len(grades)
        avg = round(sum(grades)/len(grades), 2)
    return name, avg


while True:
    if not students:
        exit('Словарь пуст.')
    avg_dict = dict(map(solve, students.items()))
    print(avg_dict)
    print(students_grades)
    while True:
        print('Ещё раз? (y,n)')
        s = input().strip().lower()
        if s == 'y':
            break
        if s == 'n':
            exit()
