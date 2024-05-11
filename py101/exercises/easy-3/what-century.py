# Write a function that takes a year as input and returns the century. 
# The return value should be a string that begins with the century number, 
# and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

def century(number):
    cent = (number//100)
    if 1 <= number % 10 <= 100:
        cent += 1
    if cent%100 not in [int(x) for x in list(range(11, 20))]:
        match cent % 10:
            case 1:
                    ordinal = 'st'
            case 2:
                    ordinal = 'nd'
            case 3:
                    ordinal = 'rd'
            case _:
                    ordinal = 'th'
    else:
          ordinal = 'th'
    return f"{cent}{ordinal}"
            
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True