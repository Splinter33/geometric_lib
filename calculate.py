import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {"perimeter-circle": 1, "area-circle": 1,
         "perimeter-square": 1, "area-square": 1,
         "perimeter-triangle": 3, "area-triangle": 3}

def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}")

    # Проверка на количество аргументов
    required_size = sizes.get(f"{func}-{fig}", 1)
    if len(size) != required_size:
        raise ValueError(f"Invalid number of arguments for {func} of {fig}")

    # Проверка на отрицательные значения (для круга и квадрата)
    if fig in ['circle', 'square'] and any(s <= 0 for s in size):
        raise ValueError(f"Size must be positive for {fig}")

    # Проверка на корректные размеры треугольника
    if fig == 'triangle':
        a, b, c = size
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(f"Invalid side lengths for a triangle")

    # Вычисление результата
    try:
        result = eval(f'{fig}.{func}(*{size})')
    except Exception as e:
        raise ValueError(f"Calculation error: {e}")

    return result
