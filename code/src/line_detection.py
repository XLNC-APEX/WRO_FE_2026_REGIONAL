from pybricks.ev3devices import ColorSensor


class LineDetector:
    def __init__(self, color_sensor: ColorSensor):
        self.color_sensor = color_sensor

    def recognize_color(self, rgb: tuple[int, int, int]):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        if sum(rgb) >= 110:
            return "white"
        elif b >= max(r, g):
            return "blue"
        else:
            return "orange"



    def check_line(self):
        color = self.color_sensor.rgb()
        print("rgb: ", color)
        return self.recognize_color(color)
