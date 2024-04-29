#What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# produces an error because foo isn't defined in the same scope