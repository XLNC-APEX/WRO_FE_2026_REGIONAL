from pixy2 import Pixy2

# CAM_RESOLUTION = (316, 208)
Kp = 0.3
DESIRED_X_GREEN = 30
DESIRED_X_RED = 286


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

    def _calculate_correction(self, x: int, is_green: bool):
        if is_green:
            error = x - DESIRED_X_GREEN
        else:
            error = x - DESIRED_X_RED
        return error * Kp

    def get_correction(self):
        self.update()

        red_count = self.red_obstacles[0]
        green_count = self.green_obstacles[0]

        if red_count > 0 and green_count > 0:
            red = self.red_obstacles[1][0]
            green = self.green_obstacles[1][0]
            if red.width * red.height > green.width * green.height:
                self.correction = self._calculate_correction(red.x_center, is_green=False)
            else:
                self.correction = self._calculate_correction(green.x_center, is_green=True)
        elif red_count > 0:
            x = self.red_obstacles[1][0].x_center
            self.correction = self._calculate_correction(x, is_green=False)
        elif green_count > 0:
            x = self.green_obstacles[1][0].x_center
            self.correction = self._calculate_correction(x, is_green=True)
        else:
            self.correction = 0
        print("pixy-correction: ", self.correction)
        return self.correction
