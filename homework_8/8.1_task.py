def func_name_decorator(name: str):
    """DEC doc"""

    def middle_wraper(func):
        """Middle wraper"""

        def inner(number1: int, number2: int):
            return f'__{name}__\n{func(number1, number2)}'

        return inner

    return middle_wraper


@func_name_decorator('summation')
def summ(number1: int, number2: int) -> int:
    return number1 + number2


@func_name_decorator('multiplication')
def multi(number1: int, number2: int) -> int:
    return number1 * number2

if __name__ == '__main__':
    print(summ(3, 6))
    print(multi(3, 6))
