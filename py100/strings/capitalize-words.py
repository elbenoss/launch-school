#Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

print('launch school tech & talk'.title())

def capitalize_words(string):
    list = []
    words = string.split()
    for word in words:
        list.append(word.capitalize())
    return ' '.join(list)


string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)  # Launch School Tech & Talk