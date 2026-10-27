import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    '''
    Скрипт для перевода файлов в из .json в .сsv и наоборот, а также из .csv в .xlsx формат.
    '''
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv", help='Перевод данных из .json файла в .csv файл')
    p1.add_argument("--in", dest="input", required=True, help='Входной файл в формате .json')
    p1.add_argument("--out", dest="output", required=True, help='Файл для результата в формате .csv')

    p2 = sub.add_parser("csv2json", help='Перевод данных из .csv файла в .json файл')
    p2.add_argument("--in", dest="input", required=True, help='Входной файл в формате .csv')
    p2.add_argument("--out", dest="output", required=True, help='Файл для результата в формате .json')

    p3 = sub.add_parser("csv2xlsx", help='Перевод данных из .csv файла в .xlsx файл')
    p3.add_argument("--in", dest="input", required=True, help='Входной файл в формате .csv')
    p3.add_argument("--out", dest="output", required=True, help='Файл для результата в формате .xlsx')

    args = parser.parse_args()

    if args.command == 'json2csv':
        json_to_csv(args.input, args.output)
    elif args.command == 'csv2json':
        csv_to_json(args.input, args.output)
    elif args.command == 'csv2xlsx':
        csv_to_xlsx(args.input, args.output)
    print(f'Данные из файла {args.input} преобразованы и помещены в файл {args.output}!')
if __name__ == '__main__':
    main()