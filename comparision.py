import random
import time


def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return deterministic_quicksort(less) + [pivot] + deterministic_quicksort(greater)


def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    less = []
    equal = []
    greater = []

    for x in arr:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)


def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr.copy())
    end = time.perf_counter()

    return end - start


sizes = [1000, 2000, 5000]

for n in sizes:

    print("\nInput Size:", n)

    random_array = [random.randint(1, 100000) for _ in range(n)]
    sorted_array = list(range(n))
    reverse_array = list(range(n, 0, -1))
    repeated_array = [random.randint(1, 10) for _ in range(n)]

    datasets = {
        "Random": random_array,
        "Sorted": sorted_array,
        "Reverse Sorted": reverse_array,
        "Repeated": repeated_array
    }

    for name, data in datasets.items():

        try:
            det_time = measure_time(deterministic_quicksort, data)
            det_result = f"{det_time:.6f}s"
        except RecursionError:
            det_result = "Recursion Error"

        rand_time = measure_time(randomized_quicksort, data)

        print(
            f"{name:<15} "
            f"Deterministic: {det_result} "
            f"Randomized: {rand_time:.6f}s"
        )
