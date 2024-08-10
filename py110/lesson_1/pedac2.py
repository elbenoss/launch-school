"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

# input: string
# output sub-strings in a list?
# rules:
#   - in each input check if two-letter or greater sequences are palindromic
#   - forward and backward is same (palindromic)
#   - case-sensitive
#   - ?? empty substrings should result in empty list ??

# find palindrome by searching BEGIN to i var if i == 2
# also from i var to i + 2 and from i var to -1 index

# i + 2
# (i + 1) + 2 
# 0 + i
# 1 + i
# etc.

# for i 0-len
#   for j 0-len
#       (i = 0)

# create an empty list to hold this resulting substring
# for each index from 0 through the next to last index position
# for each length value from 2 through the longest possible substring
# extract the substring of that length starting at the current index posiiton
# add the substring to our resulting list

"""

- create empty list 'result' for substrings
- init 'start_index' var to 0 for first char of substring
- iterate over string from 'start_index' to length of string - 2
    - init 'num_chars' var to 2 for initial substring length
    - iterate from 'num_chars' to length of string - 'start_index'
    - append extracted substring to 'result'
    - increment 'num_chars' by '1'
  - end inner loop
  - increment 'start_index' by '1'
- end outer loop
- return 'result' list

"""

"""
def palindrome_substrings(string):
    result = []
    start_index = 0

    while start_index <= len(string) - 2:
        num_chars = 2
        while num_chars <= len(string) - start_index:
            substring = string[start_index:start_index + num_chars]
            result.append(substring)
            num_chars += 1
        start_index += 1
    print(result)

"""

def palindrome_substrings(string):
    result = []

    for i in range(len(string) - 2):
        for j in range(len(string) - i):
            result.append(string[i:i+j])
    print(result)



"""
def palindrome_substrings(s):
    result = []
    substrings_list = substrings(s)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)
    
    return result
"""

"""
def palindrome_substrings(string):
    print(string)
    result = []
    substrings_list = []
    length = len(string)
    
    for i in range(length - 2):
        for j in range(2, length - i):
            substrings_list.append(string[i:j])
    print(substrings_list)
"""






"""
def palindrome_substrings(string):
    res = []
    substr_list = []
    for i in range(len(string) + 1):
        if i < len(string) - 2:
            substr_list.append(string[i:-1])
        if i > 1:
            substr_list.append(string[0:i])
    for word in substr_list:
        if word == word[::-1]:
            res.append(word)
    print(res)
"""


# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
#palindrome_substrings("palindrome") # []
#palindrome_substrings("")           # []
#palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
#palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]
