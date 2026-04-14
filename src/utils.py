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
    def __init__(
        self,
        k: float,
        b: float,
    ) -> None:
        self.k: float = k
        self.b: float = b

    def y(self, x: float) -> float:
        return x * self.k + self.b

    def x(self, y: float) -> float:
        return (y - self.b) / self.k


class Point2D:
    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self.x: float = x
        self.y: float = y
