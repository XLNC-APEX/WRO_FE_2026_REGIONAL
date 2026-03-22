from pixy2 import Pixy2
from pybricks.parameters import Port
from pybricks.tools import wait

#TODO: Figure out how to move to tests folder instead of src. Add all tests, run them independently.

cam = Pixy2(Port.S2)
print(cam.get_version())
print(cam.get_resolution())
print("Toggling lamps")
cam.set_lamp(True, True)
wait(200)
cam.set_lamp(False, False)
print(cam.get_blocks(1|2, 8))
# print(cam.get_linetracking_data()) #TODO: this crashes,unstable: Read wrong type of packet: 3 instead of 49
