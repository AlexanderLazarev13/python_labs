import openpyxl
import csv
from pathlib import Path
from src.lab04.io_to_txt import ensure_parent_dir

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    import openpyxl
    import csv
    from pathlib import Path
    from src.lab04.io_to_txt import ensure_parent_dir
    '''
    Конвертация CSV в XLSX.
    Первая строка CSV — заголовок.
    Колонки — автоширина по длине текста (не менее 8 символов).
    '''
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Sheet1'
    try:
        with open(csv_path, encoding='utf-8') as f:
            sample = f.read()
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            f.seek(0)
            csv_file = list(csv.reader(f, dialect=dialect))
        if Path(xlsx_path).suffix != '.xlsx': raise ValueError('Невозможно перевести данные в отличный от .xlsx файл')
        if len(csv_file) < 2: raise ValueError('Файл пуст, или в файле отсутствует заголовок, или в файле присутствует только ')
        for line in csv_file:
            ws.append(line)
        for column in ws.columns:
            len_column = max([len(str(cell.value)) for cell in column] + [8])
            ws.column_dimensions[column[0].column_letter].width = len_column
        ensure_parent_dir(xlsx_path)
        wb.save(xlsx_path)

    except FileNotFoundError:
        raise FileNotFoundError('Файл не найден.')
    except UnicodeDecodeError:
        raise ValueError('Кодировка не соответствует "utf-8".')
    except csv.Error:
        raise ValueError('Невозможно обработать не .csv файл.')

if __name__ == '__main__':
    csv_to_xlsx('data/samples/cities.csv', 'data/out/cities.xlsx')
    csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')

    with open('data/samples/cities.csv', newline='', encoding='utf-8') as f:
        len_csv_file = len(list(csv.DictReader(f)))
    
    cities_xlsx_out = openpyxl.load_workbook('data/out/cities.xlsx')
    sheet1 = cities_xlsx_out["Sheet1"]
    len_xlsx_cities = sheet1.max_row - 1 # -заголовок
    assert len_csv_file == len_xlsx_cities
    print(f'Тест №1 конвертации CSV -> XLSX пройден, .csv = {len_csv_file} строк(и); .xlsx = {len_xlsx_cities} записей(и) + заголовок')

    with open('data/samples/people.csv', newline='', encoding='utf-8') as f:
        len_csv_file = len(list(csv.DictReader(f)))
    people_xlsx_out = openpyxl.load_workbook('data/out/cities.xlsx')
    sheet2 = people_xlsx_out["Sheet1"]
    len_xlsx_people = sheet2.max_row - 1 # -заголовок
    assert len_csv_file == len_xlsx_people
    print(f'Тест №2 конвертации CSV -> XLSX пройден, .csv = {len_csv_file} строк(и); .xlsx = {len_xlsx_people} записей(и) + заголовок')
    