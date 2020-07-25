import math
import sys

x='cal 1(BY: sam programmer)'
sys.stdout.write(x + '\n')
print("\tHi User, i am a simple bot that solves quadratic equations")
print(">>a: ")
a = sys.stdin.readline()
print(">>b: ")
b = sys.stdin.readline()
print(">>c: ")
c = sys.stdin.readline()

'''x_1 = (int(b)**2) - ((4) * int(a) * int(c))
x_11 = math.sqrt(int(x_1))
x_12 = (-b)+int(int(x_11))
x1 = (int(x_12)//(2)*int(a))'''

'''x1 = ((-b) + (math.sqrt(int(b)**2)-float((4)*int(a)* int(c)))/(2)*int (a))
x2 = ((-b) - (math.sqrt(int(b)**2)-float((4)*int(a)* int(c)))/(2)*int (a))'''
#x1 = ((lambda a,b,c:(b**2 - 4*a*c)/2*a))
'''def quadratic(a,b,c):
    return (-(int(b)) + ((int(b)**2 - 4*int(a)*int(c))))/2*int(a)
print("x1 = ",quadratic(a,b,c))'''
#for x1
try:
    def quadratic(a,b,c):
        x1= int(b)**2
        x2= 4*int(a)*int(c)
        x3= 2*int(a) 
        x4= -(-(int(x1)) + (int(x2)))
        x5= math.sqrt(x4)
        return (round((-(int(b)) + (x5)))/x3)
    print("your value for x1 is:")
    print("x1 = ",quadratic(a,b,c))
    print("your value for x2 is:")

#for x2
    def quadratic(a,b,c):
        x6= int(b)**2
        x7= 4*int(a)*int(c)
        x8= 2*int(a) 
        x9= -(-(int(x6)) + (int(x7)))
        x10= math.sqrt(x9)
        return (round((-(int(b)) - (x10)))/x8)
    print("x2 = ",quadratic(a,b,c))
    print("Have a good day")
#print("x1 = \n",x1)
#print("x2 = \n",x2)
except ValueError:
    print('An error occured while solving\n\tThe value of root is negative')
    print('Input a valid quadratic equation')

      
