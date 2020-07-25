from math import hypot
class vector():
    'solving Vectors'

    def __init__(self, a = 0, b = 0):

        self.a = a
        self.b = b


    def __add__(self, other):
        return vector(self.a + other.a, self.b + other.b)
    
    def __repr__(self): 
      return 'Vector (%r, %r)' % (self.a, self.b)

    def __sub__(self, other):
        return vector(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        try:
            return vector(self.a * other.a, self.b * other.b)
        except AttributeError:
            return vector(self.a * other, self.b * other)

    def __abs__(self):
        return hypot(self.a, self.b)

    def __bool__(self):
        return bool(abs(self))

v1 = vector(5, -10)
v2 = vector(-5, 10)

print(v1 + v2)
print(bool(v1))
print(abs(v2))
