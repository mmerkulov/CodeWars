# Бинарный поиск элемента в отсортированном массиве


def binary_search(array, target):
    start = 0
    end = len(array)

    while start <= end:
        mid = (end + start) // 2
        if array[mid] == target:
            return f'Мы нашли! idx = {mid} and val = {array[mid]}'

        if array[mid] < target:
            start = mid + 1
        if array[mid] > target:
            end = mid - 1


def recursive_binary_search(array, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == target:
        return mid

    if array[mid] < target:
        return recursive_binary_search(array, mid + 1, end, target)
    else:
        return recursive_binary_search(array, start, end - 1, target)


nums = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
target = 18
print(binary_search(nums, target))
print(recursive_binary_search(nums, 0, len(nums), target))
