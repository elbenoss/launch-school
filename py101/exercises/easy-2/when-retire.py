# Build a program that displays when the user will retire and how many years she has to work till retirement.

# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!
import datetime
age = int(input('What is your age? '))
retire = int(input('At what age would you like to retire? '))
current_year = datetime.datetime.now().year
retire_year = (retire - age) + current_year
print(f"It's {current_year}. You will retire in {retire_year}.")
print(f"You have only {retire - age} years of work to go!")