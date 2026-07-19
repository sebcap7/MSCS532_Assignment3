import random

# Deterministic Quicksort
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return deterministic_quicksort(less) + [pivot] + deterministic_quicksort(greater)


# Randomized Quicksort
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

    return (
        randomized_quicksort(less)
        + equal
        + randomized_quicksort(greater)
    )


# Testing
if __name__ == "__main__":
    test = [5, 2, 8, 1, 9, 3]

    print("Original:", test)
    print("Deterministic:", deterministic_quicksort(test))
    print("Randomized:", randomized_quicksort(test))

    print("\nEdge Case Tests")

    print("Empty Array:", randomized_quicksort([]))
    print("Single Element:", randomized_quicksort([10]))
    print("Sorted Array:", randomized_quicksort([1, 2, 3, 4, 5]))
    print("Reverse Sorted Array:", randomized_quicksort([5, 4, 3, 2, 1]))
    print("Repeated Elements:", randomized_quicksort([4, 4, 4, 2, 2, 1, 1]))
