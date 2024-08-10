"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

def change_me(string):
    for word in string.split():
        if word == word[::-1]:
            string = string.replace(word, word.upper())
    print(string)



# Comments show expected return values
change_me("We will meet at noon")       # "We will meet at NOON"
change_me("No palindromes here")        # "No palindromes here"
change_me("")                           # ""
change_me("I LOVE mom and dad equally") # "I LOVE MOM and DAD equally"
