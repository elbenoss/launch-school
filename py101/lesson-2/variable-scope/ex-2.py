#What will the following code print and why? Don't run it until you have tried to answer.

num = 5

def my_func():
    num = 10

my_func()
print(num)

# 5
# function creates local num
# global num is still 5.
