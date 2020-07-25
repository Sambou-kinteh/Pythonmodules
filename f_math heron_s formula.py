import math
import sys

print("\t\t\tInput In Here Your Values\n\n")
print("HERONS FORMULA\n")
a = input(">>a: ")
b = input(">>b: ")
c = input(">>c: ")
s = ((int(a)+int(b)+int(c)))/2
def area(a,b,c,s):

    return math.sqrt(int(s) * ((int(s) - int(a)) * (int(s) - int(b)) * (int(s) - int(c))))
print("Area :",area(a,b,c,s))
