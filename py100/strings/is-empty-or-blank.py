#Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:

def is_empty_or_blank(s):
    # return True if not s or s.isspace() else False
    return not s.strip(' ')

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
