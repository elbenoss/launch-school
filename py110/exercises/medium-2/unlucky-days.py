"""
Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths 
in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar 
will remain in use for the foreseeable future.

"""


def is_leap_year(year):
    if year < 1752: 
        if year % 4 == 0:
            return True
        else:
            return False
    else:
        if year > 0 and year % 400 == 0:
            return True
        elif year > 0 and year % 4 == 0 and not year % 100 == 0:
            return True
        else:
            return False

def friday_the_13ths(year):
    e = (year // 10) % 10
    d = year % 10

    first = year // 100
    second = (e * 10) + d

    day = (second // 4) + 13

    months = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    if is_leap_year(year):
        months[0] -= 1
        months[1] -= 1
        
    m = [month + day for month in months]
    

    idx = [17, 18, 19, 20].index(first)
    gregorian = [4, 2, 0, 6][idx]

    
    days = [(i + second + gregorian) % 7 for i in m]
    return days.count(6)


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
