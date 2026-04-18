from utils import find_perpendicular
from config import SAFE_DISTANCE_FROM_WALLS
from pybricks.ev3devices import UltrasonicSensor

Kp = 0.2

class DistanceKeeper:
    def __init__(self, ultrasonic_left: UltrasonicSensor, ultrasonic_right: UltrasonicSensor):
        self.ultrasonic_left = ultrasonic_left
        self.ultrasonic_right = ultrasonic_right
        
    def correction(self, clockwise: bool, heading: int, target: int):
        if clockwise:
            d = self.ultrasonic_left.distance()
        else:
            d = self.ultrasonic_right.distance()
            
        d = find_perpendicular(heading, d, target)
        # print("ultrasonic:", d)

        error = SAFE_DISTANCE_FROM_WALLS - d
        if clockwise:
            error *= -1

        if abs(error) < 10:
            error = 0

        return Kp * error


class DistanceKeeperOneUltrasonic:
    def __init__(self, ultrasonic: UltrasonicSensor):
        self.ultrasonic = ultrasonic

    def correction(self, clockwise: bool, heading: int, target: int):
        d = self.ultrasonic.distance()
        d = find_perpendicular(heading, d, target)

        error = SAFE_DISTANCE_FROM_WALLS - d
        if clockwise:
            error *= -1

        if abs(error) < 20:
            error = 0

        return Kp * error
