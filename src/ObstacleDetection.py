from config import MIN_OBSTACLE_AREA
from pixy2 import Pixy2
from utils import Line2D, Point2D

# CAM_RESOLUTION = (316, 208)
Kp = 0.25

RED_LINE = Line2D(-1.206, 172.5)
# GREEN_LINE = Line2D(1.747, -364.8)
GREEN_LINE = Line2D(1.206, -208.596)


class ObstacleDetection:
    def __init__(self, camera: Pixy2):
        self.camera = camera
        self.red_obstacles = []
        self.green_obstacles = []
        self.correction = 0

    def update(self):
        self.red_obstacles = self.camera.get_blocks(1, 1)
        self.green_obstacles = self.camera.get_blocks(2, 1)

    def _calculate_correction(self, p: Point2D, line: Line2D) -> float:
        # Simple x error instead of perpendicular, it is easier to compute and is proportional? to perp.
        return (line.x(p.y) - p.x) * Kp

    def get_correction(self):
        self.update()

        red_count = self.red_obstacles[0]
        green_count = self.green_obstacles[0]

        red_area = 0
        green_area = 0
        self.correction = 0

        if red_count > 0:
            red_area = self.red_obstacles[1][0].width * self.red_obstacles[1][0].height
        if green_count > 0:
            green_area = self.green_obstacles[1][0].width * self.green_obstacles[1][0].height

        if red_area > green_area:
            if red_area >= MIN_OBSTACLE_AREA:
                red = self.red_obstacles[1][0]
                self.correction = self._calculate_correction(
                    Point2D(red.x_center, red.y_center), RED_LINE
                )
        else:
            if green_area >= MIN_OBSTACLE_AREA:
                green = self.green_obstacles[1][0]
                self.correction = self._calculate_correction(
                    Point2D(green.x_center, green.y_center), GREEN_LINE
                )

        print("pixy-correction: ", self.correction)
        return self.correction