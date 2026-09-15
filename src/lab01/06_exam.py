n = int(input('in_1: '))
students = []
for i in range(n):
    a = input(f'in_{i+2}: ')
    students.append(a.split())

count = 0
for x in students:
    if x[3] == 'True': count += 1

print(f'out: {count} {len(students) - count}')