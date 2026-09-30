def format_record(rec: tuple[str, str, float]) -> str:
    '''
    Функция преобразует данные из кортежа rec в строку в формате:

    Иванов И.И., гр. BIVT-25, GPA 4.60
    или
    Иванов И., гр. BIVT-25, GPA 4.60

    Формат данных в rec: 
    первый элемент - ФИО/ФИ, 
    второй - группа, 
    третий - gpa в формате float.

    Если данные некоректны:
    пустое имя, пустая группа, неверный формат ввода gpa, 
    неверное количество элементов, gpa не удовлетворяет диапазону от 0 до 5
    
    будет возвращено ValueError.
    '''
    if rec[0].strip() == '' or rec[1].strip() == '' or (not (type(rec[2]) is float)) or \
        (not (0 <= rec[2] <= 5.00)) or (not (type(rec) is tuple)) or len(rec) != 3: 
        raise ValueError('Данные некоректны')
    initials = rec[0].strip().split()[0].capitalize() + ' ' + \
        ''.join([x[0].upper() + '.'  for x in rec[0].strip().split()[1:]]) 
    return f'{initials}, гр. {rec[1]}, GPA {rec[2]:.2f}'

for ex in [("Иванов Иван Иванович", "BIVT-25", 4.6), ("Петров Пётр", "IKBO-12", 5.0), \
           ("Петров Пётр Петрович", "IKBO-12", 5.0), \
           ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)]:
    for l in ex:
        if type(l) == str and l.strip() == '': print(f'"{l}"')
        else: print(l)
    print('->')
    print(format_record(ex))
    print('')


print(('Лазарев Александр Викторович', 'BIVT-26', 25.37))
print('->')
print(format_record(('Лазарев Александр Викторович', 'BIVT-26', 'ab')))
print(format_record())