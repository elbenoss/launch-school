def single_int(int_a):
    if int_a < 0:
        print(f"{int_a} is less than 0")
    elif int_a >= 0 and int_a <= 50:
        print(f"{int_a} is between 0 and 50")
    elif int_a > 50 and int_a <= 100:
        print(f"{int_a} is between 51 and 100")
    else:
        print(f"{int_a} is greater than 100")

single_int(int(input("Enter a single integer: ")))
