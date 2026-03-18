import math

from config import WHEEL_DIAMETER
from pybricks.ev3devices import Motor


def constrain(x, low, high):
    return max(low, min(high, x))


def normalize_angle(angle):
    return (angle + 180) % 360 - 180


def get_distance(motor: Motor):
    return motor.angle() / 360 * (WHEEL_DIAMETER * math.pi)
