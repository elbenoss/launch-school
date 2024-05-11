# Given a string that consists of some words and an assortment of non-alphabetic characters, 
# write a function that returns that string with all of the non-alphabetic characters replaced by spaces. 
# If one or more non-alphabetic characters occur in a row, 
# you should only have one space in the result (i.e., the result string should never have consecutive spaces).

def clean_up(str):
    # if str.isascii():
        # print(str)
    list = str.split()
    print(list)
    cleaned_list = []
    for i in list:
        for char in i:
            print(char)
            if char.isalpha():
                cleaned_list.append(char)
            else:
                cleaned_list.append(" ")
            
            

    r = ("".join(cleaned_list))
    print(r)
    print(' '.join(r.split()))
    


# print(clean_up("---what's my +*& line?") == " what s my line ")
# True


print(clean_up("---what's my +*& line?"))
