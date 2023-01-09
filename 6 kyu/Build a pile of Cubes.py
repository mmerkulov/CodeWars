# Your task is to construct a building which will be a pile of n cubes.The cube at the bottom will have a volume of
# n ^ 3, the cube above will have volume of(n - 1) ^ 3 and so on until the top which will have a volume of
# 1 ^ 3.
#
# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to
# build?
#
# The parameter of the function findNb(find_nb, find - nb, findNb, ...) will be an integer m and you have to return the
# integer n such as n ^ 3 + (n−1) ^ 3 + ... + 1 ^ 3 = m. if such a n exists or -1 if there is no such n.
#
# Examples:
# findNb(1071225) --> 45
# findNb(91716553919377) --> -1


def find_nb(m):
    answer = 1
    while m > 0:
        answer_pow = pow(answer, 3)
        m -= answer_pow
        answer += 1
        # print(f'answer = {answer}', f'answer_pow = {answer_pow}')

        if m < 0:
            #print('На выход!!!')
            return -1

    return answer - 1

def find_nb_recursive(m, answer):
    if m < 0:
        return -1
    else:
        answer_pow = pow(answer, 3)
        m -= answer_pow
        answer += 1

# x = pow(3, 3)
# print(x)
# y = pow(27, 1 / 3)
# print(y)

z = 135440716410000
print(find_nb(z))
#
# 1 ** 3 = 1
# 36 - 1 = 35
# 2 ** 3 = 8
# 35 - 8 = 27
# 3 ** 3 = 27
# 27 - 27 = 0

# 1^3=1
# 2^3=8
# 3^3=27
#    =36
