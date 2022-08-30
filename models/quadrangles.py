import math
from typing import Union

from models.base import Trigonometric, Processable


class Quadrangle(Trigonometric, Processable):
    """
    Simple composition for all quadrangles to provide required methods.
    """


class Rectangle(Quadrangle):
    def __init__(
        self,
        side_ab: Union[int, float],
        side_bc: Union[int, float],
        angle_x: Union[int, float],
        angle_y: Union[int, float],
        diag: Union[int, float],
        square: Union[int, float],
        perimeter: Union[int, float],
    ):
        self._side_ab = side_ab
        self._side_bc = side_bc
        self._angle_x = angle_x
        self._angle_y = angle_y
        self._diag = diag
        self._square = square
        self._perimeter = perimeter

    @property
    def side_ab(self) -> Union[int, float]:
        if self._side_ab:
            return self._side_ab
        elif self._side_bc and self._square:
            self._side_ab = self._square / self._side_bc
            return self._side_ab
        elif self._side_bc and self._diag:
            # AB² = d² - BC²
            self._side_ab = math.sqrt(self._diag**2 - self._side_bc**2)
            return self._side_ab
        elif self._perimeter and self._diag:
            # AB=(P-√(8d²-P² ))/4
            self._side_ab = (
                self._perimeter - math.sqrt(8 * self._diag**2 - self._perimeter**2)
            ) / 4
            return self._side_ab
        elif self._diag and self._angle_y:
            # AB = d * sin(y/2)
            self._side_ab = self._diag * math.sin(self.to_rad(self._angle_y / 2))
            return self._side_ab
        elif self._perimeter and self._side_bc:
            # AB = (P - 2BC) / 2
            self._side_ab = (self._perimeter - (self._side_bc * 2)) / 2
            return self._side_ab
        elif self._square and self._side_bc:
            # AB = S / BC
            self._side_ab = self._square / self._side_bc
            return self._side_ab
        return 0

    @property
    def side_bc(self) -> Union[int, float]:
        if self._side_bc:
            return self._side_bc
        elif self._side_ab and self._square:
            self._side_bc = self._square / self._side_ab
            return self._side_bc
        elif self._side_ab and self._diag:
            # BC² = d² - AB²
            self._side_bc = math.sqrt(self._diag**2 - self._side_ab**2)
            return self._side_bc
        elif self._perimeter and self._diag:
            # BC=(P+√(8d²-P² ))/4
            self._side_bc = (
                self._perimeter + math.sqrt(8 * self._diag**2 - self._perimeter**2)
            ) / 4
            return self._side_bc
        elif self._diag and self._angle_y:
            # BC = d * cos(y/2)
            self._side_ab = self._diag * math.cos(self.to_rad(self._angle_y / 2))
            return self._side_bc
        elif self._perimeter and self._side_ab:
            # BC = (P - 2AC) / 2
            self._side_bc = (self._perimeter - (self._side_ab * 2)) / 2
            return self._side_bc
        elif self._square and self._side_ab:
            # BC = S / AB
            self._side_bc = self._square / self._side_ab
            return self._side_bc
        return 0

    @property
    def angle_x(self) -> Union[int, float]:
        if self._angle_x:
            return self._angle_x
        elif self._side_ab and self._side_bc:
            # y=arc-tan(BC/AB) * 2
            self._angle_x = (self.to_deg(math.atan(self._side_bc / self._side_ab))) * 2
            return self._angle_x
        elif self._angle_y:
            self._angle_x = 180 - self._angle_y
            return self.angle_x
        return 0

    @property
    def angle_y(self) -> Union[int, float]:
        if self._angle_y:
            return self._angle_y
        elif self._side_ab and self._side_bc:
            # x=arc-tan(AB/BC) * 2
            self._angle_y = (self.to_deg(math.atan(self._side_ab / self._side_bc))) * 2
            return self._angle_y
        elif self._angle_x:
            self._angle_y = 180 - self._angle_x
            return self._angle_y
        return 0

    @property
    def diag(self) -> Union[int, float]:
        if self._diag:
            return self._diag
        elif self._side_ab and self._side_bc:
            # d_1=d_2=√(a² + b²)
            self._diag = math.sqrt(self._side_ab**2 + self._side_bc**2)
            return self._diag
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._side_ab and self._side_bc:
            # S = ab * bc
            self._square = self._side_ab * self._side_bc
            return self._square
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._side_ab and self._side_bc:
            # P = 2AB + 2BC
            self._perimeter = self._side_ab * 2 + self._side_bc * 2
            return self._perimeter
        return 0


class Parallelogram(Quadrangle):
    def __init__(
        self,
        side_ab: Union[int, float],
        side_bc: Union[int, float],
        height: Union[int, float],
        angle_x: Union[int, float],
        angle_y: Union[int, float],
        angle_a: Union[int, float],
        angle_b: Union[int, float],
        diag_1: Union[int, float],
        diag_2: Union[int, float],
        square: Union[int, float],
        perimeter: Union[int, float],
    ):
        self._side_ab = side_ab
        self._side_bc = side_bc
        self._height = height
        self._angle_x = angle_x
        self._angle_y = angle_y
        self._angle_a = angle_a
        self._angle_b = angle_b
        self._diag_1 = diag_1
        self._diag_2 = diag_2
        self._square = square
        self._perimeter = perimeter

    @property
    def side_ab(self) -> Union[int, float]:
        if self._side_ab:
            return self._side_ab
        elif self._diag_1 and self._diag_2 and self._angle_y:
            # AB = 0.5 * √(d_1² + d_2² - (2*d_1*d_2) * cos(y))
            self._side_ab = (
                math.sqrt(
                    self._diag_1**2
                    + self._diag_2**2
                    - (2 * self._diag_1 * self._diag_2)
                    * math.cos(self.to_rad(self._angle_y))
                )
                * 0.5
            )
            return self._side_ab
        return 0

    @property
    def side_bc(self) -> Union[int, float]:
        if self._side_bc:
            return self._side_bc
        elif self._diag_1 and self._diag_2 and self._angle_y:
            # BC = 0.5 * √(d_1² + d_2² + (2*d_1*d_2) * cos(y))
            self._side_bc = 0.5 * math.sqrt(
                self._diag_1**2
                + self._diag_2**2
                + (2 * self._diag_1 * self._diag_2)
                * math.cos(self.to_rad(self._angle_y))
            )
            return self._side_bc
        return 0

    @property
    def height(self) -> Union[int, float]:
        if self._height:
            return self._height
        elif self._side_ab and self._angle_a:
            # h = AB * sin(α)
            self._height = self._side_ab * math.sin(self.to_rad(self._angle_a))
            return self._height
        return 0

    @property
    def angle_x(self) -> Union[int, float]:
        if self._angle_x:
            return self._angle_x
        elif self._angle_y:
            self._angle_x = 180 - self._angle_y
            return self._angle_x
        elif self._diag_1 and self._diag_2 and self._side_bc:
            # cos(y) = (d_1²+d_2²-4*BC²)/(2*d_1*d_2)
            self._angle_x = self.to_deg(
                math.acos(
                    ((self._diag_1**2) + (self._diag_2**2) - 4 * self._side_bc**2)
                    / (2 * self._diag_1 * self._diag_2)
                )
            )
            return self._angle_x
        return 0

    @property
    def angle_y(self) -> Union[int, float]:
        if self._angle_y:
            return self._angle_y
        elif self._angle_x:
            self._angle_y = 180 - self._angle_x
            return self._angle_y
        elif self._diag_1 and self._diag_2 and self._side_ab:
            # cos(y) = (d_1²+d_2²-4*AB²)/(2*d_1*d_2)
            self._angle_y = self.to_deg(
                math.acos(
                    ((self._diag_1**2) + (self._diag_2**2) - 4 * self._side_ab**2)
                    / (2 * self._diag_1 * self._diag_2)
                )
            )
            return self._angle_y
        return 0

    @property
    def angle_a(self) -> Union[int, float]:
        if self._angle_a:
            return self._angle_a
        elif self._angle_b:
            self._angle_a = 180 - self._angle_b
            return self._angle_a
        elif self._side_ab and self._side_bc and self._diag_1:
            # Transformation from the cosine theorem
            # cos(α)=(AB² + BC² - d_1²) / (2 * AB * BC)
            cos_a = (self._side_ab**2 + self._side_bc**2 - self._diag_1**2) / (
                2 * self._side_ab * self._side_bc
            )
            self._angle_a = self.to_deg(math.acos(cos_a))
            return self._angle_a
        elif self._side_ab and self._height:
            # sin(α)= h / a
            self._angle_a = self.to_deg(math.asin(self._height / self._side_ab))
            return self._angle_a
        return 0

    @property
    def angle_b(self) -> Union[int, float]:
        if self._angle_b:
            return self._angle_b
        elif self._angle_a:
            self._angle_b = 180 - self._angle_a
            return self._angle_b
        return 0

    @property
    def diag_1(self) -> Union[int, float]:
        if self._diag_1:
            return self._diag_1
        elif self._side_ab and self._side_bc and self._angle_b:
            # d_1=√(AB² + BC² - 2*AB*BC * cos(b))
            self._diag_1 = math.sqrt(
                (
                    self._side_ab**2
                    + self._side_bc**2
                    - (2 * self._side_ab * self._side_bc)
                    * math.cos(self.to_rad(self._angle_b))
                )
            )
            return self.diag_1
        return 0

    @property
    def diag_2(self) -> Union[int, float]:
        if self._diag_2:
            return self._diag_2
        elif self._side_ab and self._side_bc and self._angle_b:
            # d_2 =√(AB² + BC²+ 2*AB*BC * cos(b))
            self._diag_2 = math.sqrt(
                (
                    self._side_ab**2
                    + self._side_bc**2
                    + (2 * self._side_ab * self._side_bc)
                    * math.cos(self.to_rad(self._angle_b))
                )
            )
            return self._diag_2
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._side_bc and self._height:
            # BC * h
            self._square = self._side_bc * self._height
            return self._square
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._side_ab and self._side_bc:
            self._perimeter = self._side_ab * 2 + self._side_bc * 2
            return self._perimeter
        return 0


class Trapezoid(Quadrangle):
    def __init__(
        self,
        side_ab: Union[int, float],
        side_bc: Union[int, float],
        side_cd: Union[int, float],
        side_da: Union[int, float],
        angle_a: Union[int, float],
        angle_b: Union[int, float],
        angle_c: Union[int, float],
        angle_d: Union[int, float],
        diag_1: Union[int, float],
        diag_2: Union[int, float],
        height: Union[int, float],
        median: Union[int, float],
        square: Union[int, float],
        perimeter: Union[int, float],
    ):
        self._side_ab = side_ab
        self._side_bc = side_bc
        self._side_cd = side_cd
        self._side_da = side_da
        self._angle_a = angle_a
        self._angle_b = angle_b
        self._angle_c = angle_c
        self._angle_d = angle_d
        self._diag_1 = diag_1
        self._diag_2 = diag_2
        self._height = height
        self._median = median
        self._square = square
        self._perimeter = perimeter

    @property
    def side_ab(self) -> Union[int, float]:
        if self._side_ab:
            return self._side_ab
        elif self._height and self._side_bc and self._side_da:
            # c² = a² + b²
            small_side = abs((self._side_bc - self._side_da) / 2)
            self._side_ab = math.sqrt(self._height**2 + small_side**2)
            return self._side_ab
        return 0

    @property
    def side_bc(self) -> Union[int, float]:
        if self._side_bc:
            return self._side_bc
        return 0

    @property
    def side_cd(self) -> Union[int, float]:
        if self._side_cd:
            return self._side_cd
        elif self._side_ab:
            # If trapezium is isosceles, sides are equal
            self._side_cd = self._side_ab
            return self._side_cd
        return 0

    @property
    def side_da(self) -> Union[int, float]:
        if self._side_da:
            return self._side_da
        return 0

    @property
    def angle_a(self) -> Union[int, float]:
        if self._angle_a:
            return self._angle_a
        # elif self._side_ab and self._side_da and self._diag_1:
        #     cos = (self._side_ab**2 + self._side_da**2 - self._diag_1**2) / (2*self._side_ab*self._side_da)
        #     self._angle_a = self.to_deg(math.acos(cos))
        #     return self._angle_a
        elif self._height and self._side_ab:
            # a = 90° - acos(h / AB) * (180 / Pi)
            cos_a = math.acos(self._height / self._side_ab)
            self._angle_a = 90 - cos_a * (180 / math.pi)
            return self._angle_a
        return 0

    @property
    def angle_b(self) -> Union[int, float]:
        if self._angle_b:
            return self._angle_b
        elif self._angle_a:
            # The sum of the angles on the side of a trapezoid is 180
            self._angle_b = 180 - self._angle_a
            return self._angle_b
        return 0

    @property
    def angle_c(self) -> Union[int, float]:
        if self._angle_c:
            return self._angle_c
        elif self._angle_d:
            # The sum of the angles on the side of a trapezoid is 180
            self._angle_c = 180 - self._angle_d
            return self._angle_c
        return 0

    @property
    def angle_d(self) -> Union[int, float]:
        if self._angle_d:
            return self._angle_d
        # elif self._side_da and self._side_cd and self._diag_2:
        #     cos = (self._side_da**2 + self._side_cd**2 - self._diag_2**2) / (2*self._side_da*self._side_cd)
        #     self._angle_d = self.to_deg(math.acos(cos))
        #     return self._angle_d
        elif self._height and self._side_cd:
            # d = 90° - acos(h / CD) * (180 / Pi)
            cos_d = math.acos(self._height / self._side_cd)
            self._angle_d = 90 - cos_d * (180 / math.pi)
            return self._angle_d
        return 0

    @property
    def diag_2(self) -> Union[int, float]:
        if self._diag_2:
            return self._diag_2
        elif self._side_ab and self._side_bc and self._side_cd and self._side_da:
            # d_2 = √(CD² + (DA*BC) - DA(CD²-AB²) / (DA-BC))
            self._diag_2 = math.sqrt(
                self._side_cd**2
                + self._side_da * self._side_bc
                - self._side_da
                * (self._side_cd**2 - self._side_ab**2)
                / (self._side_da - self._side_bc)
            )
            return self._diag_2
        elif self._height and self._median:
            # d² = h² + m² | If trapezium is isosceles
            self._diag_2 = math.sqrt(self._height**2 + self._median**2)
            return self._diag_2
        return 0

    @property
    def diag_1(self) -> Union[int, float]:
        if self._diag_1:
            return self._diag_1
        elif self._side_ab and self._side_bc and self._side_cd and self._side_da:
            # d_1 = √(AB² + (DA*BC) - DA(AB²-CD²) / (DA-BC))
            self._diag_1 = math.sqrt(
                self._side_ab**2
                + self._side_da * self._side_bc
                - self._side_da
                * (self._side_ab**2 - self._side_cd**2)
                / (self._side_da - self._side_bc)
            )
            return self._diag_1
        elif self._height and self._median:
            # d² = h² + m² | If trapezium is isosceles
            self._diag_1 = math.sqrt(self._height**2 + self._median**2)
            return self._diag_1
        return 0

    @property
    def height(self) -> Union[int, float]:
        if self._height:
            return self._height
        elif self._side_ab and self._side_bc and self._side_cd and self._side_da:
            # h = √(AB² - (((DA-BC)² + AB² - CD²) / (2(DA - BC)))²)
            self._height = math.sqrt(
                self._side_ab**2
                - (
                    (
                        (self._side_da - self._side_bc) ** 2
                        + self._side_ab**2
                        - self._side_cd**2
                    )
                    / (2 * (self._side_da - self._side_bc))
                )
                ** 2
            )
            return self._height
        return 0

    @property
    def median(self) -> Union[int, float]:
        if self._median:
            return self._median
        elif self._side_bc and self._side_da:
            # m = (BC+DA) / 2
            self._median = (self._side_bc + self._side_da) / 2
            return self._median
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._median and self._height:
            # S = hm
            self._square = self._median * self._height
            return self._square
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._side_ab and self._side_bc and self._side_cd and self._side_da:
            self._perimeter = (
                self._side_ab + self._side_bc + self._side_cd + self._side_da
            )
            return self._perimeter
        return 0


class Rhombus(Quadrangle):
    def __init__(
        self,
        side: Union[int, float],
        height: Union[int, float],
        angle_a: Union[int, float],
        angle_b: Union[int, float],
        diag_1: Union[int, float],
        diag_2: Union[int, float],
        small_r: Union[int, float],
        square: Union[int, float],
        perimeter: Union[int, float],
    ):
        self._side = side
        self._height = height
        self._angle_a = angle_a
        self._angle_b = angle_b
        self._diag_1 = diag_1
        self._diag_2 = diag_2
        self._small_r = small_r
        self._square = square
        self._perimeter = perimeter

    @property
    def side(self) -> Union[int, float]:
        if self._side:
            return self._side
        elif self._square and self._angle_a:
            # side = √(S / sin(α))
            self._side = math.sqrt(self._square / math.sin(self.to_rad(self._angle_a)))
            return self._side
        elif self._perimeter:
            # P = side*4 => side = P/4
            self._side = self._perimeter / 4
            return self._side
        elif self._diag_1 and self._diag_2:
            # side = √(d_1²/4 + d_2²/4)
            self._side = math.sqrt(self._diag_1**2 / 4 + self._diag_2**2 / 4)
            return self._side
        elif self._small_r and self._angle_a:
            # side = 2r / sin(α)
            self._side = 2 * self._small_r / math.sin(self.to_rad(self._angle_a))
            return self._side
        return 0

    @property
    def height(self) -> Union[int, float]:
        if self._height:
            return self._height
        elif self._square and self._angle_a:
            # h = √(S * sin(α))
            self._height = math.sqrt(
                self._square * math.sin(self.to_rad(self._angle_a))
            )
            return self._height
        elif self._square and self._side:
            # h=S/side
            self._height = self._square / self._side
            return self._height
        elif self._small_r:
            # h=2r
            self._height = 2 * self._small_r
            return self._height
        return 0

    @property
    def angle_a(self) -> Union[int, float]:
        if self._angle_a:
            return self._angle_a
        elif self._angle_b:
            self._angle_a = 180 - self._angle_b
            return self._angle_a
        elif self._diag_1 and self._diag_2:
            # sin(a) = (2*d_1*d_2) / (d_1²+d_2²)
            self._angle_a = self.to_deg(
                math.asin(
                    (
                        2
                        * self._diag_1
                        * self._diag_2
                        / (self._diag_1**2 + self._diag_2**2)
                    )
                )
            )
            return self._angle_a
        elif self._side and self._diag_1:
            # cos(a) = (d_1²/2side²) - 1
            division = self._diag_1**2 / (2 * self._side**2)
            self._angle_a = self.to_deg(math.acos(division - 1))
            return self._angle_a
        elif self._square and self._diag_1:
            # tan(a) = (2S / d_1²) * 2
            self._angle_a = (
                self.to_deg(math.atan(2 * self._square / self._diag_1**2))
            ) * 2
            return self._angle_a
        elif self._small_r and self._side:
            # sin(α)=2r/a
            self._angle_a = self.to_deg(math.asin(2 * self._small_r / self._side))
            return self._angle_a
        return 0

    @property
    def angle_b(self) -> Union[int, float]:
        if self._angle_b:
            return self._angle_b
        elif self._angle_a:
            self._angle_b = 180 - self._angle_a
            return self._angle_b
        return 0

    @property
    def diag_1(self) -> Union[int, float]:
        if self._diag_1:
            return self._diag_1
        elif self._angle_b and self._side:
            # d_1 = side * sin(b) * 2
            self._diag_1 = self._side * math.sin(self.to_rad(self._angle_b / 2)) * 2
            return self._diag_1
        elif self._side and self._diag_2:
            # d_1 = √(4 * side² - d_2²)
            self._diag_1 = math.sqrt(4 * self._side**2 - self._diag_2**2)
            return self._diag_1
        elif self._angle_b and self._diag_1:
            # d_1 = d_2 * tg(b/2)
            self._diag_1 = self._diag_2 * math.tan(self.to_rad(self._angle_b / 2))
            return self._diag_1
        elif self._square and self._diag_2:
            # d_1 = 2*S / d_2
            self._diag_1 = 2 * self._square / self._diag_2
            return self._diag_1
        return 0

    @property
    def diag_2(self) -> Union[int, float]:
        if self._diag_2:
            return self._diag_2
        elif self._side and self._angle_b:
            # d_2 = side * cos(b) * 2
            self._diag_2 = self._side * math.cos(self.to_rad(self._angle_b / 2)) * 2
            return self._diag_2
        elif self._side and self._diag_1:
            # d_2 = √(4 * side² - d_1²)
            self._diag_2 = math.sqrt(4 * self._side**2 - self._diag_1**2)
            return self._diag_2
        elif self._angle_a and self._diag_1:
            # d_2 = d_1 * tg(a/2)
            self._diag_2 = self._diag_1 * math.tan(self.to_rad(self._angle_a / 2))
            return self._diag_2
        elif self._square and self._diag_1:
            # d_2 = 2*S / d_1
            self._diag_2 = 2 * self._square / self._diag_1
            return self._diag_2
        return 0

    @property
    def small_r(self) -> Union[int, float]:
        if self._small_r:
            return self._small_r
        elif self._height:
            # r=h/2
            self._small_r = self._height / 2
            return self._small_r
        return 0

    @property
    def square(self) -> Union[int, float]:
        if self._square:
            return self._square
        elif self._side and self._height:
            # S = side * h
            self._square = self._side * self._height
            return self._square
        elif self._diag_1 and self._diag_2:
            # S = (d1 * d2) / 2
            self._square = (self._diag_1 * self._diag_2) / 2
            return self._square
        elif self._small_r and self._side:
            # S=2 * side * r
            self._square = 2 * self._side * self._small_r
            return self._square
        return 0

    @property
    def perimeter(self) -> Union[int, float]:
        if self._perimeter:
            return self._perimeter
        elif self._side:
            self._perimeter = self._side * 4
            return self._perimeter
        return 0
