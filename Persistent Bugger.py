# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.
#
# For example (Input --> Output):
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

# 6 kyu = 147
from functools import reduce


def persistence(n):
    num_list = list(str(n))
    result = 0
    while len(num_list) > 1:
        new_val = 1
        for x in num_list:
            new_val = new_val * int(x)

        num_list = list(str(new_val))
        result += 1

    return result


# Не моё решение, через функцию reduce и генератор сделан, вместо цикла.
def persistence1(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist


def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0


x = 999
print(persistence(x))
print(persistence1(x))

q1 = 5
q2 = -5
print((paperwork(q1, q2)))
