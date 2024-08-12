"""
The following dictionary has list values that contains strings. 
Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.
"""

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}


res = [] 
for key, value in dict1.items():
    for word in value:
        for letter in word:
            if letter.casefold() in 'aeiou':
               res.append(letter)


list_of_vowels = [letter for words in dict1.values()
                         for word in words
                         for letter in word if letter in 'aeiou']



print(list_of_vowels)
print(list_of_vowels == ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o'])

# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

# Start by trying to write this using nested loops.

# Extra Challenge: Once your nested loop code works, try to refactor the code so it uses a single list comprehension. 
# (You can print the resulting list outside of the comprehension.)



