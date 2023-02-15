from typing import Callable

random_int = [2, 94, 34, 7, 111]
random_float = [4.6, 7.1, 0.8, 37.4, 62.9]
random_str = ['book', 'table', 'coffee', 'phone']
new_filter_list =[]

def some_even_func(item):
    if item > 4:
        return item
    else:
        pass
def some_str_func(item):
    if item.find('0'):
        return item
def filter_function(callback: Callable, iterable):
    for item in iterable:
        new_filter_list.append(some_even_func(item))
    for item in iterable:
        new_filter_list.append(some_str_func(item))
    return

if __name__ == '__main__':
    filter_function(some_even_func, random_int)
    filter_function(some_even_func, random_float)
    filter_function(some_str_func, random_str)
    print(new_filter_list)
