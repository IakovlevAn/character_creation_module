import math

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number: float) -> None:
    """Проверяет число на положительное значение и возвращает результат."""
    if your_number <= 0:
        return None
    root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


print(message)
calc(25.5)
