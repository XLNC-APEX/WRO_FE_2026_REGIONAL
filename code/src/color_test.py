#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (
    ColorSensor,
)
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import wait
from line_detection import LineDetector
from utils import ColorHSV, color_id_as_str

ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S3)

# ORANGE = (28, 12, 9)
# WHITE = (30, 30, 77)
# BLUE = (7, 10, 20)


def recognize_colorb(rgb: tuple[int, int, int]):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    if sum(rgb) >= 55:
        return "white"
    elif b >= max(r, g):
        return "blue"
    else:
        return "orange"


while True:
    color = color_sensor.rgb()
    hsv = ColorHSV.from_rgb(color)
    ld = LineDetector(color_sensor)
    print(color, recognize_colorb(color))
    print(hsv, ld.recognize_color(color))
    wait(500)
