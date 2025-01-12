import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

    
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y

        return Vector(new_x, new_y)

    def __mul__(self, other):

        print(f"{self = }, {other = }")

        product = (self.x * other.x) + (self.y * other.y)

        return product

    def __abs__(self):

        squares = (self.x ** 2) + (self.y ** 2)

        return math.sqrt(squares)


    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'


v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)


print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0