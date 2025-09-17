from __future__ import annotations
from math import isclose, sqrt
from .base import Shape

class Triangle(Shape):
    """Треугольник по трём сторонам с валидацией."""
    __slots__ = ("a", "b", "c")

    def __init__(self, a: float, b: float, c: float):
        for x in (a, b, c):
            if x <= 0:
                raise ValueError("Sides must be positive numbers")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Triangle inequality violated")
        self.a, self.b, self.c = float(a), float(b), float(c)

    def area(self) -> float:
        """Площадь по формуле Герона."""
        s = (self.a + self.b + self.c) / 2.0
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self, *, rel_tol: float = 1e-9, abs_tol: float = 1e-9) -> bool:
        """Проверка прямоугольности с допуском по float."""
        a, b, c = sorted((self.a, self.b, self.c))
        return isclose(c * c, a * a + b * b, rel_tol=rel_tol, abs_tol=abs_tol)
