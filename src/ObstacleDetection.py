from pixy2 import Pixy2
from utils import Line2D, Point2D

# CAM_RESOLUTION = (316, 208)
Kp = 0.3

RED_LINE = Line2D(1, 1)
GREEN_LINE = Line2D(1, 1)


class ObstacleDetection:
    def __init__(self, camera: Pixy2):
        self.camera = camera
        self.red_obstacles = []
        self.green_obstacles = []
        self.correction = 0
        # self.prev_error = 0

    def update(self):
        self.red_obstacles = self.camera.get_blocks(1, 1)
        self.green_obstacles = self.camera.get_blocks(2, 1)

    def _calculate_correction(self, p: Point2D, line: Line2D) -> float:
        # Simple x error instead of perpendicular, it is easier to compute and is proportional? to perp.
        return (p.x - line.x(p.y)) * Kp

    def get_correction(self):
        self.update()

        red_count = self.red_obstacles[0]
        green_count = self.green_obstacles[0]

        if red_count > 0 and green_count > 0:
            red = self.red_obstacles[1][0]
            green = self.green_obstacles[1][0]
            if red.width * red.height > green.width * green.height:
                self.correction = self._calculate_correction(
                    Point2D(red.x_center, red.y_center), RED_LINE
                )
            else:
                self.correction = self._calculate_correction(
                    Point2D(green.x_center, green.y_center), GREEN_LINE
                )
        elif red_count > 0:
            red = self.red_obstacles[1][0]
            self.correction = self._calculate_correction(
                Point2D(red.x_center, red.y_center), RED_LINE
            )
        elif green_count > 0:
            green = self.green_obstacles[1][0]
            self.correction = self._calculate_correction(
                Point2D(green.x_center, green.y_center), GREEN_LINE
            )
        else:
            self.correction = 0
        print("pixy-correction: ", self.correction)
        return self.correction
