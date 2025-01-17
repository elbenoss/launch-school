# The or operator returns a truthy value if either or both of its operands are truthy, 
# a falsy value if both operands are falsy. 
# The and operator returns a truthy value if both of its operands are truthy, 
# and a falsy value if either operand is falsy. 
# This works great until you need only one of two conditions to be truthy, 
# the so-called exclusive or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two arguments, 
# and returns True if exactly one of its arguments is truthy, False otherwise.

def xor(arg1, arg2):
    # if arg1 or arg2:
    #     if not arg1:
    #         return(bool(arg2))
    #     elif not arg2:
    #         return(bool(arg1))
    # elif arg1 and arg2:
    #     return False
    return bool((arg1 and not arg2) or (arg2 and not arg1))
    
print(xor(5, 0))
print(xor(False, True))
print(xor(1, 1))
print(xor(True, True))
