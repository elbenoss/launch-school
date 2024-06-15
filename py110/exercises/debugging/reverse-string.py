def reverse_string(string):
#   rev_str = ''
    for char in string:
        string = char + string[:-1]
#       rev_str = char + rev_str

    return string

print(reverse_string("hello") == "olleh")
