"""
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0. If either of these conditions is not satisfied, 
the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and returns one of the following four strings representing 
the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry about floating point errors. You may also assume that the arguments are in degrees.

"""


def triangle(a1, a2, a3):
    if [a1, a2, a3].count(90) == 1:
        return "right"
    elif sum([1 for i in [a1, a2, a3] if i < 90]) == 3 and sum([a1, a2, a3]) == 180:
        return "acute"
    elif [i for i in [a1, a2, a3] if i > 90]:
        return "obtuse"
    else:
        return "invalid"



print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

