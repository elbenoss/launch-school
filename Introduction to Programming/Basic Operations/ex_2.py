#This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.
#Use the REPL and the arithmetic operators to extract the individual digits of 4936:
num = 4936

one_place = num % 10
tens_place = (num//10) % 10
hundreds_place = (num//100) % 10
thousands_place = (num//1000)

