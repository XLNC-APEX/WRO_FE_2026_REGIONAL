#!/usr/bin/env pybricks-micropython
from config import CHECK_DISTANCE
from line_detection import LineDetector
from pybricks.ev3devices import (
    ColorSensor,
    GyroSensor,
    InfraredSensor,
    Motor,
    TouchSensor,
    UltrasonicSensor,
)
from pybricks.hubs import EV3Brick

# from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, wait
from steering import Steering
from utils import get_distance
from wall_avoidance import DistanceKeeper

ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S3)

# ORANGE = (28, 12, 9)
# WHITE = (30, 30, 77)
# BLUE = (7, 10, 20)


def recognize_color(rgb: tuple[int, int, int]):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    if sum(rgb) >= 100:
        return "white"
    elif b - r >= 10 and b - g >= 10:
        return "blue"
    else:
        return "orange"


while True:
    color = color_sensor.rgb()
    print(color, recognize_color(color))
    wait(500)
