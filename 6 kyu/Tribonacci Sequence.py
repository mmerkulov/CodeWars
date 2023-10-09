"""
Well met with Fibonacci bigger brother, AKA Tribonacci.
As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]

But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)
"""


def tribonacci(signature: list, n: int = 0) -> list:
    if n == 0:
        return []
    if n == 1:
        return signature[:1]
    if n == 2:
        return signature[:2]

    result = signature

    for i in range(2, n - 1):
        new_x = result[i] + result[i - 1] + result[i - 2]
        result.append(new_x)
    return result


# Не моё
def tribonacci1(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


# s = [1, 1, 1]
# s = [0, 0, 1]
# s = [0, 1, 1]
# s = [1, 0, 0]
# s = [0, 0, 0]
# s = [1, 1, 0]
# s = [0.5, 0.5, 0.5]
# s = [300, 200, 100]
s = [124, 22, 184]
print(tribonacci(signature=s, n=3))
print(tribonacci1(signature=s, n=3))
