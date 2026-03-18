from config import SAFE_DISTANCE_FROM_WALLS
from pybricks.ev3devices import UltrasonicSensor

Kp = 0.4


class DistanceKeeper:
    def __init__(self, ultrasonic_left: UltrasonicSensor, ultrasonic_right: UltrasonicSensor):
        self.ultrasonic_left = ultrasonic_left
        self.ultrasonic_right = ultrasonic_right

    def correction(self):
        d = self.ultrasonic_left.distance()

        error = SAFE_DISTANCE_FROM_WALLS - d

        return Kp * error
