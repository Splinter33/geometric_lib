def validate_triangle_sides(a, b, c):
    # Проверка корректности сторон треугольника
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Invalid side lengths for a triangle")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Side lengths must be positive")

def area(a, b, c):
    # Проверка корректности сторон треугольника
    validate_triangle_sides(a, b, c)
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def perimeter(a, b, c):
    # Проверка корректности сторон треугольника
    validate_triangle_sides(a, b, c)
    return a + b + c
