"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""
import string


def solution(s):
    # upper_letters = [x for x in string.ascii_uppercase]
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    new_answer = s
    for idx, letter in enumerate(s):
        if letter in upper_letters:
            new_answer = new_answer.replace(letter, ' ' + letter)
            upper_letters.remove(letter)
    return new_answer


def solution1(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


print(solution('camelCasing'))
print(solution1('camelCasing'))
