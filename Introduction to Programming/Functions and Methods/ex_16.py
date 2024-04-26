def multiply(left, right):      #In the code shown below, identify all of the function names and parameters present in the code. 
    return left * right         #Include the line numbers for each item identified.

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

#line 1 multiply is defined function with left, right parameters
#line 4 get_num is defined function with prompt parameter
#line 5 float and input
#line 7,8 get_num function
#line 9 multiply function
#line 10 print function

