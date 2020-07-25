#y1-y=(y2-y1)/(x2-x1)(x-x1)
import math
x1 = input("x1: ")
y1 = input("y1: ")
x2 = input("x2: ")
y2 = input("y2: ")
def eq(x1,x2,y1,y2):
    a = int(y1)
    b = int(y2) - int(y1)
    c = int(x2) - int(x1)
    d = int(x1)
    return (a - y == (int(b)/int(c))*(x - int(d)))
print("Eq: ",eq(x1,x2,y1,y2))
