def my_all(list) -> bool:
    result = []
    for number in list:
        if number != 0:
            result = True
        elif number == 0:
            result = False
            break
    return result

if __name__ == '__main__':
    print(my_all([5, 98, 54, 4, 0, 9, 73, -453]))
