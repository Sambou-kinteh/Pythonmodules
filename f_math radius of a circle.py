import math
print(" \tFor the radius of a cirlce\n \tGiven the 'g','f' and 'c'\n\n")
g = input("value of g: ")
f = input("value of f: ")
c = input("value of c: ")
r = math.sqrt(int(g)**2 + int(f)**2 - int(c))
print("r = ",r)
