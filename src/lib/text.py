def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    Очистка строки text от невидимых управляющих символов (например, \t, \r), 
    замена их на пробелы, а также конвертация повторяющихся пробелов в один.

    Если параметр casefold=True — текст будет преобразован с помощью casefold. 
    Если параметр casefold=False - использование lower().

    Если параметр yo2e=True — заменить все ё/Ё на е/Е.
    '''
    words = text.split()
    new_text = ' '.join(words)

    if casefold == True: new_text = new_text.casefold()
    else: new_text = new_text.lower()

    if yo2e == True:
        new_text = new_text.replace('ё', 'е')
    return new_text

def tokenize(text: str) -> list[str]:
    '''
    Разбиение строку text на "слова" по небуквенно-цифровым разделителям.
    Слова - последовательности символов (буквы/цифры/подчёркивание)
    + дефис внутри слова (например, по-настоящему),
    числа (например, 2025) считаем словами.
    '''
    from re import findall
    return findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    Подсчёт частот элементов из списка tokens в виде словаря слово → количество.
    '''
    unique_elements = sorted(list(set(tokens)))
    return {e: tokens.count(e) for e in unique_elements}

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
    Поиск топ-n по убыванию частоты в словаре freq.
    При равенстве частот — по алфавиту слова.
    '''
    freq_alph = sorted(list(freq.items()), key=lambda x: x[0])
    final_freq = sorted(freq_alph, key=lambda x: x[1], reverse=True)
    return final_freq[:n]

if __name__ == '__main__':
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"
    print('Все тесты функций normalize пройдены!')

    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]
    print('Все тесты функций tokenize пройдены!')

    assert count_freq(["a","b","a","c","b","a"]) == {"a":3,"b":2,"c":1}
    assert top_n({"a":3,"b":2,"c":1}, n=2) == [("a",3), ("b",2)]
    assert count_freq(["bb","aa","bb","aa","cc"]) == {"aa":2,"bb":2,"cc":1}
    assert top_n({"aa":2,"bb":2,"cc":1}, 2) == [("aa",2), ("bb",2)]
    print('Все тесты функций count_freq и top_n пройдены!')