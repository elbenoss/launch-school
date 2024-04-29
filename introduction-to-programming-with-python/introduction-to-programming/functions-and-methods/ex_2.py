#Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# bar because the initial assignment is foo = 'bar' and the function call of set_foo only changes on a local scope