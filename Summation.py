# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# For example:
# summation(2) -> 3
# 1 + 2
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(n):
    x = 0
    z = 0
    while n > 0:
        x = x + 1
        z += x
        n -= 1
    return z


def summation_2(n):
    total = 0
    for i in range(0, num + 1):
        total = total + i
    return total


def recursive_summation(n):
    if n == 1:
        return 1
    else:
        return n + recursive_summation(n - 1)


num = 22
print(summation(num))
print(summation_2(num))
print(recursive_summation(num))
