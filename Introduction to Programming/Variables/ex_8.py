#Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.
#Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.
initial_amount = 1000
compound_interest = .05
frequency = 1
years = 5
balance = initial_amount * (1 + (compound_interest/frequency) )**(frequency * years)
single_expression = 1000 * (1.05**(5))


