#!/usr/bin/env pybricks-micropython
from config import CHECK_DISTANCE
from line_detection import LineDetector
from pybricks.ev3devices import ColorSensor, GyroSensor, Motor, UltrasonicSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import StopWatch, wait
from steering import Steering
from utils import get_distance
from wall_avoidance import DistanceKeeper

ev3 = EV3Brick()

steering_motor = Motor(Port.D)
rear_motor = Motor(Port.B)

gyro = GyroSensor(Port.S4)
ultrasonic_left = UltrasonicSensor(Port.S1)
ultrasonic_right = UltrasonicSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)

steering = Steering(motor=steering_motor, gyro=gyro)
line_checker = LineDetector(color_sensor=color_sensor)
wall_distance_keeper = DistanceKeeper(ultrasonic_left, ultrasonic_right)

passed_lines = 0
distance = 0

steering.reset_angles()
steering.reset_time()
rear_motor.reset_angle(0)

ev3.speaker.beep()

rear_motor.run(-2000)

timer = StopWatch()

first = True
clockwise = True

while passed_lines < 12:
    correction = wall_distance_keeper.correction(clockwise)
    steering.pid()

    line = line_checker.check_line()
    new_distance = get_distance(rear_motor)
    if abs(new_distance - distance) > CHECK_DISTANCE:
        if line != "white" and first:
            first = False
            if line == "blue":
                clockwise = False

        if clockwise and line == "orange":
            ev3.speaker.beep()
            steering.increase_target_angle(90)
            distance = new_distance
            passed_lines += 1
        elif not clockwise and line == "blue":
            ev3.speaker.beep()
            steering.increase_target_angle(-90)
            distance = new_distance
            passed_lines += 1

    print(
        "heading:",
        gyro.angle(),
        "target:",
        steering.target_angle,
        "steer:",
        steering_motor.angle(),
        "color:",
        line,
        "distance:",
        new_distance,
    )
    wait(20)


rear_motor.stop()

ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
