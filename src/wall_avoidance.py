from config import SAFE_DISTANCE_FROM_WALLS
from pybricks.ev3devices import UltrasonicSensor
from math import cos

Kp = 0.004


class DistanceKeeper:
    def __init__(self, ultrasonic_left: UltrasonicSensor, ultrasonic_right: UltrasonicSensor):
        self.ultrasonic_left = ultrasonic_left
        self.ultrasonic_right = ultrasonic_right

    def correction(self, angle):
        self.d = self.ultrasonic_right.distance()
        self.d_shortest = self.d * cos(angle)
        # d = self.ultrasonic_left.distance()

        error = SAFE_DISTANCE_FROM_WALLS - self.d_shortest

        return (Kp * error)
