import math
from abc import ABC, abstractmethod


class Figure(ABC):
    """Abstract class for any figure."""

    @abstractmethod
    def area(self) -> float:
        """Calculate an area of a figure."""
        pass


class Circle(Figure):
    """A circle figure."""

    def __init__(self, radius: float):
        """Initialize a circle."""
        if radius <= 0:
            raise ValueError('Radius must be positive.')
        self.radius = radius

    def area(self) -> float:
        """Calculate an area of a figure."""
        return math.pi * self.radius ** 2


class Triangle(Figure):
    """A triangle figure."""

    def __init__(self, a: float, b: float, c: float):
        """Initialize a triangle."""
        sides = sorted([a, b, c])
        if any(side <= 0 for side in sides):
            raise ValueError('Side must be positive.')
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError('Invalid triangle sides.')
        self.a, self.b, self.c = sides

    def area(self) -> float:
        """Calculate an area of a figure."""
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self) -> bool:
        """If a triangle is right."""
        return math.isclose(self.a ** 2 + self.b ** 2, self.c ** 2, rel_tol=1e-9)
