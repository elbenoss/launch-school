num = int(input("Please enter an integer greater than 0: "))
operate = input("Enter \"s\" to compute the sum, or \"p\" to compute the product. ")
match operate:
    case 's':
        sum = 0
        for i in range(1, num+1):
            sum += i
        print(f"The sum of integers between 1 and {num} is {sum}.")
    case 'p':
        product = 1
        for i in range(1, num+1):
            product *= i
            print(i)
        print(f"The product of the integers between 1 and {num} is {product}.")
    case _:
        print('Invalid input.')