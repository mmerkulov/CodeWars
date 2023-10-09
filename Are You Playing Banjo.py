# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# Example:
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.

def do_you_playing_bonjo(name=''):
    return name + ' plays banjo' if name.lstrip()[0:1].lower() == 'r' else name + ' does not play banjo'


name = 'Roman'
name = 'Mikhail'
name = 'Rouse'
print(do_you_playing_bonjo(name))
