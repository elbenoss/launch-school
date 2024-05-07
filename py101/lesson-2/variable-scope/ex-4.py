#What will the following code print and why? Don't run it until you have tried to answer.
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# Hello World
# outer_var is referenced from outer function to print
