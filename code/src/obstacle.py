#!/usr/bin/env pybricks-micropython
from config import CHECK_DISTANCE, HIGH_SPEED, LOW_SPEED
from line_detection import LineDetector
from ObstacleDetection import ObstacleDetection
from pixy2 import Pixy2
from pybricks.ev3devices import ColorSensor, GyroSensor, Motor, UltrasonicSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Direction, Port
from pybricks.tools import wait
from steering import Steering
from utils import get_distance
from wall_avoidance import DistanceKeeperOneUltrasonic

ev3 = EV3Brick()

steering_motor = Motor(Port.D)
rear_motor = Motor(Port.B)

gyro = GyroSensor(Port.S4, direction=Direction.COUNTERCLOCKWISE)
ultrasonic = UltrasonicSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)
camera = Pixy2(port=Port.S1)

steering = Steering(motor=steering_motor, gyro=gyro)
line_checker = LineDetector(color_sensor=color_sensor)
wall_distance_keeper = DistanceKeeperOneUltrasonic(ultrasonic)
obstacle_detection = ObstacleDetection(camera)

passed_lines = 0
distance = 0

steering.reset_angles()
rear_motor.reset_angle(0)

ev3.speaker.beep()

rear_motor.run(HIGH_SPEED)

direction_set = False
is_turning = False
clockwise = True
wall_correction = 0
pixy_correction = 0

while passed_lines < 12:
    line = line_checker.check_line()
    new_distance = get_distance(rear_motor)
    if abs(new_distance - distance) > CHECK_DISTANCE:
        if line != "white" and not direction_set:
            direction_set = True
            # wait(300)
            if line == "blue":
                clockwise = False

        is_turning = False

        if direction_set and clockwise and line == "orange":
            ev3.speaker.beep()
            steering.increase_target_angle(-90)
            is_turning = True
            distance = new_distance
            passed_lines += 1
        elif direction_set and not clockwise and line == "blue":
            ev3.speaker.beep()
            steering.increase_target_angle(90)
            is_turning = True
            distance = new_distance
            passed_lines += 1

    pixy_correction = obstacle_detection.get_correction()

    if direction_set and not is_turning:
        wall_correction = wall_distance_keeper.correction(clockwise, steering.heading, passed_lines)
    else:
        wall_correction = 0

    steer = steering.pid(pixy=pixy_correction, wall=wall_correction)

    if abs(steer) > 20 or abs(pixy_correction) > 0:
        rear_motor.run(LOW_SPEED)
    else:
        rear_motor.run(HIGH_SPEED)

    # print(
    #     "heading:",
    #     steering.heading,
    #     "target:",
    #     steering.target_angle,
    #     "steer:",
    #     steering_motor.angle(),
    #     "rear motor speed:",
    #     rear_motor.speed()
    # )
    wait(20)

# finish_dist = get_distance(rear_motor)
# while abs(get_distance(rear_motor) - finish_dist) < 2000:
#     wall_correction = wall_distance_keeper.correction(clockwise)
#     steering.pid(wall=wall_correction)

rear_motor.stop()

ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
