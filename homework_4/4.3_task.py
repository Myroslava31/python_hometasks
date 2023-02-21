my_string = 'name=Amanda=sssss&age=32&&salary=1500&currency=euro'
better_string = my_string.replace('sssss&', '')
good_string = better_string.replace('&&', '=')
perfect_string = good_string.replace('&', '=')
print(perfect_string)
filtered_string = perfect_string.split('=')
print(filtered_string)
new_dict = {filtered_string[item]: filtered_string[item + 1] for item in range(0, len(filtered_string), 2)}
print(new_dict)
