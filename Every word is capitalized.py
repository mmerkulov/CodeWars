text = 'Hello, my name is Mikhail Merkulov and i wanna wort at Tinkoff'

text = text.split()
text = [x.capitalize() for x in text]
text = ' '.join(text)
print(text)

LENGTH = 7


def create_fib_sequence(length=LENGTH):
    lst = [0, 1]
    for i in range(1, length - 1):
        lst.append(lst[i - 1] + lst[i])
    return lst


print(create_fib_sequence(length=7))

tpl = (1, 2, 3, [1, 2, 3], 5)
print(tpl)
tpl[3].append(4)
print(tpl)
# tpl[4].append(55)   # так нельзя делать, потому что кортеж не изменяемый тип данных
print(tpl)