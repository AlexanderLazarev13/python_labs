def bubble_sort(nums) -> list:
    '''
    Сортировка "пузырьком" списка без изменения исходного.
    '''
    sorted_nums = list(nums)
    for i in range(len(sorted_nums)):
        swapped = False
        for j in range(len(sorted_nums) - i - 1):
            if sorted_nums[j] > sorted_nums[j + 1]:
                sorted_nums[j], sorted_nums[j + 1] = sorted_nums[j + 1], sorted_nums[j]
                swapped = True
        if not swapped:
            break
    return sorted_nums

def insertion_sort(nums) -> list:
    '''
    Сортировка вставками списка без изменения исходного.
    '''
    sorted_nums = list(nums)
    for i in range(1, len(sorted_nums)):
        v = sorted_nums[i]
        j = i - 1
        while j >= 0 and sorted_nums[j] > v:
            sorted_nums[j + 1] = sorted_nums[j]
            j -= 1
        sorted_nums[j + 1] = v
    return sorted_nums

def selection_sort(nums) -> list:
    '''
    Сортировка выбором списка без изменения исходного.
    '''
    sorted_nums = list(nums)
    for i in range(len(sorted_nums) - 1):
        i1 = i
        for j in range(i + 1, len(sorted_nums)):
            if sorted_nums[j] < sorted_nums[i1]:
                i1 = j
        sorted_nums[i], sorted_nums[i1] = sorted_nums[i1], sorted_nums[i]
    return sorted_nums

def merge_nums(nums: list) -> list:
    '''
    Сортировка отрезками списка без изменения исходного.
    '''
    sorted_nums = list(nums)
    length = 1
    while length < len(sorted_nums):
        for i in range(0, len(sorted_nums), 2 * length):
            left, right = sorted_nums[i: i + length], sorted_nums[i + length:i + 2 * length]
            merge = []
            l_seg, r_seg = 0, 0
            while l_seg < len(left) and r_seg < len(right):
                if left[l_seg] <= right[r_seg]:
                    merge.append(left[l_seg])
                    l_seg += 1
                else:
                    merge.append(right[r_seg])
                    r_seg += 1

            merge.extend(left[l_seg:])
            merge.extend(right[r_seg:])
            sorted_nums[i: i + len(merge)] = merge
        length *= 2
    return sorted_nums

def counting_sort(nums: list, lo: int, hi: int) -> list:
    '''
    Сортировка подсчётом для целых чисел в диапозоне от lo до hi
    без изменения исходного списка.
    '''
    nums_copy = list(nums)
    counter = [0] * (hi - lo + 1)
    for x in nums_copy:
        counter[x - lo] += 1
    for i in range(1, hi - lo + 1):
        counter[i] += counter[i - 1]
    sorted_nums = [0] * len(nums_copy)
    for y in reversed(nums_copy):
        counter[y - lo] -= 1
        sorted_nums[counter[y - lo]] = y
    return sorted_nums