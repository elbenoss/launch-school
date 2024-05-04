bill = float(input("What is the bill? "))
tip_per = float(input("What is the tip percentage? "))/100
tip = bill * tip_per
print(f"The tip is ${tip}\nThe total is ${bill+tip}")