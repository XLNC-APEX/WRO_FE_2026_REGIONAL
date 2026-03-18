from config import CHECK_DISTANCE
from line_detection import LineDetector
from pybricks.ev3devices import (
    ColorSensor,
    GyroSensor,
    InfraredSensor,
    Motor,
    TouchSensor,
    UltrasonicSensor,
)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait
from steering import Steering
from utils import get_distance
from wall_avoidance import DistanceKeeper

ev3 = EV3Brick()

steering_motor = Motor(Port.D)
rear_motor = Motor(Port.B)

gyro = GyroSensor(Port.S1)
ultrasonic_left = UltrasonicSensor(Port.S2)
ultrasonic_right = UltrasonicSensor(Port.S3)
color_sensor = ColorSensor(Port.S4)


steering = Steering(motor=steering_motor, gyro=gyro)
line_checker = LineDetector(color_sensor=color_sensor)
wall_distance_keeper = DistanceKeeper(ultrasonic_left, ultrasonic_right)

passed_lines = 0
distance = 0


steering.reset_angles()
steering.reset_time()
rear_motor.reset_angle(0)

ev3.speaker.beep()

rear_motor.run(-900)

while passed_lines < 24:
    correction = wall_distance_keeper.correction()
    steering.pid(extra=correction)

    line = line_checker.check_line()
    new_distance = get_distance(rear_motor)
    if new_distance - distance > CHECK_DISTANCE:
        if line != "white":
            passed_lines += 1
            distance = new_distance

        if passed_lines % 2 != 0:
            ev3.speaker.beep()
            if line == "orange":
                steering.increase_target_angle(90)
            elif line == "blue":
                steering.increase_target_angle(-90)

    print(
        "heading:", gyro.angle(), "target:", steering.target_angle, "steer:", steering_motor.angle()
    )

    wait(20)


rear_motor.stop()

ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
