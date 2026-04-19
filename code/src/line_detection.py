from pybricks.ev3devices import ColorSensor
from utils import ColorID, ColorHSV

COLOR_ORANGE = ColorHSV(15, 75, 12)  # CMYK (0, 60, 100, 0)
COLOR_BLUE = ColorHSV(235, 84, 4.8)  # CMYK(100, 80, 0, 0)
# COLOR_WHITE = ColorHSV(222, 52, 25)


class LineDetector:
    def __init__(self, color_sensor: ColorSensor):
        self.color_sensor = color_sensor

    # def recognize_color(self, rgb: tuple[int, int, int]) -> int:
    #     r = rgb[0]
    #     g = rgb[1]
    #     b = rgb[2]

    #     if sum(rgb) >= 90:
    #         return ColorID.WHITE
    #     elif b >= min(r, g) + 10:
    #         return ColorID.BLUE
    #     else:
    #         return ColorID.ORANGE

    def recognize_color(self, rgb: tuple[int, int, int]) -> int:
        color = ColorHSV.from_rgb(rgb)
        # if color.in_range(COLOR_ORANGE, 20, 15, 10):
        #     return ColorID.ORANGE
        # if color.in_range(COLOR_BLUE, 10, 10, 5):
        #     return ColorID.BLUE
        # return ColorID.WHITE
        # if color.s < 60:
        #     return ColorID.WHITE
        # elif color.h > 200:
        #     return ColorID.BLUE
        # return ColorID.ORANGE
        if color.in_range(COLOR_ORANGE, 20, 15, 10):
            return ColorID.ORANGE
        if (color.s < 60) or (color.v > 21):
            return ColorID.WHITE
        return ColorID.BLUE

    def check_line(self):
        color = self.color_sensor.rgb()
        # print("rgb: ", color)
        return self.recognize_color(color)
