name = input('ФИО: ')
fio = name.split()
print(f'Инициалы: {''.join([x[0] for x in fio])}.')
print(f'Длина (символов): {2 + sum([len(x) for x in fio])}')