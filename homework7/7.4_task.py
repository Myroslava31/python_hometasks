def my_max_min(list) -> tuple:
    max_list = list[0]
    for number in list:
        if number > max_list:
            max_list = number
    min_list = list[0]
    for number in list:
        if number < min_list:
            min_list = number
    return min_list, max_list


if __name__ == '__main__':
    print(my_max_min([5, 27, 34, 7, 21, 4, 67]))
