from typing import Callable

random_int = [2, 94, 34, 7, 111]
random_float = [4.6, 7.1, 0.8, 37.4, 62.9]
random_str = ['book', 'table', 'coffee', 'phone']
new_map_list =[]
def some_sum_func(item: (int, float, str)) -> (int, float, str):
    return item + item

def map_function(callback: Callable, iterable: list) -> (int, float, str):
    for item in iterable:
        new_map_list.append(some_sum_func(item))
    return

if __name__ == '__main__':
    map_function(some_sum_func, random_int)
    map_function(some_sum_func, random_float)
    map_function(some_sum_func, random_str)
    print(new_map_list)
