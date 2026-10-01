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

if __name__ == '__main__':
    assert(normalize("ПрИвЕт\nМИр\t")) == "привет мир"
    assert(normalize("ёжик, Ёлка", yo2e=True)) == "ежик, елка"
    assert(normalize("Hello\r\nWorld")) == "hello world"
    assert(normalize("  двойные   пробелы  ")) == "двойные пробелы"
    print('Все тесты пройдены')