num_list = []
num_list.append(input("Enter the 1st number: "))
num_list.append(input("Enter the 2nd number: "))
num_list.append(input("Enter the 3rd number: "))
for i in range(4, 7):
    num_list.append(input(f"Enter the {i}th number: "))

if num_list[5] in num_list[0:5]:
    print(f"{num_list[5]} is in {','.join(num_list)}")
else:
    print(f"{num_list[5]} isn't in {','.join(num_list)}")
