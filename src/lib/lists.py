def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''
    Функция возвращает минимум и максимум поданного на вход списка nums, 
    содержащий вещественные и/или целые числа, в виде кортежа.
    Если список пуст, возвращается ValueError.
    '''
    if nums == []: raise ValueError('На вход подан пустой список')
    min_n, max_n = nums[0], nums[0]
    for n in nums:
        if n > max_n: max_n = n
        if n < min_n: min_n = n
    return min_n, max_n


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''
    Функция принимает на вход список nums, содержащий вещественные и/или целые числа
    и возвращает отсортированный список уникальных значений (по возрастанию).
    '''
    uniq_nums = list(set(nums))
    for i in range(len(uniq_nums) - 1):
        for j in range(len(uniq_nums) - 1 - i):
            if uniq_nums[j] > uniq_nums[j+1]: 
                uniq_nums[j], uniq_nums[j+1] = uniq_nums[j+1], uniq_nums[j]
    return uniq_nums


def flatten(mat: list[list | tuple]) -> list:
    '''
    Функции на вход подаётся список mat, состоящий из кортежей и/или списков.
    Функция возвращает список, содержащий элементы всех входных списков/кортежей
    по очереди в соответсвии с очередью элементов mat.
    Если встретился элемент, не являющийся кортежем/списком, функция выведет TypeError.
    '''
    if not all([(type(x) is tuple or type(x) is list) for x in mat]): 
        raise TypeError('mat содержит элемент неподоходящего типа')
    row_major = []
    for c in mat: row_major.extend(c)
    return row_major


def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    Функция меняет столбцы и строки матрицы mat местами.
    Если на вход подаётся пустая матрица, она же и возвращается.
    Если матрица содержит строки разной длины, функция выведет ValueError.
    '''
    if mat == []: return []
    if len(set([len(row) for row in mat])) != 1: raise ValueError('"Рваная" матрица')
    num_rows, num_cols = len(mat), len(mat[0])
    transposed_mat = []
    for l in range(num_cols):
        transposed_mat.append([0] * num_rows)

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_mat[j][i] = mat[i][j]

    return transposed_mat


def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Функция по каждой строке матрицы mat вычисляет сумму и возвращает их в виде списка.
    Если длины всех строк матриц не равны, будет возврашено ValueError.
    '''
    if len(set([len(row) for row in mat])) != 1: raise ValueError('"Рваная" матрица')
    mat_f = mat.copy()
    return [sum(row) for row in mat_f]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Функция по каждому столбцу матрицы mat вычисляет сумму и возвращает их в виде списка.
    Если длины всех строк матриц не равны, будет возврашено ValueError.
    '''
    if len(set([len(row) for row in mat])) != 1: raise ValueError('"Рваная" матрица')
    mat_f = mat.copy()
    return [sum([row[i] for row in mat_f]) for i in range(len(mat_f[0]))]


def format_record(rec: tuple[str, str, float]) -> str:
    '''
    Функция преобразует данные из кортежа rec в строку в формате:

    Иванов И.И., гр. BIVT-25, GPA 4.60
    или
    Иванов И., гр. BIVT-25, GPA 4.60

    Формат данных в rec: 
    первый элемент - ФИО/ФИ, 
    второй - группа, 
    третий - gpa в формате float.

    Если данные некоректны:
    пустое имя, пустая группа, неверный формат ввода gpa, 
    неверное количество элементов, gpa не удовлетворяет диапазону от 0 до 5
    
    будет возвращено ValueError.
    '''    
    if rec[0].strip() == '' or rec[1].strip() == '' or (not (type(rec[2]) is float)) or \
        (not (type(rec[0]) is str)) or (not (type(rec[1]) is str)) or \
        (not (0 <= rec[2] <= 5.00)) or (not (type(rec) is tuple)) or len(rec) != 3: 
        raise ValueError('Данные некоректны')
    data = rec.copy()
    initials = data[0].strip().split()[0].capitalize() + ' ' + \
        ''.join([x[0].upper() + '.'  for x in data[0].strip().split()[1:]]) 
    return f'{initials}, гр. {data[1]}, GPA {data[2]:.2f}'