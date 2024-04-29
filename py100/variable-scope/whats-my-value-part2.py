#What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# my_function is called. 
#x previously assigned with 10. 
#this value isn't pulled into scope. 
#an undefined x is reassigned to itself plus 5 resulting in an error.