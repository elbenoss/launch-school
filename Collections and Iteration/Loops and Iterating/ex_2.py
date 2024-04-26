#Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.
age = int(input("How old are you? "))
print(f"You are {age} years old.")
for i in range(1, 5):
    future = i * 10
    print(f"In {future} years, you will be {age+future} years old.")
