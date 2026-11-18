from src.lab08.models import student_to_dict, student_from_dict
from src.lab04.io_to_txt import ensure_parent_dir
from pathlib import Path
import json
import csv
def students_to_json(students: list[dict], path: str | Path) -> None:
    '''
    Запись списка студентов в .json файл.
    '''
    data = [student_to_dict(s) for s in students]
    final_path = Path(path)
    if final_path.suffix != '.json': raise ValueError('Файл для результата должен быть в формате ".json"')
    ensure_parent_dir(final_path)

    with open(final_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str | Path) -> list[dict]:
    '''
    Преобразование .json файла в список студентов.
    '''
    final_path = Path(path)
    if final_path.suffix != '.json': raise ValueError('Файл для обработки должен быть в формате ".json"')
    with open(final_path, 'r', encoding='utf-8') as f:
        students = json.load(f)

    checked_students = []
    for i, st in enumerate(students):
        try:
            checked_students.append(student_from_dict(st))
        except ValueError as e:
            raise ValueError(f'Ошибка в записи №{i + 1}: {e}')
    return checked_students

def students_from_csv(path: str | Path) -> list[dict]:
    '''
    Преобразование .csv файла в список студентов.
    '''
    final_path = Path(path)
    if final_path.suffix != '.csv': raise ValueError('Файл для обработки должен быть в формате ".csv"')
    with open(final_path, 'r', encoding='utf-8', newline='') as f:
        sample = f.read()
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample)
        f.seek(0)
        students = csv.DictReader(f, dialect=dialect)
        if not sniffer.has_header(sample): raise ValueError('В файле отсутсвует заголовок')
        if students.fieldnames != ['fio', 'birthdate', 'group', 'gpa']: raise ValueError('Заголовок не соответсвует требуемым параметрам: "fio", "birthdate", "group", "gpa"')
        new_students = list(students)

    checked_students = []
    for i, st in enumerate(new_students):
        try:
            checked_students.append(student_from_dict(st))
        except ValueError as e:
            raise ValueError(f'Ошибка в записи №{i + 1}: {e}')
    return checked_students