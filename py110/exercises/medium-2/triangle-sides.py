"""
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. 
If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 
    'equilateral', 'isosceles', 'scalene', or 'invalid'.
"""


def triangle(a1, a2, a3):
    if 0 < a1 and 0 < a2 and 0 < a3 and max(a1, a2, a3) - min(a1, a2, a3) - min(a1, a2, a3) <= 0:
            if a1 == a2 == a3:
                return "equilateral"
            elif a1 == a2 != a3:
                return "isosceles"
            else:
                return "scalene"
    else:
        return 'invalid'
            





print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
