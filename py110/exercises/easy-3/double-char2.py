def double_consonants(string):
    s_list = []
    for char in string:
        if char.isalpha() and char not in ['a', 'e', 'i', 'o', 'u']:
            s_list.append(char*2)
        else:
            s_list.append(char)
    return "".join(s_list)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
