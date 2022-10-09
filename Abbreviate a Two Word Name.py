# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Example:
# Sam Harris => S.H
# patrick feeney => P.F

def abbreviate_name(full_name):
    list_words = full_name.split()
    print(list_words)
    short_name = ''
    for x in list_words:
        short_name += x[0:1] + '.'
    return short_name[:3].upper()


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


name = 'Sam Harris'

print(abbreviate_name(name))
print(abbrevName(name))
