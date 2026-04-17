import math

from config import WHEEL_DIAMETER
from pybricks.ev3devices import Motor


def constrain(x, low, high):
    return max(low, min(high, x))


def normalize_angle(angle):
    angle %= 360
    if angle >= 180:
        angle -= 360
    if angle < -180:
        angle += 360
    return angle


def get_distance(motor: Motor):
    return motor.angle() / 360 * (WHEEL_DIAMETER * math.pi)


class Line2D:
    def __init__(self, k: float, b: float) -> None:
        self.k: float = k
        self.b: float = b

    def y(self, x: float) -> float:
        return x * self.k + self.b

    def x(self, y: float) -> float:
        return (y - self.b) / self.k

    def invert_in_x_range_to(self, x: float) -> Line2D:
        return Line2D(-self.k, self.b + self.k * x)

    def __str__(self) -> str:
        return f"y = {float(self.k)}x + {float(self.b)}"


class Curve2D:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_x(self, y: float) -> float:
        return self.a * (y**2) + self.b * y + self.c


# RED: y = 129.94021*x^0 + -1.282576*x^1 + 0.003517*x^2
# GREEN: y = 215.021075*x^0 + 1.319625*x^1 + -0.004968*x^2


class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y


def find_perpendicular(heading: int, dist: int, passed_lines):
    return math.cos((heading - passed_lines * 90) * math.pi / 180) * dist