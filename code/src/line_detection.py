from pybricks.ev3devices import ColorSensor
from utils import ColorHSV, ColorID

COLOR_ORANGE = ColorHSV(24, 100, 100)  # CMYK (0, 60, 100, 0)
COLOR_BLUE = ColorHSV(228, 100, 100)  # CMYK(100, 80, 0, 0)


class LineDetector:
    def __init__(self, color_sensor: ColorSensor):
        self.color_sensor = color_sensor

    # Find the closest color. TODO: proper percentages, colors.
    def recognize_color(self, rgb: tuple[int, int, int]) -> int:
        color = ColorHSV.from_rgb(rgb)
        if color.in_range(COLOR_ORANGE, 10, 5, 30):
            return ColorID.ORANGE
        if color.in_range(COLOR_BLUE, 10, 5, 30):
            return ColorID.BLUE
        return ColorID.WHITE

    def check_line(self) -> int:
        color = self.color_sensor.rgb()
        # print("rgb: ", color)
        return self.recognize_color(color)
