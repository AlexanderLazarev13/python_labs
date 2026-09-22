def format_record(rec: tuple[str, str, float]) -> str:
    '''
    Функция преобразует данные из кортежа rec в строку в формате: 
    Иванов И.И., гр. BIVT-25, GPA 4.60.
    Формат данных в rec: 
    первый элемент - ФИО/ФИ, 
    второй - группа, 
    третий - gpa в формате float.
    Если данные некоректны (пустое имя, пустая группа, неверный формат ввода gpa) будет
    возвращено ValueError.
    '''
    if rec[0].strip() == '' or rec[1].strip() == '' or (not (type(rec[2]) is float)): 
        return ValueError
    initials = rec[0].strip().split()[0].capitalize() + ' ' + \
        ''.join([x[0].upper() + '.'  for x in rec[0].strip().split()[1:]]) 
    return f'{initials}, гр. {rec[1]}, GPA {rec[2]:.2f}'

if __name__ == '__main__':
    assert format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)) \
        == "Иванов И.И., гр. BIVT-25, GPA 4.60"
    assert format_record(("Петров Пётр", "IKBO-12", 5.0)) \
        == "Петров П., гр. IKBO-12, GPA 5.00"
    assert format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)) \
        == "Петров П.П., гр. IKBO-12, GPA 5.00"
    assert format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)) \
        == "Сидорова А.С., гр. ABB-01, GPA 4.00"
    assert format_record(('', 'BIVT-26', 4.8)) == ValueError
    assert format_record(('Лазарев Александр Викторович', '   ', 5.0)) == ValueError
    assert format_record(('Лазарев Александр Викторович', 'BIVT-26', 5)) == ValueError
    print('Все тесты функции format_record пройдены!')