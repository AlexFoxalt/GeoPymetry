import math
from typing import Union

from models.base import Trigonometric, Processable


class Triangle(Trigonometric, Processable):
    """
    Simple composition for all triangles.
    """


class RightTriangle(Triangle):
    def __init__(
        self,
        cathetus_ab: Union[int, float],
        cathetus_ac: Union[int, float],
        hypotenuse_bc: Union[int, float],
        small_r: Union[int, float],
        big_r: Union[int, float],
        height: Union[int, float],
        median: Union[int, float],
        angle_a: Union[int, float],
        angle_b: Union[int, float],
        square: Union[int, float],
        perimeter: Union[int, float],
    ):
        self._cathetus_ab = cathetus_ab
        self._cathetus_ac = cathetus_ac
        self._hypotenuse_bc = hypotenuse_bc
        self._small_r = small_r
        self._big_r = big_r
        self._height = height
        self._median = median
        self._angle_a = angle_a
        self._angle_b = angle_b
        self._square = square
        self._perimeter = perimeter

    @property
    def cathetus_ab(self) -> Union[int, float]:
        if self._cathetus_ab:
            return self._cathetus_ab
        elif self._cathetus_ac and self._hypotenuse_bc:
            # By Pythagorean theorem
            self._cathetus_ab = math.sqrt(
                self._hypotenuse_bc**2 - self._cathetus_ac**2
            )
            return self._cathetus_ab
        elif self._cathetus_ac and self._angle_b:
            # AB = AC * tan(b)
            self._cathetus_ab = self._cathetus_ac * math.tan(self.to_rad(self._angle_b))
            return self._cathetus_ab
        elif self._cathetus_ac and self._angle_a:
            # AB = AC / tan(a)
            self._cathetus_ab = self._cathetus_ac / math.tan(self.to_rad(self._angle_a))
            return self._cathetus_ab
        elif self._hypotenuse_bc and self._angle_b:
            # AB = BC * sin(b)
            self._cathetus_ab = self._hypotenuse_bc * math.sin(
                self.to_rad(self._angle_b)
            )
            return self._cathetus_ab
        elif self._hypotenuse_bc and self._angle_a:
            # AB = BC * cos(a)
            self._cathetus_ab = self._hypotenuse_bc * math.cos(
                self.to_rad(self._angle_a)
            )
            return self._cathetus_ab
        return 0

    @property
    def cathetus_ac(self) -> Union[int, float]:
        if self._cathetus_ac:
            return self._cathetus_ac
        elif self._cathetus_ab and self._hypotenuse_bc:
            # By Pythagorean theorem
            self._cathetus_ac = math.sqrt(
                self._hypotenuse_bc**2 - self._cathetus_ab**2
            )
            return self._cathetus_ac
        elif self._cathetus_ab and self._angle_b:
            # AC = AB / tan(b)
            self._cathetus_ac = self._cathetus_ab / math.tan(self.to_rad(self._angle_b))
            return self._cathetus_ac
        elif self._cathetus_ab and self._angle_a:
            # AC = AB * tan(a)
            self._cathetus_ac = self._cathetus_ab * math.tan(self.to_rad(self._angle_a))
            return self._cathetus_ac
        elif self._hypotenuse_bc and self._angle_b:
            # AC = BC * cos(b)
            self._cathetus_ac = self._hypotenuse_bc * math.cos(
                self.to_rad(self._angle_b)
            )
            return self._cathetus_ac
        elif self._hypotenuse_bc and self._angle_a:
            # AC = BC * sin(a)
            self._cathetus_ac = self._hypotenuse_bc * math.sin(
                self.to_rad(self._angle_a)
            )
            return self._cathetus_ac
        return 0

    @property
    def hypotenuse_bc(self) -> Union[int, float]:
        if self._hypotenuse_bc:
            return self._hypotenuse_bc
        elif self._cathetus_ac and self._cathetus_ab:
            # By Pythagorean theorem
            self._hypotenuse_bc = math.sqrt(
                self._cathetus_ac**2 + self._cathetus_ab**2
            )
            return self._hypotenuse_bc
        elif self._cathetus_ab and self._angle_b:
            # BC = AB / sin(b)
            self._hypotenuse_bc = self._cathetus_ab / math.sin(
                self.to_rad(self._angle_b)
            )
            return self._hypotenuse_bc
        return 0

    @property
    def small_r(self) -> Union[int, float]:
        if self._small_r:
            return self._small_r
        elif self._cathetus_ac and self._cathetus_ab and self._hypotenuse_bc:
            # Radius of inscribed circle = (AB+AC-BC) / 2
            self._small_r = (
                self._cathetus_ac + self._cathetus_ab - self._hypotenuse_bc
            ) / 2
            return self._small_r
        return 0

    @property
    def big_r(self) -> Union[int, float]:
        if self._big_r:
            return self._big_r
        elif self._cathetus_ac and self._cathetus_ab:
            # Radius of circumscribed circle = (√AB² + AC²) / 2
            self._big_r = math.sqrt(self._cathetus_ac**2 + self._cathetus_ab**2) / 2
            return self._big_r
        elif self._hypotenuse_bc:
            # Radius of circumscribed circle = BC / 2
            self._big_r = self._hypotenuse_bc / 2
            return self._big_r
        return 0

    @property
    def height(self) -> Union[int, float]:
        if self._height:
            return self._height
        elif self._cathetus_ac and self._cathetus_ab and self._hypotenuse_bc:
            # H = AB*BC/BC
            self._height = (self._cathetus_ac * self._cathetus_ab) / self._hypotenuse_bc
            return self._height
        return 0

    @property
    def median(self) -> Union[int, float]:
        if self._median:
            return self._median
        elif self._hypotenuse_bc:
            # M = Half of hypotenuse
            self._median = 0.5 * self._hypotenuse_bc
            return self._median
        elif self._cathetus_ac and self._cathetus_ab:
            # M = (√AB² + AC²) / 2
            self._median = (
                math.sqrt(self._cathetus_ac**2 + self._cathetus_ab**2)
            ) / 2
            return self._median
        return 0

    @property
    def angle_a(self) -> Union[int, float]:
        if self._angle_a:
            return self._angle_a
        elif self._angle_b:
            # a = 180 - 90 - b
            self._angle_a = 90 - self._angle_b
            return self._angle_a
        return 0

    @property
    def angle_b(self) -> Union[int, float]:
        if self._angle_b:
            return self._angle_b
        elif self._angle_a:
            # b = 180 - 90 - a
            self._angle_b = 90 - self._angle_a
            return self._angle_b
        elif self._cathetus_ac and self._cathetus_ab:
            # tan(b) = AB / AC
            self._angle_b = self.to_deg(
                math.atan(self._cathetus_ab / self._cathetus_ac)
            )
            return self._angle_b
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._cathetus_ac and self._cathetus_ab and self._hypotenuse_bc:
            # S = √p*(p-AB)*(p-AC)*(p-BC), p = (AC+AB+BC) / 2
            p = (self._cathetus_ac + self._cathetus_ab + self._hypotenuse_bc) / 2
            self._square = math.sqrt(
                p
                * (p - self._cathetus_ac)
                * (p - self._cathetus_ab)
                * (p - self._hypotenuse_bc)
            )
            return self._square
        elif self._cathetus_ac and self._cathetus_ab:
            # S = AB * AC / 2
            self._square = (self._cathetus_ac * self._cathetus_ab) / 2
            return self._square
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._cathetus_ac and self._cathetus_ab and self._hypotenuse_bc:
            return self._cathetus_ac + self._cathetus_ab + self._hypotenuse_bc
        return 0


class EquilateralTriangle(Triangle):
    def __init__(
        self,
        side: Union[int, float],
        small_r: Union[int, float],
        big_r: Union[int, float],
        height: Union[int, float],
        square: Union[int, float],
        perimeter: Union[int, float],
    ):
        self._side = side
        self._small_r = small_r
        self._big_r = big_r
        self._height = height
        self._square = square
        self._perimeter = perimeter

    @property
    def side(self) -> Union[int, float]:
        if self._side:
            return self._side
        elif self._perimeter:
            # a = P/3
            self._side = self._perimeter / 3
            return self._side
        elif self._small_r:
            # a = r * (2√3)
            self._side = self._small_r * (2 * math.sqrt(3))
        elif self._big_r:
            # a = R * √3
            self._side = self._big_r * math.sqrt(3)
        elif self._square:
            # a = √(S*4/√3)
            self._side = math.sqrt((self._square * 4 / math.sqrt(3)))
        elif self._height:
            # a = h*2/√3
            self._side = self._height * 2 / math.sqrt(3)
        return 0

    @property
    def small_r(self) -> Union[int, float]:
        if self._small_r:
            return self._small_r
        elif self._side:
            # r = a/(2√3)
            self._small_r = self._side / (2 * math.sqrt(3))
        return 0

    @property
    def big_r(self) -> Union[int, float]:
        if self._big_r:
            return self._big_r
        elif self._side:
            # R = a/√3
            self._big_r = self._side / math.sqrt(3)
        return 0

    @property
    def height(self) -> Union[int, float]:
        if self._height:
            return self._height
        elif self._side:
            # h = (√3 a)/2
            self._height = (math.sqrt(3) * self._side) / 2
            return self._height
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._side:
            # S = (√3 * a^2)/4
            self._square = (math.sqrt(3) * self._side**2) / 4
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._side:
            # P = 3 * a
            self._perimeter = 3 * self._side
            return self._perimeter
        return 0


class ArbitraryTriangle(Triangle):
    def __init__(
        self,
        side_ab: Union[int, float],
        side_ac: Union[int, float],
        side_bc: Union[int, float],
        square: Union[int, float],
        small_r: Union[int, float],
        big_r: Union[int, float],
        height: Union[int, float],
        perimeter: Union[int, float],
        median: Union[int, float],
        angle_a: Union[int, float],
        angle_b: Union[int, float],
        angle_c: Union[int, float],
    ):
        self._side_ab = side_ab
        self._side_ac = side_ac
        self._side_bc = side_bc
        self._square = square

        self._small_r = small_r
        self._big_r = big_r
        self._height = height
        self._perimeter = perimeter

        self._median = median
        self._angle_a = angle_a
        self._angle_b = angle_b
        self._angle_c = angle_c

    @property
    def side_ab(self) -> Union[int, float]:
        if self._side_ab:
            return self._side_ab
        elif self._side_bc and self._angle_c and self._angle_a:
            # AB/sin(c) = BC/sin(a) = AC/sin(b)
            bc = self._side_bc / math.sin(self.to_rad(self._angle_a))
            self._side_ab = bc * math.sin(self.to_rad(self._angle_c))
            return self._side_ab
        elif self._side_ac and self._angle_c and self._angle_b:
            # AB/sin(c) = BC/sin(a) = AC/sin(b)
            ac = self._side_ac / math.sin(self.to_rad(self._angle_b))
            self._side_ab = ac * math.sin(self.to_rad(self._angle_c))
            return self._side_ab
        elif self._side_bc and self._side_ac and self._angle_c:
            # Cosine theorem
            self._side_ab = math.sqrt(
                self._side_bc**2
                + self._side_ac**2
                - (
                    2
                    * self._side_bc
                    * self._side_ac
                    * math.cos(self.to_rad(self._angle_c))
                )
            )
            return self._side_ab
        return 0

    @property
    def side_ac(self) -> Union[int, float]:
        if self._side_ac:
            return self._side_ac
        elif self._side_ab and self._angle_b and self._angle_c:
            # AB/sin(c) = BC/sin(a) = AC/sin(b)
            ab = self._side_ab / math.sin(self.to_rad(self._angle_c))
            self._side_ac = ab * math.sin(self.to_rad(self._angle_b))
            return self._side_ac
        elif self._side_bc and self._angle_b and self._angle_a:
            # AB/sin(c) = BC/sin(a) = AC/sin(b)
            bc = self._side_bc / math.sin(self.to_rad(self._angle_a))
            self._side_ac = bc * math.sin(self.to_rad(self._angle_b))
            return self._side_ac
        elif self._side_bc and self._side_ab and self._angle_b:
            # Cosine theorem
            self._side_ac = math.sqrt(
                self._side_bc**2
                + self._side_ab**2
                - (
                    2
                    * self._side_bc
                    * self._side_ab
                    * math.cos(self.to_rad(self._angle_b))
                )
            )
            return self._side_ac
        return 0

    @property
    def side_bc(self) -> Union[int, float]:
        if self._side_bc:
            return self._side_bc
        elif self._side_ac and self._angle_a and self._angle_b:
            # AB/sin(c) = BC/sin(a) = AC/sin(b)
            ac = self._side_ac / math.sin(self.to_rad(self._angle_b))
            self._side_bc = ac * math.sin(self.to_rad(self._angle_a))
            return self._side_bc
        elif self._side_ab and self._angle_a and self._angle_c:
            # AB/sin(c) = BC/sin(a) = AC/sin(b)
            ab = self._side_ab / math.sin(self.to_rad(self._angle_c))
            self._side_bc = ab * math.sin(self.to_rad(self._angle_a))
            return self._side_bc
        elif self._side_ab and self._side_ac and self._angle_a:
            # Cosine theorem
            self._side_bc = math.sqrt(
                self._side_ab**2
                + self._side_ac**2
                - (
                    2
                    * self._side_ab
                    * self._side_ac
                    * math.cos(self.to_rad(self._angle_a))
                )
            )
            return self._side_bc
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._side_ab and self._side_bc and self._side_ac:
            # S = √p*(p-AB)*(p-AC)*(p-BC), p = (AC+AB+BC) / 2
            p = (self._side_ab + self._side_bc + self._side_ac) / 2
            self._square = math.sqrt(
                p * (p - self._side_ab) * (p - self._side_bc) * (p - self._side_ac)
            )
            return self._square
        elif self._side_ac and self._height:
            # S = side * height / 2
            self._square = self._side_ac * self._height / 2
            return self._square
        return 0

    @property
    def small_r(self) -> Union[int, float]:
        if self._small_r:
            return self._small_r
        elif self._side_ab and self._side_bc and self._side_ac:
            # r = √(((p-a)(p-b)(p-c))/p)
            p = (self._side_ab + self._side_bc + self._side_ac) / 2
            self._small_r = math.sqrt(
                ((p - self._side_ab) * (p - self._side_bc) * (p - self._side_ac)) / p
            )
            return self._small_r
        return 0

    @property
    def big_r(self) -> Union[int, float]:
        if self._big_r:
            return self._big_r
        elif self._side_ab and self._side_bc and self._side_ac:
            # R = abc / (4√(p(p-a)(p-b)(p-c)))
            p = (self._side_ab + self._side_bc + self._side_ac) / 2
            abc = self._side_ab * self._side_bc * self._side_ac
            self._big_r = abc / (
                4
                * math.sqrt(
                    p * (p - self._side_ab) * (p - self._side_bc) * (p - self._side_ac)
                )
            )
            return self._big_r
        return 0

    @property
    def height(self) -> Union[int, float]:
        if self._height:
            return self._height
        elif self._side_ab and self._side_bc and self._side_ac:
            # h = (2/AC) * √(p * (p-a) * (p-b) * (p-c))
            # p = half perimeter
            p = (self._side_ab + self._side_bc + self._side_ac) / 2
            self._height = (2 / self._side_ac) * math.sqrt(
                p * (p - self._side_ab) * (p - self._side_bc) * (p - self._side_ac)
            )
            return self._height
        elif self._angle_a and self._side_ab:
            # h = AB * sin(a)
            self._height = self._side_ab * math.sin(self.to_rad(self._angle_a))
            return self._height
        elif self._angle_c and self._side_bc:
            # h = BC * sin(c)
            self._height = self._side_bc * math.sin(self.to_rad(self._angle_c))
            return self._height
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._side_ab and self._side_bc and self._side_ac:
            # P = AB + BC + AC
            self._perimeter = self._side_ab + self._side_bc + self._side_ac
            return self._perimeter
        return 0

    @property
    def median(self) -> Union[int, float]:
        if self._median:
            return self._median
        elif self._side_ab and self._side_bc and self._side_ac:
            # m = √(2 * AB² + 2BC² - AC²) / 2
            self._median = (
                math.sqrt(
                    2 * self._side_ab**2 + 2 * self._side_bc**2 - self._side_ac**2
                )
                / 2
            )
            return self._median
        return 0

    @property
    def angle_a(self) -> Union[int, float]:
        if self._angle_a:
            return self._angle_a
        elif self._side_ab and self._side_bc and self._side_ac:
            # cos(a)=(AB² + AC² - BC²) / (2 * AB * AC)
            cos = (self._side_ab**2 + self._side_ac**2 - self._side_bc**2) / (
                2 * self._side_ab * self._side_ac
            )
            self._angle_a = self.to_deg(math.acos(cos))
            return self._angle_a
        elif self._angle_b and self._angle_c:
            # a = 180 - b - c
            self._angle_a = 180 - self._angle_b - self._angle_c
            return self._angle_a
        return 0

    @property
    def angle_b(self) -> Union[int, float]:
        if self._angle_b:
            return self._angle_b
        elif self._side_ab and self._side_bc and self._side_ac:
            # cos(b)=(BC² + AB² - AC²) / (2 * BC * AB)
            cos = (self._side_bc**2 + self._side_ab**2 - self._side_ac**2) / (
                2 * self._side_bc * self._side_ab
            )
            self._angle_b = self.to_deg(math.acos(cos))
            return self._angle_b
        elif self._angle_a and self._angle_c:
            # b = 180 - a - c
            self._angle_b = 180 - self._angle_a - self._angle_c
            return self._angle_b
        return 0

    @property
    def angle_c(self) -> Union[int, float]:
        if self._angle_c:
            return self._angle_c
        elif self._side_ab and self._side_bc and self._side_ac:
            # cos(c)=(BC² + AC² - AB²) / (2 * BC * AC)
            cos = (self._side_bc**2 + self._side_ac**2 - self._side_ab**2) / (
                2 * self._side_bc * self._side_ac
            )
            self._angle_c = self.to_deg(math.acos(cos))
            return self._angle_c
        elif self._angle_a and self._angle_b:
            # c = 180 - a - b
            self._angle_c = 180 - self._angle_a - self._angle_b
            return self._angle_c
        return 0
