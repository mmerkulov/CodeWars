# '1h 45m,360s,25m,30m 120s,2h 60s'
# посчитать кол-во минут

class CustomTimeHour:
    @staticmethod
    def get_second(value: int) -> int:
        return value * 3600


class CustomTimeMinute:
    @staticmethod
    def get_second(value: int) -> int:
        return value * 60


class CustomTimeSecond:
    @staticmethod
    def get_second(value: int) -> int:
        return value * 1


def get_seconds(value: str) -> int:
    # result: int = int(x.translate({ord('s'): None,
    #                                ord('m'): None,
    #                                ord('h'): None}))
    res = 0
    if 'h' in value:
        # res = int(value.replace('h', '')) * 3600
        res = CustomTimeHour.get_second(int(value.replace('h', '')))
    elif 'm' in value:
        # res = int(value.replace('m', '')) * 60
        res = CustomTimeMinute.get_second(int(value.replace('m', '')))
    elif 's' in value:
        res = int(value.replace('s', '')) * 1
        # TODO ну по сути тоже вызывается класс для расчёта секунд
    else:
        pass
    return res


## Тестовые данные
row = '1h 45m,360s,25m,30m 120s,2h 60s'
list_values = row.replace(',', ' ').split()
print(f'Результат разбивки строки на элементы => {list_values}')

answer = sum(map(get_seconds, list_values))
print(f'total seconds = {answer}', f'total minutes = {answer / 60}')

### тестил translate()
x = '123h'
result: int = int(x.translate({ord('s'): None,
                               ord('m'): None,
                               ord('h'): None}))
