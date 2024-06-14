def staggered_case(string):
    r_str = ''
    count = 0
    for i in range(len(string)):
        if string[i].isalpha():
            if count % 2 == 0:
                r_str += string[i].upper()
            elif count % 2 != 0:
                r_str += string[i].lower()
            count += 1
        else:
            r_str += string[i]
    return r_str




string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
