from config import BLUE_LINE, COLOR_RANGE, ORANGE_LINE
from pybricks.ev3devices import ColorSensor


def _check_color(color, target):
    return target - COLOR_RANGE <= color <= target + COLOR_RANGE


class LineDetector:
    def __init__(self, color_sensor: ColorSensor):
        self.color_sensor = color_sensor

    def check_line(self):
        color = self.color_sensor.rgb()
        if all(_check_color(c, t) for c, t in zip(color, ORANGE_LINE)):
            return "orange"
        elif all(_check_color(c, t) for c, t in zip(color, BLUE_LINE)):
            return "blue"
        else:
            return "white"
