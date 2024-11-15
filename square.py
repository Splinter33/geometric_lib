def area(a):
    # Проверка положительного значения
    if a <= 0:
        raise ValueError("Side length must be positive")
    
    return a * a


def perimeter(a):
    # Проверка положительного значения
    if a <= 0:
        raise ValueError("Side length must be positive")
    
    return 4 * a
