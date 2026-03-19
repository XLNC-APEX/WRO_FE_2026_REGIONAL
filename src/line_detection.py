from config import BLUE_LINE, COLOR_RANGE, ORANGE_LINE
from pybricks.ev3devices import ColorSensor


class LineDetector:
    def __init__(self, color_sensor: ColorSensor):
        self.color_sensor = color_sensor

    def recognize_color(self, rgb: tuple[int, int, int]):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        if r >= 30 and g >= 30 and b >= 30:
            return "white"
        elif b > 10 and r < 10 and g < 10:
            return "blue"
        else:
            return "orange"

    def check_line(self):
        color = self.color_sensor.rgb()
        return self.recognize_color(color)
