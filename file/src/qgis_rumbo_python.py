# https://github.com/rcfdtools
# Calling function and return:
# dist = coursepy(cx, cy, dcx, dcy)[0]
# course = coursepy(cx, cy, dcx, dcy)[1]
# label = coursepy(cx, cy, dcx, dcy)[2]
# Sample for label:
# print(coursepy(10, 20, 50, 38)[2])

from qgis.core import *
from qgis.gui import *
# To test online https://www.online-python.com/
# Require: import math as math
from math import *
import math as math

@qgsfunction(group='Custom', referenced_columns=[])

def coursepy(cx, cy, dcx, dcy):
    roundv = 6
    dist = math.sqrt((cx - dcx)**2 + (cy - dcy)**2)
    distY = abs(cy - dcy)
    distX = abs(cx - dcx)
    if distY != 0:
        ang = math.atan(distX / distY) * 180 / math.pi
    else:
        ang = 0
    if cx >= dcx and cy >= dcy:
        course = "N" + str(round(ang, roundv)) + "E"
    elif cx >= dcx and cy <= dcy:
        course = "S" + str(round(ang, roundv)) + "E"
    elif cx <= dcx and cy >= dcy:
        course = "N" + str(round(ang, roundv)) + "W"
    else:
        course = "S" + str(round(ang, roundv)) + "W"
    label = f"D(m): {round(dist, roundv)}\nCourse: {course}"   
    return [round(dist, roundv), course, label]


