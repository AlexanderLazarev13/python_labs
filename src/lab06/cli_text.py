import argparse
from src.lab04.io_to_txt import read_text
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    '''
    Скрипт для вывода содержимого файла по строкам (опционально - нумерованно),
    или для вывода частот слов во входном файле.
    '''
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help='Входной файл')
    cat_parser.add_argument("-n", action="store_true", help="Требуется ли нумерация строк")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help='Входной файл в формате .txt')
    stats_parser.add_argument("--top", type=int, default=5, \
                              help='Количество значений при выводе таблицы с частотами (по умолчанию - 5)')

    args = parser.parse_args()

    if args.command == "cat":
        lines = read_text(args.input).splitlines()
        if args.n:
            for i in range(1, len(lines) + 1):
                print(f'{i}. {lines[i - 1]}')
        else:
            for l in lines:
                print(l)
    elif args.command == "stats":
        full_text = read_text(args.input)
        normalized_text = normalize(full_text)
        words = tokenize(normalized_text)
        unique_words = count_freq(words)
        print(f'Всего слов: {len(words)}')
        print(f'Уникальных слов: {len(unique_words)}')
        
        top_words = top_n(unique_words, n=args.top)
        max_len_word = max(len(w[0]) for w in top_words)
        len_table = max(len('слово'), max_len_word)
        print(f'{'слово':<{len_table}} | частота')
        print(f'{'-' * len_table}-|-------')
        for w, n in top_words:
            print(f'{w:<{len_table}} | {n}')

if __name__ == '__main__':
    main()