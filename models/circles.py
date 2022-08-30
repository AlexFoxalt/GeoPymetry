import math
from typing import Union

from models.base import Processable


class Circle(Processable):
    def __init__(
        self,
        radius: Union[int, float],
        diameter: Union[int, float],
        square: Union[int, float],
        perimeter: Union[int, float],
    ):
        self._radius = radius
        self._diameter = diameter
        self._square = square
        self._perimeter = perimeter

    @property
    def radius(self) -> Union[int, float]:
        if self._radius:
            return self._radius
        elif self._diameter:
            # r = d / 2
            self._radius = self._diameter / 2
            return self._radius
        elif self._square:
            # r=√(S/π)
            self._radius = math.sqrt(self._square / math.pi)
            return self._radius
        elif self._perimeter:
            # r=L/2π
            self._radius = self._perimeter / (2 * math.pi)
        return 0

    @property
    def diameter(self) -> Union[int, float]:
        if self._diameter:
            return self._diameter
        elif self._radius:
            # d = 2r
            self._diameter = self._radius * 2
            return self._diameter
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._radius:
            # S=πr²
            self._square = math.pi * self._radius**2
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._radius:
            # L=2πr
            self._perimeter = 2 * math.pi * self._radius
            return self._perimeter
        return 0
