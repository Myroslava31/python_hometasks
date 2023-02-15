random_list_str = ['book', 'table', 'coffee', 'phone']


new_filter = filter(lambda sum_str: random_list_str.startswith('b'), random_list_str)
new_list = list(new_filter)
print(new_list)
