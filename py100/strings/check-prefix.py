#Write a function that checks whether a string starts with a specific prefix.

def starts_with(word, pre):
    # return not word == word.removeprefix(pre)
    return word.startswith(pre)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True