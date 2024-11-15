import math


def area(r):
    # Проверка на отрицательное значение радиуса
    if r < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * r * r


def perimeter(r):
    # Проверка на отрицательное значение радиуса
    if r < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * r
