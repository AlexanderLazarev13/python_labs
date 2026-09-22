# функция №1
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''
    Функция возвращает минимум и максимум поданного на вход списка nums, 
    содержащий вещественные и/или целые числа, в виде кортежа.
    Если список пуст, возвращается ValueError.
    '''
    if nums == []: return ValueError
    return min(nums), max(nums)

if __name__ == '__main__':
    assert min_max([3, -1, 5, 5, 0]) == (-1, 5)
    assert min_max([42]) == (42, 42)
    assert min_max([-5, -2, -9]) == (-9, -2)
    assert min_max([]) == ValueError
    assert min_max([1.5, 2, 2.0, -3.1]) == (-3.1, 2)
    print('Все тесты функции min_max пройдены!')

# функция №2
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''
    Функция принимает на вход список nums, содержащий вещественные и/или целые числа
    и возвращает отсортированный список уникальных значений (по возрастанию).
    '''
    return sorted(list(set(nums)))

if __name__ == '__main__':
    assert unique_sorted([3, 1, 2, 1, 3]) == [1, 2, 3]
    assert unique_sorted([]) == []
    assert unique_sorted([-1, -1, 0, 2, 2]) == [-1, 0, 2]
    assert unique_sorted([1.0, 1, 2.5, 2.5, 0]) == [0, 1.0, 2.5]
    print('Все тесты функции unique_sorted пройдены!')

# функция №3
def flatten(mat: list[list | tuple]) -> list:
    '''
    Функции на вход подаётся список mat, состоящий из кортежей и/или списков.
    Функция возвращает список, содержащий элементы всех входных списков/кортежей
    по очереди в соответсвии с очередью элементов mat.
    Если встретился элемент, не являющийся кортежем/списком, функция выведет TypeError.
    '''
    if not all([(type(x) is tuple or type(x) is list) for x in mat]): return TypeError
    row_major = []
    for c in mat: row_major.extend(c)
    return row_major

if __name__ == '__main__':
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([[1, 2], (3, 4, 5)]) == [1, 2, 3, 4, 5]
    assert flatten([[1], [], [2, 3]]) == [1, 2, 3]
    assert flatten([[1, 2], "ab"]) == TypeError
    print('Все тесты функции flatten пройдены!')