import os
import pickle

os.chdir("./directory/for/file")
with open ('calculator.txt', 'rb') as file:
    result = file.read()
my_list = pickle.loads(result)
for my_tuple in my_list:
    print(my_tuple)
    if my_tuple[2] == 1:
        first = my_tuple[0] + my_tuple[1]
        print(first)
    elif my_tuple[2] == 2:
        second = my_tuple[0] - my_tuple[1]
        print(second)
    elif my_tuple[2] == 3:
        third = my_tuple[0] * my_tuple[1]
        print(third)

