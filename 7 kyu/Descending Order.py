# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits
# in descending order. Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: `42145` Output: `54421`
# Input: `145263` Output: `654321`
# Input: `123456789` Output: `987654321`

def descending_order(num):
    l = list(str(num))
    q = []
    for i in range(0, len(l)):
        q.append(int(l[i]))
    q.sort(reverse=True)
    print(type(q))
    str_l = [str(x) for x in q]
    return ''.join(str_l)


def Descending_Order2(num):
    return int("".join(sorted(str(num), reverse=True)))


q = 42145
z = descending_order(q)
print(z)
