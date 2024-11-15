def area(a):
    # Проверка на отрицательное значение
    if a < 0:
        raise ValueError("Side length must be non-negative")
    
    return a * a


def perimeter(a):
    # Проверка на отрицательное значение
    if a < 0:
        raise ValueError("Side length must be non-negative")
    
    return 4 * a
