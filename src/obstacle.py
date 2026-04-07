#!/usr/bin/env pybricks-micropython
from config import CHECK_DISTANCE
from line_detection import LineDetector
from ObstacleDetection import ObstacleDetection
from pixy2 import Pixy2
from pybricks.ev3devices import ColorSensor, GyroSensor, Motor, UltrasonicSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import StopWatch, wait
from steering import Steering
from utils import get_distance
from wall_avoidance import DistanceKeeperOneUltrasonic

ev3 = EV3Brick()

steering_motor = Motor(Port.D)
rear_motor = Motor(Port.B)

gyro = GyroSensor(Port.S4)
ultrasonic_right = UltrasonicSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)
camera = Pixy2(port=Port.S1)

steering = Steering(motor=steering_motor, gyro=gyro)
line_checker = LineDetector(color_sensor=color_sensor)
wall_distance_keeper = DistanceKeeperOneUltrasonic(ultrasonic_right)
obstacle_detection = ObstacleDetection(camera)

passed_lines = 0
distance = 0

steering.reset_angles()
steering.reset_time()
rear_motor.reset_angle(0)

# ev3.speaker.beep()

rear_motor.run(-500)

timer = StopWatch()

first = True
clockwise = True
wall_correction = 0
pixy_correction = 0

while passed_lines < 12:

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
    
    pixy_correction = obstacle_detection.get_correction()
    
    if not first:
        wall_correction = wall_distance_keeper.correction(clockwise)
        
    steering.pid(pixy=pixy_correction, wall=wall_correction)
    
    print(
        "heading:",
        gyro.angle(),
        "target:",
        steering.target_angle,
        "steer:",
        steering_motor.angle(),
    )
    wait(20)

finish_dist = get_distance(rear_motor)
while abs(get_distance(rear_motor) - finish_dist) < 2000:
    wall_correction = wall_distance_keeper.correction(clockwise)
    steering.pid(wall=wall_correction)

rear_motor.stop()

ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
