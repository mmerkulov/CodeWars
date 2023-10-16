"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
import string


def is_pangram(s):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    q = 0
    for i in letters:
        if i in s.lower():
            q += 1
    if q == len(letters):
        return True
    return False


def is_pangram1(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


# print(string.ascii_lowercase)
z = 'The quick brown fox jumps over the lazy dog'
print(is_pangram(s=z))
print(is_pangram1(s=z))
