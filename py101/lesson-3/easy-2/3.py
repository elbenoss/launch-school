# Programmatically determine whether 42 lies between 10 and 100, inclusive. 
# Do the same for the values 100 and 101,

#for i in range(10,101):
#    if i == 42 or i == 100 or i == 101:
#        print(f"{i} is between 10 and 100")
print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))
