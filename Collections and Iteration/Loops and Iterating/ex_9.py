#Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

def factorial(n):
   i = 0
   fac = 1
   while i < n:
       i += 1
       fac *= i
   print(fac)
factorial(8)
