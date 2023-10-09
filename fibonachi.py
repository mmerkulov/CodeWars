class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


def fib_recursion(x: int = 0) -> int:
    if x < 0:
        raise Exception('Cannot be less than 0.')
    if 0 <= x <= 2:
        return 1
    return fib_recursion(x - 1) + fib_recursion(x - 2)


def fib_get_list(x: int = 0) -> list:
    if 0 <= x <= 2:
        return [1]

    result = [1, 1]

    for i in range(1, x - 1):
        new_x = result[i] + result[i - 1]
        result.append(new_x)
    return result


z = 10

print(f'z => {fib_recursion(z)}')

# print(fib_get_list(z))
#
# fibonacci_of = Fibonacci()
# print(f'x=> {fibonacci_of(z)}')
# print([fibonacci_of(n) for n in range(z)])
