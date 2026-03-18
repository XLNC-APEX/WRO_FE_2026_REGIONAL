from config import MAX_STEER
from pybricks.ev3devices import GyroSensor, Motor
from pybricks.tools import StopWatch
from utils import constrain, normalize_angle

Kp = 3
Ki = 0
Kd = 0.5


class Steering:
    def __init__(self, motor: Motor, gyro: GyroSensor):
        self.motor = motor
        self.gyro = gyro
        self.target_angle = 0
        self.integral_sum = 0
        self.last_error = 0
        self.timer = StopWatch()

    def increase_target_angle(self, angle):
        self.target_angle += angle

    def reset_angles(self):
        self.gyro.reset_angle(0)
        self.motor.reset_angle(0)

    def reset_time(self):
        self.timer.reset()

    def get_sec(self):
        return self.timer.time() / 1000

    def pid(self, extra=0.0):
        dt = self.get_sec()
        dt = max(dt, 0.01)

        heading = self.gyro.angle()

        error = normalize_angle(self.target_angle - heading)

        derivative = (error - self.last_error) / dt
        self.integral_sum += error * dt

        self.integral_sum = constrain(self.integral_sum, -100, 100)  # TODO: CHANGE IT

        out = (error * Kp) + (self.integral_sum * Ki) + (derivative * Kd)
        out += extra
        out = constrain(out, -MAX_STEER, MAX_STEER)

        self.motor.track_target(out)

        self.last_error = error

        self.reset_time()
