import sys
import os

src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, src_path)

from lib.text import *
text = sys.stdin.read()
if text.strip() == '':
    raise ValueError('Невозможно преобразовать пустую строку')

normalized_text = normalize(text)
words = tokenize(normalized_text)
unique_words = count_freq(words)
top_words = top_n(unique_words)
table_const = 1 # константа для вывода таблицей

print(f'Всего слов: {len(words)}')
print(f'Уникальных слов: {len(unique_words)}')
print('Топ-5:')

if table_const:
    max_len_word= max(len(w) for w, n in top_words)
    len_table = max(len('слово'), max_len_word)
    print(f'{'слово':<{len_table}} | частота')
    print(f'{'-' * len_table}-|-------')
    for w, n in top_words:
        print(f'{w:<{len_table}} | {n}')