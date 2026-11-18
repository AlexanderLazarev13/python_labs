from src.lab08.models import make_student, student_age, student_to_dict, student_from_dict, format_student, update_student
from src.lab08.serialize import students_from_csv, students_from_json, students_to_json
if __name__ == '__main__':
    print('Примермы работы функций модуля "models":')
    print('')
    print(f'Входные данные {"Иванов Иван Иванович", "2007-05-14", "БИВТ-26-6-1", 4.3}')
    student_1 = make_student("Иванов Иван Иванович", "2007-05-14", "БИВТ-26-6-1", 4.3)
    print(f'Результат функции "make_student" на данных выше: {student_1}')
    print('')
    student_age_now = student_age(student_1)
    print(f'Результат функции "student_age" на данных выше: {student_age_now}')
    print('')
    student_copy = student_to_dict(student_1)
    print(f'Результат функции "student_to_dict" на данных выше (совапдают ли адреса записей): {student_copy is student_1}')
    print(f'Результат функции "student_to_dict" на данных выше (сама копия): {student_copy}')
    print('')
    data = {"fio": "Петров Пётр Петрович", "birthdate": "2008-03-26", "respect": "got it", "group": "БИВТ-26-6-6", "gpa": 3.5}
    print(f'Входные данные: {data}')
    student_2 = student_from_dict(data)
    print(f'Результат функции "student_from_dict" на данных выше: {student_2}')
    print('')
    print(f'Красивый вывод при помощи "format_student" последней записи: {format_student(student_2)}')
    print('')
    updated_student_2 = update_student(student_2, gpa=4.78)
    print(f'★ Результат функции "update_student(последняя запись, gpa=4.78)": {updated_student_2}')
    print('')
    print('')

    print('Примеры работы функций модуля "serialize":')
    print('')
    students_json = students_from_json('data/lab08/input/students_input.json')
    students_csv = students_from_csv('data/lab08/input/students_input.csv')
    print('Функциям "students_from_json" и "students_from_csv" были поданы одинаковые данные в нужных для каждой функции формате файла.')
    print(f'Результат функции "students_from_json": {students_json}')
    print(f'★ Результат функции "students_from_csv": {students_csv}')
    print('')
    students_to_json(students_csv, 'data/lab08/out/students_output.json')

    try:
        students_from_json('data/lab08/input/students_bad.json')
    except ValueError as e:
        print(e)
    print('')

    try:
        students_from_csv('data/lab08/input/students_bad.csv')
    except ValueError as e:
        print(e)