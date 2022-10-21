# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.



def find_short(s):
    list_words = s.split()
    new_list_word = sorted(list_words, key=lambda x: len(x))
    return len(new_list_word[0])



text = 'bitcoin take over the world maybe who knows perhaps'
print(find_short(text))
