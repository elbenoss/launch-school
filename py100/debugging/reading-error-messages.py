#You come across the following code. What errors does it raise for the given examples and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)      # takes 1 arg, 6 were given
find_first_nonzero_among(1)                     # int object is not iterable
# requires a list to iterate among several members to find the first non zero


