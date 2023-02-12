import re

def remove_numbers(file):
    with open(file, 'r') as file:
        result = file.read()

    return re.sub((r'\d'), '', result)

if __name__ == '__main__':
    print(remove_numbers('text.txt'))
