#The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

#What is the difference between the year attribute and the isocalendar method?
# year returns the year from the date/datetime object
# isocalendar returns a tuple with the year, week, and weekday
print(today_year)
print(iso_year)