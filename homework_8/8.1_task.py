def func_name_decorator(func):
    def inner(number1: int, number2: int):
        return (f'{func.__name__}\n{func(number1, number2)}')
    return inner

@func_name_decorator
def summation(number1: int, number2: int) -> int:
    return number1 + number2


@func_name_decorator
def multiplication(number1: int, number2: int) -> int:
    return number1 * number2

if __name__ == '__main__':
    print(summation(3, 6))
    print(multiplication(3, 6))
