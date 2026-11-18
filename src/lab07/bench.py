import pandas as pd
import matplotlib.pyplot as plt
import timeit
import random
from src.lab04.io_to_txt import write_csv
from src.lab07.sorting import bubble_sort, selection_sort, insertion_sort, merge_nums, counting_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def main() -> None:
    '''
    Модуль для сравнения разных сортировок и поисков по времени в зависимости от размера данных.
    '''
    random.seed(42)
    rows = []
    for n in [1_000, 10_000, 100_000]:
        array = [random.randint(-1_000_000, 1_000_000) for i in range(n)]
        array_low = [random.randint(-50, 50) for i in range(n)]
        for f in [bubble_sort, selection_sort, insertion_sort, merge_nums]:
            if n <= 10_000:
                t = timeit.timeit(lambda: f(array), number=1)
                rows.append(('sort', n, f.__name__, f'{t:.6f}'))
            elif n == 100_000 and f in [bubble_sort, selection_sort, insertion_sort]:
                rows.append(('sort', n, f.__name__, '> 60c'))
        
        t = timeit.timeit(lambda: f(array), number=1)
        rows.append(('sort', n, 'sorted_on_usual', f'{t:.6f}'))
        t = timeit.timeit(lambda: f(array_low), number=1)
        rows.append(('sort', n, 'sorted_on_low', f'{t:.6f}'))

        lo_low, hi_low = min(array_low), max(array_low)
        t = timeit.timeit(lambda: counting_sort(array_low, lo_low, hi_low), number=1)
        rows.append(('sort', n, 'counting_sort_on_low', f'{t:.6f}'))
        lo, hi = min(array), max(array)
        t = timeit.timeit(lambda: counting_sort(array, lo, hi), number=1)
        rows.append(('sort', n, 'counting_sort_on_usual', f'{t:.6f}'))

    for n in [10_000, 100_000]:
        array = [random.randint(-1_000_000, 1_000_000) for i in range(n)]
        x = random.choice(array)
        for f in [linear_search, binary_search]:
            if f == linear_search:
                t = timeit.timeit(lambda: f(array, x), number=1)
                rows.append(('search', n, f.__name__, f'{t:.6f}'))
            else:
                t1 = timeit.timeit(lambda: sorted(array), number=1)
                arr_sorted = sorted(array)
                t2 = timeit.timeit(lambda: binary_search(arr_sorted, x), number=1)
                t = t1 + t2
                rows.append(('search', n, f.__name__, f'{t:.6f}'))

    for n in [1_000, 10_000]:
        array = [random.randint(-1_000_000, 1_000_000) for i in range(n)]
        x1, x2 = random.sample(array, 2)
        target = x2 - x1
        for f in [two_sum_brute, two_sum_fast]:
            t = timeit.timeit(lambda: f(array, target), number=1)
            rows.append(('two_sum', n, f.__name__, f'{t:.6f}'))

    write_csv(rows, "data/lab07/bench.csv", header=('task', 'n', 'impl', 'seconds'))

    print('Сравнительная таблица замеров по времени различных сортировок и видов поиска')
    col1_len = max([len(x[0]) for x in rows] + [len('task')])
    col2_len = max([len(x) for x in ['1_000', '10_000', '100_000']] + [len('n')])
    col3_len = max([len(x[2]) for x in rows] + [len('impl')])
    col4_len = max([len(x[3]) for x in rows] + [len('seconds')])
    print(f'{'task':<{col1_len}} | {'n':<{col2_len}} | {'impl':<{col3_len}} | {'seconds':<{col4_len}}')
    print('-' * len(f'{'task':<{col1_len}} | {'n':<{col2_len}} | {'impl':<{col3_len}} | {'seconds':<{col4_len}}'))
    for task, n, impl, seconds in rows:
        print(f'{task:<{col1_len}} | {n:<{col2_len}} | {impl:<{col3_len}} | {seconds:<{col4_len}}')

    df = pd.read_csv('data/lab07/bench.csv')
    def clean_time(value):
        if isinstance(value, str) and '>' in value:
            return 60.0
        return float(value)
    df['seconds'] = df['seconds'].apply(clean_time)

    plt.figure(figsize=(10, 6))

    for impl in df['impl'].unique():
        if 'low' in impl: continue
        else:
            subset = df[df['impl'] == impl]
            plt.plot(subset['n'], subset['seconds'], marker='o', label=impl)

    plt.ylim(10 ** -5, 1)
    plt.yscale('log')
    plt.xlabel('n (количество элементов)')
    plt.ylabel('Время (секунды, лог. шкала)')
    plt.title('Время выполнения сортировок в зависимости от n')
    avg_times = {impl: df[df['impl'] == impl]['seconds'].mean() for impl in df['impl'].unique() if 'low' not in impl}

    sorted_impls = sorted(avg_times, key=avg_times.get)

    handles, labels = plt.gca().get_legend_handles_labels()
    label_to_handle = {label: handle for handle, label in zip(handles, labels)}
    sorted_handles = [label_to_handle[impl] for impl in sorted_impls if 'low' not in impl]
    plt.legend(sorted_handles, sorted_impls, title='Алгоритм (от быстрого к медленному)')
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()