# Write a program that asks for user's name, then greets the user. 
#If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

name = input("What is your name? ")
if name.isupper():
    print(f"HELLO {name}! WHY ARE WE YELLING?")
else:
    print(f"Hello {name}.")