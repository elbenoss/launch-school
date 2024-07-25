"""
Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.

"""


def sum_square_difference(n):
    return sum(range(1, n + 1)) ** 2 - sum([i ** 2 for i in range(1, n + 1)])






print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
