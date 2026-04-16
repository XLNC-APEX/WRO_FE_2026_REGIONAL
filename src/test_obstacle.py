#!/usr/bin/env pybricks-micropython
from config import CHECK_DISTANCE
from line_detection import LineDetector
from pybricks.ev3devices import ColorSensor, GyroSensor, Motor, UltrasonicSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import StopWatch, wait
from pixy2 import Pixy2
from steering import Steering
from utils import get_distance
from wall_avoidance import DistanceKeeper

ev3 = EV3Brick()

steering_motor = Motor(Port.D)
rear_motor = Motor(Port.B)

gyro = GyroSensor(Port.S4)
# ultrasonic_left = UltrasonicSensor(Port.S1)
ultrasonic_right = UltrasonicSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)

steering = Steering(motor=steering_motor, gyro=gyro)

camera = Pixy2(port=Port.S1)


steering.reset_angles()
rear_motor.reset_angle(0)

# ev3.speaker.beep()

rear_motor.run(-200)

red_obstacles = []
green_obstacles = []

DESIRED_X_GREEN = 30
DESIRED_X_RED = 286

CAM_RESOLUTION = (316, 208)

Kp = 0.3

while True:
    red_obstacles = camera.get_blocks(1, 1)
    green_obstacles = camera.get_blocks(2, 1)
    
    if red_obstacles[0] > 0:
        x = red_obstacles[1][0].x_center
        error = x - DESIRED_X_RED
        pixy_correction = error * Kp
        steering.pid(pixy=pixy_correction)
        print("RED: ", pixy_correction, "POS", x)
    elif green_obstacles[0] > 0:
        x = green_obstacles[1][0].x_center
        error = x - DESIRED_X_GREEN
        pixy_correction = error * Kp
        steering.pid(pixy=pixy_correction)
        print("GREEN: ", pixy_correction)
    else:
        steering.pid()
        print("NO OBSTACLE")
    print("Angle: ", steering_motor.angle())
    wait(400)