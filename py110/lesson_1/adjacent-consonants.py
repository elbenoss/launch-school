"""
Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. 
If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

- Step 1
input: list of strings
output: same list sorted by highest number of adjacent consonants
rules: 
    1. counted consonants can have a space in between separate words
    2. if there is a tie between two strings their original order is maintained
-
- Step 2

-
- Step 3
lists are used for input and output
-
- Step 4
given list use sort function with key argument
key argument is from custom function counting adjacent consonants
function takes string and adds counter going through the characters disregarding spaces
return the count
sort takes the count and orders it by highest number to lowest number


-
- Step 5

"""


def c_count(string):
    count = -1
    high = 0
    for let in string:
        if let not in 'aeiou':
            count += 1
            if count > high:
                high = count
        else:
            count = -1

    return high 


def sort_by_consonant_count(lst):
    new_lst = sorted(lst, key=c_count, reverse=True)
    return new_lst



my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])
# ['xxxx', 'xxxb', 'xxxa']
