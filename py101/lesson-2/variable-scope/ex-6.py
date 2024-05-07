#What will the following code print and why? Don't run it until you have tried to answer.
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# Inner 1: 25 local variable defined in function
# Inner 2: 15 variable defined in outermost function

