def is_real_palindrome(string):
    list = string.split()
    for words in list:
        for char in words:
            if not char.isalnum():
                list[list.index(words)] = words.replace(char, "")
    res = ''.join(list).lower()
    return res == res[::-1]



print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
