# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers.
# 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def method_arr(nums):
    c = 0
    s = 0
    if len(nums) < 1:
        return []

    for x in nums:
        if x > 0:
            c += 1
        elif x < 0:
            s += x
        else:
            continue

    if not s and not c:
        return [0, 0]

    return [c, s]


def count_positives_sum_negatives(nums):
    pos = sum(1 for x in nums if x > 0)
    neg = sum(x for x in nums if x < 0)
    return [pos, neg] if len(nums) else []


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# nums = [0, 0]
# nums = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
# nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
nums = [1]
print(method_arr(nums))
print(count_positives_sum_negatives(nums))
