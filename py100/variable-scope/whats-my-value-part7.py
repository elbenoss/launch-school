#What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# prints 2 because global a is reassigned 2 within  my_function which is called before the print