from pathlib import Path
from src.lab08.models import STUDENT_FIELDS, validate_student, update_student
from src.lab08.serialize import students_from_csv
from src.lab04.io_to_txt import ensure_parent_dir
import csv
def ensure_storage(path: str | Path) -> None:
    '''
    Создание .csv файла с заголовком для хранения записей о студентах.
    '''
    p = Path(path)
    if p.suffix != '.csv': raise ValueError('Файл должен быть в .csv формате')
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(','.join(STUDENT_FIELDS), encoding='utf-8')

def load_students(path: str | Path) -> list[dict]:
    '''
    Проверка каждой записи и создание массива с записями о студентах.
    '''
    ready_students = students_from_csv(Path(path))
    return ready_students

def save_students(path: str | Path, students: list[dict]) -> None:
    '''
    Создание .csv файла с записями из списка "students".
    '''
    if Path(path).suffix != '.csv': raise ValueError('Файл должен быть в .csv формате')
    ensure_parent_dir(path)
    with open(Path(path), 'w', newline='', encoding='utf-8') as f:
        csv_file = csv.DictWriter(f, fieldnames=STUDENT_FIELDS, extrasaction='ignore')
        csv_file.writeheader()
        for st in students:
            validate_student(st)
        csv_file.writerows(students)


def add_student(path: str | Path, student: dict) -> None:
    '''
    Добавление студента в конец записи.
    '''
    validate_student(student)
    students_from_file = load_students(Path(path))
    for rec in students_from_file:
        if rec["fio"] == student["fio"]: raise ValueError('Студент с таким ФИО уже присутсвует в базе данных')
    students_from_file.append(student)
    save_students(path, students_from_file)

def list_students(path: str | Path, sort_by=None) -> list[dict]:
    '''
    Сортировка записей по параметру sort_by (sort_by ∈ {None, "fio", "gpa"}).
    '''
    if sort_by not in {None, "fio", "gpa"}: raise ValueError(f'"{sort_by}" не является параметром для сортировки')
    students_to_sort = load_students(Path(path))
    return sorted(students_to_sort, key=lambda x: x[sort_by])

def find_students(path: str | Path, substr: str) -> list[dict]:
    '''
    Поиск записей, в которые входит аргумент "substr" (без учёта регистра).
    '''
    students_to_find = load_students(Path(path))
    return [rec for rec in students_to_find if substr.lower() in rec['fio'].lower()]

def remove_student(path: str | Path, fio: str) -> int:
    '''
    Удаление записей со значением fio, совпадающим с заданным параметром.
    Вывод количества таких записей.
    '''
    students_to_check = load_students(Path(path))
    counter = 0
    for i, rec in enumerate(students_to_check):
        if rec["fio"] == fio:
            students_to_check.pop(i)
            counter += 1
    save_students(path, students_to_check)
    return counter

def update_student_with_upload(path, fio, **fields):
    '''
    Обновление параметров первого студента с заданным "fio".
    '''
    students = load_students(Path(path))
    for i, rec in enumerate(students):
        if rec['fio'] == fio:
            updated_student = update_student(rec, **fields)
            students[i] = updated_student
            save_students(path, students)
            return True
    return False

def stats(path: str | Path) -> dict:
    students_to_analyze = load_students(path)
    counter = len(students_to_analyze)
    min_gpa, max_gpa = min([rec['gpa'] for rec in students_to_analyze]), max([rec['gpa'] for rec in students_to_analyze])
    avg_gpa = sum([rec['gpa'] for rec in students_to_analyze]) / counter
    sorted_by_gpa_students = list_students(path, sort_by='gpa')[::-1]
    all_groups = set([rec['group'] for rec in students_to_analyze])
    return {
        "count": counter,
        "min_gpa": min_gpa,
        "max_gpa": max_gpa,
        "avg_gpa": avg_gpa,
        "groups": {gr: len([rec for rec in students_to_analyze if rec['group'] == gr]) for gr in all_groups},
        "top_5_students": sorted_by_gpa_students[:5]
        }