# What will the following code output?
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# str1 is initialized with 'hello there'
# str2 is initialized by referencing str1, pointing towards the same location in memory
# str2 is then reassigned goodbye, pointing to a new location in memory
# str1 is passed as an argument to the print function outputting:
# "hello there"
