from typing import Callable

random_int = [2, 94, 34, 7, 111]
random_float = [4.6, 7.1, 0.8, 37.4, 62.9]
random_str = ['book', 'table', 'coffee', 'phone']

def some_sum_func(item: (int, float, str)) -> (int, float, str):
    return item + item

def map_function(callback: Callable, iterable: list) -> list:
    map_list = []
    for item in iterable:
        if callback(item):
            map_list.append(some_sum_func(item))
    return map_list

if __name__ == '__main__':
    print(map_function(some_sum_func, random_int))
    print(map_function(some_sum_func, random_float))
    print(map_function(some_sum_func, random_str))
