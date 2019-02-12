import turtle
import math 


def convert_deg_to_rad(angle_deg):
    radian = angle_deg / 180 * math.pi
    return radian

def convert_rad_to_deg(rad):
    return rad / math.pi * 180

def findo(angle_deg,radius):
    angle_radian = convert_deg_to_rad(angle_deg)
    o = radius * math.sin(angle_radian / 2)
    return o


def drawPolyCircle(noOfSides, radius):
    degEachTriangle = 360 / noOfSides
    o = findo(degEachTriangle, radius)



    internalAngle = 180-((noOfSides - 2) * 180)/noOfSides
    print( internalAngle )

    for i in range(noOfSides):
        turtle.forward( round( 2 * o) )
        turtle.left(internalAngle)

for i in range(5,10):
    sides = round(1.5**i)
    print(sides)
    drawPolyCircle(sides, 200)
