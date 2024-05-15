# Given a string that consists of some words and an assortment of non-alphabetic characters, 
# write a function that returns that string with all of the non-alphabetic characters replaced by spaces. 
# If one or more non-alphabetic characters occur in a row, 
# you should only have one space in the result (i.e., the result string should never have consecutive spaces).
import string
def clean_up(str):
    new_char = []
    for i in range(len(str)):
        if str[i].isalpha():
            new_char.append(str[i])
        elif str[i-1].isalpha() or str[i+1].isalpha() and not str[i].isspace():
            new_char.append(" ")
    return "".join(new_char)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True