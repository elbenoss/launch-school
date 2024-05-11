# Write a function that takes a string argument and returns a new string that contains the value of the 
# original string with all consecutive duplicate characters collapsed into a single character.

def crunch(str):
    new_list = [char for char in list(str)]
    list_length = len(new_list)
    i = 0
    while i < list_length:
        try:
            new_list[-i] == new_list[-i-1]
        except IndexError:
            print("NO MORE INDEXED")
        else:
            if new_list[-i] == new_list[-i-1] and list_length > 1:
                new_list.pop()
                i -= 1
        finally:
            list_length = len(new_list)
            i += 1
    print(new_list)
            




# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')



# print(crunch('ggggggggggggggg'))
print(crunch('ddaaiillyy ddoouubbllee'))

