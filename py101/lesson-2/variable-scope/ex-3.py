#What will the following code print and why? Don't run it until you have tried to answer.
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# 10
# global num is referenced in function before assigning 10
