# Простой декоратор
def my_decorator(my_func):

    def inner():
        print('Befor Hello')
        my_func(value)
        print('After Hello')

    return inner


# Декоратор для функции с параметрами
def my_decorator_with_params(my_func):

    def inner(*args, **kwargs):
        print('Decorator starts...')
        my_func(*args, **kwargs)
        print('Decorator finishes...')

    return inner


@my_decorator
def print_hi():
    print('Hi!')


@my_decorator_with_params
def adder(**nums):
    print(sum(nums.values()))

# Вызов декорированных функций
print_hi()
print(adder(a=2, b=3))
