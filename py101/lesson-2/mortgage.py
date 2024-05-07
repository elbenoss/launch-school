loan_amount = float(input("Enter principal amount: "))
apr = float(input("Enter annual percentage rate: ")) / 100
loan_duration_years = float(input("Enter the loan term: "))

monthly_interest_rate = apr / 12
loan_duration_months = loan_duration_years * 12

monthly_payment = loan_amount * ( monthly_interest_rate / ( 1 - (1 + monthly_interest_rate) ** (-loan_duration_months) ) )

print(monthly_payment)