import math

def area(r):
    # Проверка положительного значения радиуса
    if r <= 0:
        raise ValueError("Radius must be positive")
    
    return math.pi * r * r


def perimeter(r):
    # Проверка положительного значения радиуса
    if r <= 0:
        raise ValueError("Radius must be positive")
    
    return 2 * math.pi * r
