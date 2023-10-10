"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text: str):
    start = 0
    answer = []
    for idx, val in enumerate(list(text)):
        print(idx, val)
        if val == ' ':
            print(f'idx => {idx}', f'val => {val}')
            split_words = str(text[start:idx])[::-1]
            print(f'split_words => {split_words}')
            if split_words != '':
                answer.append(split_words)
            answer.append(' ')
            print(f'answer => {answer}')
            start = idx + 1
            print(f'start => {start}')
    # last word add
    answer.append(str(text[start:])[::-1])
    return ''.join(answer)


def reverse_words1(str):
    # go for it
    newStr = []
    for i in str.split(' '):
        newStr.append(i[::-1])
    return ' '.join(newStr)


t = 'double  spaced  words'
# print(reverse_words(t))
# print(reverse_words1(t))
print(t.split(' '))
print(' '.join(['double', '', 'spaced', '', 'words']))
