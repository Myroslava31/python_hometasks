def is_prime(number: int(2-1000)) -> bool:
    for numeric in range(2, (int (number /2) + 1)):
        if number % numeric == 0:
            return False
    else:
        return True

if __name__ == '__main__':
    print(is_prime(29))

