import random

left_operand = []
right_operand = []
action_element = []

for i in range(101):
    left_operand.insert(0, (random.randint(0, 100)))
    right_operand.insert(0, (random.randint(0, 100)))
    action_element.insert(0, (random.randint(1, 3)))

my_list = list(zip(left_operand, right_operand, action_element))
print(my_list)
import os
import pickle
os.makedirs('directory/for/file')
os.chdir("./directory/for/file")
if __name__ == '__main__':

    with open ('calculator.txt', 'x+b') as file:
        list_bytes = pickle.dumps(my_list)
        file.write(list_bytes)
