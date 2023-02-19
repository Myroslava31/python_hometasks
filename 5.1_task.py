import random

my_list = []
for _ in range(100):
    my_list.append(((random.randint(0, 100)), (random.randint(0, 100)), (random.randint(1, 3))))
print(my_list)
import os
import pickle
os.makedirs('directory/for/file')
os.chdir("./directory/for/file")
if __name__ == '__main__':

    with open ('calculator.txt', 'x+b') as file:
        list_bytes = pickle.dumps(my_list)
        file.write(list_bytes)
