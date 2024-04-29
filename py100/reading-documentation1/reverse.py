#Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

# there is no in-built method for reverse a string like there is for a list.reverse()
# reverse indexing can be used 'hello'[::-1]
print('hello'[-1::])