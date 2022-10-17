# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.
#
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    s1 = set(a1)
    s2 = set(a2)
    s3 = s1 | s2
    return ''.join(sorted(s3))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))
