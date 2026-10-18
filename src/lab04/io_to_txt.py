import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Чтение файла через path c кодировкой  "utf-8" по умолчанию
    и преобразование его в одну строку.

    Если файл не найден - FileNotFoundError.
    Если неподходящая кодировка - UnicodeDecodeError.

    Для замены кодировки во время вызова функции нужно передать в параметр encoding другую кодировку.
    Пример: read_text(data.txt, encoding="cp1251")
    '''
    p = Path(path)
    return ' '.join(p.read_text(encoding=encoding).split())


def write_csv(rows: Iterable[Sequence], path: str | Path, 
              header: tuple[str, ...] | None = None) -> None:
    '''
    Создание/перезапись CSV с разделителем "," строк с одинаковой длиной 
    (в противном случае - ValueError).
    Если передан header - запись первой строкой в качестве заголовка.
    '''
    p = Path(path)
    rows = list(rows)

    if rows:
        if len(set(len(r) for r in rows)) != 1: 
            raise ValueError('Строки не одинаковой длины')
        if header is not None and list(set(len(r) for r in rows))[0] != len(header):
            raise ValueError('Строки и заголовок не совпадают по длине')

    ensure_parent_dir(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    '''
    Создание родительской директории, если такие отсутсвуют
    '''
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


# txt = read_text("data/input.txt")
# print(txt)
# write_csv([("word","count"),("test",3)], "data/check.csv")