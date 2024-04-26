#Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.
def age_calc(age):
    n = 10
    for i in range(1, 5):
      print(f'In {n} years, you will be {int(age)+n} years')
      n += 10
age_calc(age = input("Enter age: "))

