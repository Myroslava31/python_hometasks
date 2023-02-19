import math

def square(square_side: int) -> tuple:
    perimeter = square_side * 4
    area = pow(square_side, 2)
    diagonal = square_side * math.sqrt(2)
    result = (perimeter, area, diagonal)
    return result

if __name__ == '__main__':
    print(square(5))
    print(type(square(5)))
