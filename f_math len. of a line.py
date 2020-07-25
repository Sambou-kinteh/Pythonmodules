#importing the required modules
import sys
import math
print("\t\t\tFor line AB")
print("Input Your coodinates for x and y ")
x1 = input("x1: ")
y1 = input("y1: ")
x2 = input("x2: ")
y2 = input("y2: ")
AB = math.sqrt((int(y2) - int(y1))**2 + (int(x2) - int(x1))**2)
print("AB = ",AB)
