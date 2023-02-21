from typing import Callable
from typing import List

random_int = [2, 94, 34, 7, 111]
random_float = [4.6, 7.1, 0.8, 37.4, 62.9]
random_str = ['book', 'table', 'coffee', 'phone']


def some_number_func(item: (int, float)) -> (int, float):
    if item > 4:
        return item
def some_str_func(item: str) -> str:
    if item.startswith('t'):
        return item

def filter_function(callback: Callable, iterable: (List[int], List[float], List[str])) -> list:
    filter_list = []
    for item in iterable:
        if callback(item):
            filter_list.append(item)
    return filter_list

if __name__ == '__main__':
    print(filter_function(some_number_func, random_int))
    print(filter_function(some_number_func, random_float))
    print(filter_function(some_str_func, random_str))

