def linear_search(nums, x) -> int:
    '''
    Поиск индекса первого вхождения, при отсутствии - "-1".
    Линейный поиск.
    '''
    for i, v in enumerate(nums):
        if v == x: return i
    return -1

def binary_search(sorted_nums, x) -> int:
    '''
    Поиск индекса первого вхождения, при отсутствии - "-1".
    Подаваемый список должен быть отсортирован по возрастанию.
    На неотсортированном списке результат не определён.
    Бинарный поиск.
    '''
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        if sorted_nums[mid] == x: return mid
        elif sorted_nums[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    '''
    Поиск пары индексов (i, j), i < j, таких что
    nums[i] + nums[j] == target, при отсутствии - None.
    Двойной цикл.
    '''
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target: return i, j
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    '''
    Поиск пары индексов (i, j), i < j, таких что
    nums[i] + nums[j] == target, при отсутствии - None.
    Цикл через словарь.
    '''
    seen = dict()
    for i, x in enumerate(nums):
        t_x = target - x
        if t_x in seen:
            return seen[t_x], i
        seen[x] = i
    return None