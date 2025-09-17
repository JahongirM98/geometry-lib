from math import pi
from .base import Shape

class Circle(Shape):
    __slots__ = ("radius",)

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = float(radius)

    def area(self) -> float:
        return pi * self.radius * self.radius
