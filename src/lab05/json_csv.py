import json
from pathlib import Path
import csv
from src.lab04.io_to_txt import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    import json
    from pathlib import Path
    import csv
    from src.lab04.io_to_txt import ensure_parent_dir
    '''
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8.
    '''
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
        if not(type(json_file) == list): raise ValueError('Функция не поддерживает формат данных отличный от списка.')
        if not(all([type(d) == dict for d in json_file])): raise ValueError('Список должен содержать только словари.')
        if len(json_file) == 0: raise ValueError('Входной файл пуст')
        if Path(csv_path).suffix != '.csv': raise ValueError('Невозможно перевести данные в отличный от .csv файл')

        fieldnames = set()
        for dict_r in json_file:
            fieldnames.update(dict_r.keys())
        fieldnames = sorted(list(fieldnames))
        ensure_parent_dir(csv_path)
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            csv_file = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            csv_file.writeheader()
            csv_file.writerows(json_file)
    except FileNotFoundError:
        raise FileNotFoundError('Файл не найден.')
    except UnicodeDecodeError:
        raise ValueError('Кодировка не соответствует "utf-8".')
    except json.JSONDecodeError:
        raise ValueError('Невозможно обработать не .json файл')

def csv_to_json(csv_path: str, json_path: str) -> None:
    import json
    from pathlib import Path
    import csv
    from src.lab04.io_to_txt import ensure_parent_dir
    '''
    Преобразует CSV в JSON (список словарей) c заголовком.
    '''
    try:
        with open(csv_path, newline='', encoding='utf-8') as f:
            sample = f.read()
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            f.seek(0)
            csv_file = list(csv.DictReader(f, dialect=dialect))
        if not sniffer.has_header(sample): raise ValueError('В файле отсутсвует заголовок')
        if len(csv_file) == 0: raise ValueError('Входной файл пуст')
        if Path(json_path).suffix != '.json': raise ValueError('Невозможно перевести данные в отличный от .json файл')
    
        ensure_parent_dir(json_path)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(csv_file, f, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError('Файл не найден.')
    except UnicodeDecodeError:
        raise ValueError('Кодировка не соответствует "utf-8".')
    except csv.Error:
        raise ValueError('Невозможно обработать не .csv файл.')

if __name__ == '__main__':
    # json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
    csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')

    with open('data/samples/people.json', 'r', encoding='utf-8') as f:
        len_json_file = len(json.load(f))
    with open('data/out/people_from_json.csv', newline='', encoding='utf-8') as f:
        len_csv_res = len(list(csv.DictReader(f)))

    with open('data/samples/people.csv', newline='', encoding='utf-8') as f:
        len_csv_file = len(list(csv.DictReader(f)))
    with open('data/out/people_from_csv.json', 'r', encoding='utf-8') as f:
        len_json_res = len(json.load(f))

    assert len_json_file == len_csv_res
    print(f'Тест конвертации JSON -> CSV пройден, .json = {len_json_file} записей(и); .csv = {len_csv_res} строк(и)')
    assert len_csv_file == len_json_res
    print(f'Тест конвертации CSV -> JSON пройден, .csv = {len_csv_file} строк(и); .json = {len_json_res} записей(и)')