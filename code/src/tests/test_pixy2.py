#!/usr/bin/env pybricks-micropython
from pixy2 import Pixy2
from pybricks.parameters import Port
from pybricks.tools import wait

# TODO: Figure out how to move to tests folder instead of src. Add all tests, run them independently.

cam = Pixy2(port=Port.S1)
print(cam.get_version())
print(cam.get_resolution())
print("Toggling lamps")
cam.set_lamp(True, True)
wait(200)
cam.set_lamp(False, False)

# print(cam.get_linetracking_data()) #TODO: this crashes,unstable: Read wrong type of packet: 3 instead of 49

while True:
    red = cam.get_blocks(1, 1)
    green = cam.get_blocks(2, 1)
    if red[0] > 0:
        print("red", red[1][0].x_center)
    if green[0] > 0:
        print("green", green[1][0].x_center)
    wait(1000)
