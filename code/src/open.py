#!/usr/bin/env pybricks-micropython
from code.src.config import CHECK_DISTANCE, HIGH_SPEED, LOW_SPEED
from code.src.line_detection import LineDetector
from pybricks.ev3devices import ColorSensor, GyroSensor, Motor, UltrasonicSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Direction, Port
from pybricks.tools import StopWatch, wait
from code.src.steering import Steering
from code.src.utils import get_distance
from code.src.wall_avoidance import DistanceKeeper

ev3 = EV3Brick()

steering_motor = Motor(Port.D)
rear_motor = Motor(Port.B)

gyro = GyroSensor(Port.S4, direction=Direction.COUNTERCLOCKWISE)
ultrasonic_left = UltrasonicSensor(Port.S1)
ultrasonic_right = UltrasonicSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)

steering = Steering(motor=steering_motor, gyro=gyro)
line_checker = LineDetector(color_sensor=color_sensor)
wall_distance_keeper = DistanceKeeper(ultrasonic_left, ultrasonic_right)

passed_lines = 0
distance = 0

steering.reset_angles()
rear_motor.reset_angle(0)

ev3.speaker.beep()

rear_motor.run(HIGH_SPEED)

direction_set = False
is_turning = False
clockwise = True
correction = 0

while passed_lines < 12:
    line = line_checker.check_line()
    new_distance = get_distance(rear_motor)
    if abs(new_distance - distance) > CHECK_DISTANCE:
        if line != "white" and not direction_set:
            direction_set = True
            wait(300)
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

    if direction_set and not is_turning:
        correction = wall_distance_keeper.correction(clockwise)
    else:
        correction = 0
        
    steer = steering.pid(wall=correction)
    
    if abs(steer) > 20:
        rear_motor.run(LOW_SPEED)
    else:
        rear_motor.run(HIGH_SPEED)

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

finish_dist = get_distance(rear_motor)
while abs(get_distance(rear_motor) - finish_dist) < 2000:
    correction = wall_distance_keeper.correction(clockwise)
    steering.pid(wall=correction)

rear_motor.stop()

ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
