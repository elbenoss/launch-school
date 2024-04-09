def age_calc(age):
    n = 10
    for i in range(1, 5):
      print(f'In {n} years, you will be {int(age)+n} years')
      n += 10
age_calc(age = input("Enter age: "))