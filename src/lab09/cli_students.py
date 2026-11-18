import argparse
def main():
    '''
    Скрипт для работы с базами данных в формате .csv через терминал.
    '''

    parser = argparse.ArgumentParser(description="Работа с базами данных")
    parser.add_argument("--db", default='data/lab09/students.csv', help=f'путь к csv-хранилищу ("по умолчанию data/lab09/students.csv")')
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("add", help='Добавление записи')
    p1.add_argument("--fio", dest="fio", required=True, help='ФИО добавляемого студента')
    p1.add_argument("--birthdate", dest="birthdate", required=True, help='Дата рождения добавляемого студента')
    p1.add_argument("--group", dest="group", required=True, help='Группа добавляемого студента')
    p1.add_argument("--gpa", dest="gpa", required=True, help='Средний балл добавляемого студента')

    p2 = sub.add_parser("list", help='Сортировка (при нужде) и вывод списком данных из файла')
    p2.add_argument("--sort", dets='sort', default=None, help='Аргумент для сортировки, если она требуется')

    p3 = sub.




