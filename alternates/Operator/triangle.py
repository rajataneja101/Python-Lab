#03/02/2017

import math

side1   = float(input("Enter side 1 : "))
side2   = float(input("Enter side 2 : "))
angle   = float(input("Enter angle in degrees : "))

side3   = math.sqrt(side1**2 + side2**2 - 2*side1*side2*math.cos(angle))

print("The third side is : ", side3)