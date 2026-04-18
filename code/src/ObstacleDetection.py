from config import MIN_OBSTACLE_AREA
from pixy2 import Pixy2
from utils import Curve2D, Point2D

CAM_WIDTH = 316
CAM_HEIGHT = 208
Kp = 0.3

# v1
# RED_LINE = Line2D(-1.206, 172.5)
# GREEN_LINE = Line2D(1.747, -364.8)
# GREEN_LINE = Line2D(1.206, -208.596)
# GREEN_LINE = RED_LINE.invert_in_x_range_to(CAM_WIDTH)

# v2
RED_CURVE = Curve2D(0.003517, -1.282576, 129.94021)
GREEN_CURVE = Curve2D(-0.004968, 1.319625, 215.021075)


class ObstacleDetection:
    def __init__(self, camera: Pixy2):
        self.camera = camera
        self.red_obstacles = []
        self.green_obstacles = []
        self.correction = 0

    def update(self):
        try:
            self.red_obstacles = self.camera.get_blocks(1, 1)
            self.green_obstacles = self.camera.get_blocks(2, 1)
        except Exception as e:
            print(e)

    def _calculate_correction(self, p: Point2D, curve: Curve2D) -> float:
        # Simple x error instead of perpendicular, it is easier to compute and is proportional? to perp.
        return (curve.get_x(p.y) - p.x) * Kp

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

        if red_count > 0 and 30 < self.red_obstacles[1][0].y_center and red_area > green_area:
            if red_area >= MIN_OBSTACLE_AREA:
                red = self.red_obstacles[1][0]
                self.correction = self._calculate_correction(
                    Point2D(red.x_center, red.y_center), RED_CURVE
                )
        elif green_count > 0:
            if green_area >= MIN_OBSTACLE_AREA and 30 < self.green_obstacles[1][0].y_center:
                green = self.green_obstacles[1][0]
                self.correction = self._calculate_correction(
                    Point2D(green.x_center, green.y_center), GREEN_CURVE
                )

        print("pixy-correction: ", self.correction, "green: ", green_count, "red: ", red_count)
        return self.correction
