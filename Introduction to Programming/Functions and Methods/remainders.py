numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []
# any instances of %3 as 0
def remainders_3(numbers):
    return [number % 3 for number in numbers]
print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))
# any instance where %3 is 0 as false
def remainders_3(numbers):
    return [number % 3 != 0 for number in numbers]
print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))
# /// separate fizz and buzz /// 
numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []
# not any where %5 is 0
def remainders_5(numbers):
    return [number % 5 == 0 for number in numbers]
print(not any(remainders_5(numbers_1)))
print(not any(remainders_5(numbers_2)))
print(not any(remainders_5(numbers_3)))
print(not any(remainders_5(numbers_4)))
# all instances of %5 as 0
def remainders_5(numbers):
    return [number % 5 for number in numbers]
print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
