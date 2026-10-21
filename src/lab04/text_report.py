from src.lib.text import tokenize, normalize, top_n, count_freq
from src.lab04.io_to_txt import read_text, write_csv
from collections import Counter
from pathlib import Path
import argparse

def frequencies_from_text(text: str) -> dict[str, int]:
    from src.lib.text import normalize, tokenize
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def report_total(files: str, res_file: str, encoding: str='utf-8'):
    '''
    Создание отчёта по файлу(ам) в формате:
    слово - количество упоминаний.
    '''
    all_words = []
    for f in files:
        text = read_text(f, encoding=encoding)
        words = tokenize(normalize(text))
        all_words.extend(words)
    lines = sorted_word_counts(Counter(all_words).items())
    write_csv(lines, res_file, header=('word', 'count'))


def report_per_file(files: list[str], res_file: str, encoding: str='utf-8') -> None:
    '''
    Создание отчёта данных по каждому файлу в формате:
    файл - слово - количество упоминаний.
    '''
    lines = []
    for f in files:
        text = read_text(f, encoding=encoding)
        sorted_freq = sorted_word_counts(frequencies_from_text(text))
        file_name = Path(f).name
        for w_c in sorted_freq:
            lines.append([file_name]+list(w_c))
    lines.sort(key=lambda x: (x[0], -x[2], x[1]))
    write_csv(lines, res_file, header=('file', 'word', 'count'))

def main():
    parser = argparse.ArgumentParser(
        prog='Report',
        description='Создание отчёта по количеству строк во входном(ых) файле(ах)'
    )
    parser.add_argument(
        '--in',
        nargs='+',
        help='файлы для обработки',
        dest='files'
    )
    parser.add_argument(
        '--out',
        default='data/report.csv',
        help='файл с отчётом для одного файла',
        dest='res_file'
    )
    parser.add_argument(
        '--encoding',
        default='utf-8',
        help='кодировка',
        dest='encoding'
    )
    parser.add_argument(
        '--per-file',
        default=None,
        help='отчёт по файлам для нескольких файлов',
        dest='per_file'
    )
    parser.add_argument(
        '--total',
        default=None,
        help='общий отчёт по нескольким файлам',
        dest='total'        
    )
    args = parser.parse_args()
    if args.per_file is not None and args.total is not None:
        report_total(args.files, args.total, encoding=args.encoding)
        report_per_file(args.files, args.per_file, encoding=args.encoding)
        print(f'Полный отчёт сохранён в файл: {args.total}')
        print(f'Отчёт по каждому файлу сохранён в файл: {args.per_file}')
        return
    elif ((args.per_file is None and args.total is not None) or \
          (args.per_file is not None and args.total is None) or \
          (args.per_file is None and args.total is None and len(args.files) > 1)):
        parser.error('Для отчёта по нескольким файлам передайте по файлу в аргументы --per-file и --total')
    elif len(args.files) != 1:
        parser.error('Чтобы обработать несколько файло требуется использовать аргументы --per-file и --total')
    else:
        report_total(args.files, args.res_file, encoding=args.encoding)
        if read_text(args.res_file).strip() != 'word,count':
            normalized_text = normalize(read_text(args.files[0], encoding=args.encoding))
            words = tokenize(normalized_text)
            unique_words = count_freq(words)
            top_words = top_n(unique_words)

            print(f'Всего слов: {len(words)}')
            print(f'Уникальных слов: {len(unique_words)}')
            print('Топ-5:')

            max_len_word= max(len(w) for w, n in top_words)
            len_table = max(len('слово'), max_len_word)
            print(f'{'слово':<{len_table}} | частота')
            print(f'{'-' * len_table}-|-------')
            for w, n in top_words:
                print(f'{w:<{len_table}} | {n}')
            return
        else:
            print('Файл пуст')
            return
if __name__ == '__main__':
    main()