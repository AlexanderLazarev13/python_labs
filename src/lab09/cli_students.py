import argparse
from src.lab08.models import make_student, format_student
from src.lab09.group import add_student, list_students, find_students, remove_student, update_student_with_upload, stats
def main():
    '''
    Скрипт для работы с базами данных в формате .csv через терминал.
    '''

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--db", default='data/lab09/students.csv', help='путь к csv-хранилищу ("по умолчанию data/lab09/students.csv")')
    parser = argparse.ArgumentParser(description="Работа с базами данных")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("add", parents=[parent_parser], help='Добавление записи')
    p1.add_argument("--fio", dest="fio", required=True, help='ФИО добавляемого студента')
    p1.add_argument("--birthdate", dest="birthdate", required=True, help='Дата рождения добавляемого студента')
    p1.add_argument("--group", dest="group", required=True, help='Группа добавляемого студента')
    p1.add_argument("--gpa", type=float, dest="gpa", required=True, help='Средний балл добавляемого студента')

    p2 = sub.add_parser("list", parents=[parent_parser], help='Сортировка (при нужде) и вывод списком данных из файла')
    p2.add_argument("--sort", dest='sort', default=None, help='Аргумент для сортировки, если она требуется')

    p3 = sub.add_parser("find", parents=[parent_parser], help='Поиск студентов с переданной подстрокой в ФИО (без учёта регистра)')
    p3.add_argument("--q", dest='string', required=True, help='Подстрока для поиска в ФИО')

    p4 = sub.add_parser("remove", parents=[parent_parser], help='Удаление записей с переданным ФИО и вывод их количества')
    p4.add_argument("--fio", dest='fio', required=True, help='ФИО по которому удалятся записей')

    p5 = sub.add_parser("update", parents=[parent_parser], help='Обновление первой записи с переданным ФИО')
    p5.add_argument("--fio", dest='fio', required=True, help='ФИО для поиска')
    p5.add_argument("--gpa", type=float, dest='gpa', default=None, help='Обновлённый средний балл')
    p5.add_argument("--group", dest='group', default=None, help='Обновлённая группа')
    p5.add_argument("--birthdate", dest='birthdate', default=None, help='Обновлённая дата рождения')

    p6 = sub.add_parser("stats", parents=[parent_parser], help='Вывод статистики по файлу с базой данных о студентах')

    args = parser.parse_args()

    if args.command ==  'add':
        student_to_add = make_student(args.fio, args.birthdate, args.group, args.gpa)
        add_student(args.db, student_to_add)
        print(f'В файл {args.db} добавлена запись: {format_student(student_to_add)}')
    elif args.command == 'list':
        sorted_students = list_students(args.db, sort_by=args.sort)
        if len(sorted_students) == 0: print('Записи о студентах отсутсвуют')
        else:
            print(f'Отсортированные данные о студентах из файла {args.db} по параметру - {args.sort}')
            for rec in sorted_students:
                print(format_student(rec))
    elif args.command == 'find':
        found_students = find_students(args.db, args.string)
        if len(found_students) == 0: print(f'Студенты с подстрокой {args.string} в ФИО отсутсвуют в файле {args.db}')
        else:
            print(f'Студенты с подстрокой {args.string} в ФИО из файла {args.db}:')
            for rec in found_students:
                print(format_student(rec))
    elif args.command == 'remove':
        number_of_removed = remove_student(args.db, args.fio)
        print(f'Удалено {number_of_removed} записей(и) с ФИО - {args.fio} из файла {args.db}')
    elif args.command == 'update':
        fields = dict()
        if args.gpa is not None: fields['gpa'] = args.gpa
        if args.group is not None: fields['group'] = args.group
        if args.birthdate is not None: fields['birthdate'] = args.birthdate
        if len(fields) == 0: parser.error('Нужно обновить хотя бы один параметр')
        if update_student_with_upload(args.db, args.fio, **fields): print(f'Обновлена первая найденная запись в файле {args.db} с ФИО {args.fio}: {fields}')
        else: print(f'Студент с ФИО {args.fio} не найден в файле {args.db}')

    elif args.command == 'stats':
        statistics_about_file = stats(args.db)
        print(f'Статистика по файлу {args.db}:')
        print('')
        print(f'Количество студентов: {statistics_about_file['count']}')
        print('-' * 60)
        print(f'Наименьший GPA: {statistics_about_file['min_gpa']}')
        print(f'Наибольший GPA: {statistics_about_file['max_gpa']}')
        print(f'Средний GPA: {statistics_about_file['avg_gpa']:.2f}')
        print('-' * 60)
        for gr in statistics_about_file['groups']:
            print(f'Количество записей с группой {gr}: {statistics_about_file['groups'][gr]}')
        print('-' * 60)
        print('Топ-5 студентов ')
        k = 1
        for st in statistics_about_file['top_5_students']:
            print(f'{k}. {format_student(st)}')
            k += 1
        
if __name__ == '__main__':
    main()