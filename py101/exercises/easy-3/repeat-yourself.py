# Write a function that takes two arguments, a string and a positive integer, 
# then prints the string as many times as the integer indicates.

def repeat(str, int):
    for _ in range(int):
        print(str)

repeat('Hello', 3)