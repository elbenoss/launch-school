#Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. 
#Otherwise, it should return the original string. 
#Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def all_caps(a_string):
    return (a_string.upper() if len(a_string) > 10 else a_string)

print(all_caps(input("Enter a string: ")))
