#Consider the data in the following table:
name_country_table = {
	'Alice': 	'USA',
	'Francois': 	'Canada',
	'Inti': 	'Peru',
	'Monika': 	'Germany',
	'Sanyu': 	'Uganda',
	'Yoshitaka': 	'Japan',
	}
names = [key for key in name_country_table]
strname = str(names)[1:-1].replace("'", "")
print(strname)
chosen_name = input("Pick name to see country: \n").title()
print(name_country_table[chosen_name])
