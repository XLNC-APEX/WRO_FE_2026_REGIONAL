from config import SAFE_DISTANCE_FROM_WALLS
from pybricks.ev3devices import UltrasonicSensor

Kp = 0.03


class DistanceKeeper:
    def __init__(self, ultrasonic_left: UltrasonicSensor, ultrasonic_right: UltrasonicSensor):
        self.ultrasonic_left = ultrasonic_left
        self.ultrasonic_right = ultrasonic_right

    def correction(self, clockwise: bool):
        if clockwise:
            d = self.ultrasonic_left.distance()
        else:
            d = self.ultrasonic_right.distance()
        print("ultrasonic:", d)

        error = SAFE_DISTANCE_FROM_WALLS - d
        if clockwise:
            error *= -1

        if abs(error) < 5:
            error = 0

        return Kp * error


class DistanceKeeperOneUltrasonic:
    def __init__(self, ultrasonic: UltrasonicSensor):
        self.ultrasonic = ultrasonic

    def correction(self, clockwise: bool):
        d = self.ultrasonic.distance()

        error = SAFE_DISTANCE_FROM_WALLS - d
        if clockwise:
            error *= -1

        if abs(error) < 5:
            error = 0

        return Kp * error
