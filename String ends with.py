# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument
# (also a string).
#
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    return True if string[-len(ending):] == ending or len(ending) == 0 else False

x = 'abcde'
y = ''
print(solution(x, y))
