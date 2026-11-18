import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_nums, counting_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
def check_sorting(fn, trials=100):
    '''
    Проверка сортировок на рандомных массивах.
    '''
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f'{fn.__name__} ошиблась на {nums}: {result}'
        assert nums == original, f'{fn.__name__} изменила исходный список'

def check_search(fn, trials=100) -> None:
    '''
    Проверка поиска индекса на рандомных массивах.
    '''
    if fn == 'linear_search':
        for _ in range(trials):
            n = random.randint(0, 50)
            nums = [random.randint(-100, 100) for _ in range(n)]
            original = list(nums)
            result = fn(nums)
            assert result == nums.index(), f'{fn.__name__} ошиблась на {nums}: {result}'
            assert nums == original, f'{fn.__name__} изменила исходный список'
    elif fn == 'binary_search':
        for _ in range(trials):
            n = random.randint(0, 50)
            nums = sorted([random.randint(-100, 100) for _ in range(n)])
            original = list(nums)
            result = fn(nums)
            assert result == nums.index(), f'{fn.__name__} ошиблась на {nums}: {result}'
            assert nums == original, f'{fn.__name__} изменила исходный список'

def check_two_sum(trials=100):
    '''
    Проверка на правильность поиска пары индексов (i, j), i < j
    для функций two_sum_brute и two_sum_fast, при отсутсвии - None.
    '''
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = sorted([random.randint(-100, 100) for _ in range(n)])
        target = random.randint(5, 15)
        res_def, res_fast = two_sum_brute(nums, target), two_sum_fast(nums, target)
        if res_def is None or res_fast is None:
            continue
        else:
            assert nums[res_def[0]] + nums[res_def[1]] == target, f'Функция "two_sum_brute" ошиблась {nums}: {nums[res_def[0]] + nums[res_def[1]]} отличается от {target}'
            assert nums[res_fast[0]] + nums[res_fast[1]] == target, f'Функции "two_sum_fast" ошиблась на {nums}: {nums[res_fast[0]] + nums[res_fast[1]]} отличается от {target}'

if __name__ == "__main__":
    random.seed(42)
  
    for fn in (bubble_sort, insertion_sort, selection_sort, merge_nums):
        n_sorting = random.randint(50, 100)
        check_sorting(fn, n_sorting)
        print(f'ОК! Функция "{fn.__name__}" прошла все {n_sorting} проверок(ку).')

    for fn in (linear_search, binary_search):
        n_search = random.randint(50, 100)
        check_search(fn, n_search)
        print(f'ОК! Функция "{fn.__name__}" прошла все {n_search} проверок(ку).')

    n_twosum = random.randint(50, 100)
    check_two_sum(n_twosum)
    print(f'ОК! Функции "two_sum_brute" и "two_sum_fast" прошли все {n_twosum} проверок(ку).')