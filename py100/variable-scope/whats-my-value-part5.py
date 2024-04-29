#What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# original value of a is 1
# this would print when function is invoked but does not because a is assigned as a local varible afterwards giving an error that a is accessed before being defined
