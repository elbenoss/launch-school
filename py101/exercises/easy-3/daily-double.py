# Write a function that takes a string argument and returns a new string that contains the value of the 
# original string with all consecutive duplicate characters collapsed into a single character.

def crunch(str):
    new_letters = []
    for i in range(len(str)):
        new_letters.append(str[i])
        if str[i] == str[i-1] and i < len(str) and len(new_letters) > 1:
            new_letters.pop()
    return "".join(new_letters)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')