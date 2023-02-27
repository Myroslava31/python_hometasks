def my_gen(first:int, last: int):
    for number in range(first, last +1):
        if number % 2 == 0:
            yield number ** 2


if __name__ == '__main__':
    generator = my_gen(0, 1000)
    for result in generator:
        print(result)
