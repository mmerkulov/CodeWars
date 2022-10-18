# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function
# that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.
#
# Example: (Input --> Output)
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

def is_isogram(string):
    len_string = len(string.lower())
    len_set = len(set(string.lower()))
    print(list(string), len_string)
    print(set(string), len_set)
    if len_string == 0:
        return True
    elif len_set != len_string:
        return False
    else:
        return True


s = 'Dermatoglyphics'
s = 'aBa'
s = ''
s = 'moOse'
print(is_isogram(s))
