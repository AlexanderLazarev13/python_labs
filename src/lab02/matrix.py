<<<<<<< HEAD
# функция №1
def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    Функция меняет столбцы и строки матрицы mat местами.
    Если на вход подаётся пустая матрица, она же и возвращается.
    Если матрица содержит строки разной длины, функция выведет ValueError.
    '''
    if mat == []: return []
    if len(set([len(row) for row in mat])) != 1: return ValueError
    num_rows, num_cols = len(mat), len(mat[0])
    transposed_mat = []
    for l in range(num_cols):
        transposed_mat.append([0] * num_rows)

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_mat[j][i] = mat[i][j]

    return transposed_mat

for example1 in [[[1, 2, 3]], [[1], [2], [3]]]:
    for l1 in example1:
        print(l1)
    print('->')
    tr = transpose(example1)
    for l2 in tr:
        print(l2)
    print('')

print([])
print('->')
print(transpose([]))
print('')

for l in [[1, 2], [3]]:
    print(l)
print('->')
print(transpose([[1, 2], [3]]))

if __name__ == '__main__':
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose([]) == []
    assert transpose([[1, 2], [3]]) == ValueError
    print('Все тесты функции transpose пройдены!')

# функция №2
def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Функция по каждой строке матрицы mat вычисляет сумму и возвращает их в виде списка.
    Если длины всех строк матриц не равны, будет возврашено ValueError.
    '''
    if len(set([len(row) for row in mat])) != 1: return ValueError
    return [sum(row) for row in mat]

for example2 in [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]:
    for l in example2:
        print(l)
    print('->')
    print(row_sums(example2))
    print('')

if __name__ == '__main__':
    assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert row_sums([[-1, 1], [10, -10]]) == [0, 0]
    assert row_sums([[0, 0], [0, 0]]) == [0, 0]
    assert row_sums([[1, 2], [3]]) == ValueError
    print('Все тесты функции row_sums пройдены!')


# функция №3
def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Функция по каждому столбцу матрицы mat вычисляет сумму и возвращает их в виде списка.
    Если длины всех строк матриц не равны, будет возврашено ValueError.
    '''
    if len(set([len(row) for row in mat])) != 1: return ValueError
    return [sum([row[i] for row in mat]) for i in range(len(mat[0]))]

for example3 in [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]:
    for l in example3:
        print(l)
    print('->')
    print(col_sums(example3))
    print('')

if __name__ == '__main__':
    assert col_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
    assert col_sums([[-1, 1], [10, -10]]) == [9, -9]
    assert col_sums([[0, 0], [0, 0]]) == [0, 0]
    assert col_sums([[1, 2], [3]]) == ValueError
=======
# функция №1
def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    Функция меняет столбцы и строки матрицы mat местами.
    Если на вход подаётся пустая матрица, она же и возвращается.
    Если матрица содержит строки разной длины, функция выведет ValueError.
    '''
    if mat == []: return []
    if len(set([len(row) for row in mat])) != 1: return ValueError
    num_rows, num_cols = len(mat), len(mat[0])
    transposed_mat = []
    for l in range(num_cols):
        transposed_mat.append([0] * num_rows)

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_mat[j][i] = mat[i][j]

    return transposed_mat

if __name__ == '__main__':
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose([]) == []
    assert transpose([[1, 2], [3]]) == ValueError
    print('Все тесты функции transpose пройдены!')

# функция №2
def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Функция по каждой строке матрицы mat вычисляет сумму и возвращает их в виде списка.
    Если длины всех строк матриц не равны, будет возврашено ValueError.
    '''
    if len(set([len(row) for row in mat])) != 1: return ValueError
    return [sum(row) for row in mat]

if __name__ == '__main__':
    assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert row_sums([[-1, 1], [10, -10]]) == [0, 0]
    assert row_sums([[0, 0], [0, 0]]) == [0, 0]
    assert row_sums([[1, 2], [3]]) == ValueError
    print('Все тесты функции row_sums пройдены!')


# функция №3
def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Функция по каждому столбцу матрицы mat вычисляет сумму и возвращает их в виде списка.
    Если длины всех строк матриц не равны, будет возврашено ValueError.
    '''
    if len(set([len(row) for row in mat])) != 1: return ValueError
    return [sum([row[i] for row in mat]) for i in range(len(mat[0]))]

if __name__ == '__main__':
    assert col_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
    assert col_sums([[-1, 1], [10, -10]]) == [9, -9]
    assert col_sums([[0, 0], [0, 0]]) == [0, 0]
    assert col_sums([[1, 2], [3]]) == ValueError
>>>>>>> 8ff67be655195176283e690ea39bdfd0ec21461f
    print('Все тесты функции col_sums пройдены!')