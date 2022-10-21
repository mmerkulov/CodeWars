def find_average(numbers):
    return int(sum([x for x in numbers]) / len(numbers))


n = [1, 2, 3]
print(find_average(n))


