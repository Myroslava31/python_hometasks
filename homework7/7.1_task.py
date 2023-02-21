import sys

def my_print(*args) -> str:
    result = ''.join(args)
    sys.stdout.write(result)
    return result


if __name__ == '__main__':
    my_print('This is my print function')

