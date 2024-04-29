#Write a function that takes a single integer argument and prints a message that describes whether:

def number_range(int_a):
    if int_a < 0:
        print(f"{int_a} is less than 0")
    elif int_a >= 0 and int_a <= 50:
        print(f"{int_a} is between 0 and 50")
    elif int_a > 50 and int_a <= 100:
        print(f"{int_a} is between 51 and 100")
    else:
        print(f"{int_a} is greater than 100")

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0