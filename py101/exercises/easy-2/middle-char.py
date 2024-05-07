# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. 
# If the string has an odd length, you should return exactly one character. 
# If the string has an even length, you should return exactly two characters.

def center_of(str):
    median = len(str)//2
    if len(str) % 2 == 0:
        return str[median-1:median+1]
    else:
        return(str[median])

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True