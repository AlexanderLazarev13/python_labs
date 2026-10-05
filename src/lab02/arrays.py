# функция №1
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


# функция №2
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


# функция №3
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


# for example1 in [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [1.5, 2, 2.0, -3.1], []]:
#     print(example1)
#     print('->')
#     print(min_max(example1))
#     print('')

# for example2 in [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]:
#     print(example2)
#     print('->')
#     print(unique_sorted(example2))
#     print('')

# for example3 in [[[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]]]:
#     for l in example3:
#         print(l)
#     print('->')
#     print(flatten(example3))
#     print('')
# for l in [[1, 2], '"ab"']:
#         print(l)
# print('->')
# print(flatten([[1, 2], '"ab"']))