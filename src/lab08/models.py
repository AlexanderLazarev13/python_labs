from datetime import date
STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")

def make_student(fio: str, birthdate: str, group: str, gpa: int | float) -> dict:
    '''
    Создание записи после проверки корректности данных,
    при некорректности - ValueError.
    '''
    if type(birthdate) != str: raise ValueError('Неверный формат даты рождения')
    try:
        b = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError('Дата не существует. Верная запись: "YYYY-MM-DD"')
    if b > date.today(): raise ValueError('Дата из будущего')
    if type(fio) != str or fio.strip() == '': raise ValueError('Неверный формат ФИО')
    if type(group) != str or group.strip() == '': raise ValueError('Неверный формат группы')
    if ((type(gpa) != int) and (type(gpa) != float)) or not (0 <= gpa <= 5): raise ValueError('Неверный формат GPA')

    return {'fio': fio, 'birthdate': birthdate, 'group': group, 'gpa': float(gpa)}

def validate_student(rec: dict) -> None:
    '''
    Валидация записи о студенте.
    '''
    if type(rec) != dict: raise ValueError('Запись должна быть словарём')
    if set(rec) != set(("fio", "birthdate", "group", "gpa")): raise ValueError('Неверный набор параметров')
    if type(rec['birthdate']) != str: raise ValueError('Неверный формат даты рождения')
    try:
        b = date.fromisoformat(rec['birthdate'])
    except ValueError:
        raise ValueError('Дата не существует. Верная запись: "YYYY-MM-DD"')
    if b > date.today(): raise ValueError('Дата из будущего')
    if type(rec['fio']) != str or rec['fio'].strip() == '': raise ValueError('Неверный формат ФИО')
    if type(rec['group']) != str or rec['group'].strip() == '': raise ValueError('Неверный формат группы')
    if ((type(rec['gpa']) != int) and (type(rec['gpa']) != float)) or not (0 <= rec['gpa'] <= 5): raise ValueError('Неверный формат GPA')

def student_age(rec: dict, today=None) -> int:
    '''
    Вычисление возраста студента, по умолчанию, на сегодня.
    При желании посчитать на другой день - задать явно через параметр today.
    '''
    validate_student(rec)
    b = date.fromisoformat(rec["birthdate"])
    if today != None:
        if type(today) != str: raise ValueError('Дата должна быть передана строкой')
        today_date = date.fromisoformat(today)
    else:
        today_date = date.today()
    if today_date < b: raise ValueError('Невозможно вычислить возраст на дату раньше даты рождения')
    if today_date.month < b.month: return today_date.year - b.year - 1
    if today_date.month == b.month and today_date.day < b.day: return today_date.year - b.year - 1
    return today_date.year - b.year

def student_to_dict(rec: dict) -> dict:
    '''
    Создание копии студента при успешной валидации.
    '''
    validate_student(rec)
    return dict(rec)

def student_from_dict(d: dict) -> dict:
    '''
    Десериализация данных из словаря только по нужным параметрам.
    '''
    for k in ['fio', 'birthdate', 'group', 'gpa']:
        if k not in d: raise ValueError(f'Параметр {k} отсутсвует')
    rec = make_student(d['fio'], d['birthdate'], d['group'], float(d['gpa']))
    validate_student(rec)
    return rec

def format_student(rec: dict) -> str:
    '''
    Красивый вывод записи данных о студенте.
    '''
    validate_student(rec)
    initials = rec['fio'].strip().split()[0].capitalize() + ' ' + \
                ''.join([x[0].upper() + '.'  for x in rec['fio'].strip().split()[1:]]) 
    return f'{initials} ({rec['group']}), {student_age(rec)}, GPA {rec['gpa']:.2f}'

def update_student(rec: dict, **fields) -> dict:
    '''
    Создание новой записи студента с обновлёнными полями.
    '''
    new_rec = student_to_dict(rec)
    for k1 in fields.keys():
        if k1 not in ['fio', 'birthdate', 'group', 'gpa']: raise KeyError(f'"{k1}" не является параметром для создания записи студента')
    for k2, v in fields.items():
        try:
            new_rec[k2] = v
            validate_student(new_rec)
        except ValueError as e:
            raise ValueError(f'Ошибка в значении параметра "{k2}": {e}')
    return new_rec
