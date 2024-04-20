
def all_caps(a_string):
    return (a_string.upper() if len(a_string) > 10 else a_string)

print(all_caps(input("Enter a string: ")))
