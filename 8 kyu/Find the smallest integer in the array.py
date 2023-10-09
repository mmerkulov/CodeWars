"""
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
"""


def find_smallest_int(arr: list):
    arr.sort()
    return arr[0]


def find_smallest_int1(arr: list):
    return min(arr)


x = [78, 56, 232, 12, 11, 43]
# x.sort()
# print(x)
# sorted(x)
# print(x)
print(find_smallest_int(x))
