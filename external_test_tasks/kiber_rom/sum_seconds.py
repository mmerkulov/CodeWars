# '1h 45m,360s,25m,30m 120s,2h 60s'
# посчитать кол-во минут

def get_seconds(value: str) -> int:
    # result: int = int(x.translate({ord('s'): None,
    #                                ord('m'): None,
    #                                ord('h'): None}))
    res = 0
    if 'h' in value:
        res = int(value.replace('h', '')) * 3600
    elif 'm' in value:
        res = int(value.replace('m', '')) * 60
    elif 's' in value:
        res = int(value.replace('s', '')) * 1
    else:
        pass
    return res


row = '1h 45m,360s,25m,30m 120s,2h 60s'
list_values = row.replace(',', ' ').split()
print(list_values)

# print(get_seconds('123h'))

answer = sum(map(get_seconds, list_values))
print(f'total seconds = {answer}', f'total minutes = {answer / 60}')

x = '123h'
result: int = int(x.translate({ord('s'): None,
                               ord('m'): None,
                               ord('h'): None}))

