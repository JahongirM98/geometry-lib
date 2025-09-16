from .base import Shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        # Реализацию добавим позже (формула Герона)
        # Пока заглушка, чтобы проект собирался
        return 0.0

    def is_right(self) -> bool:
        # Заглушка, позже добавим точную проверку
        return False
