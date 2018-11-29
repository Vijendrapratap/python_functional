
#creating a function to check leap year
def leap_year(year):

	
	if (year % 4 == 0):
		if (year % 100 == 0):
			if (year % 400 == 0):
				print("it is a leap year ")

			else:
				print("it is not a leap year")

		else:
				print("it is a leap year")

	else:
		print("it is not a leap year")


#taking user input 
year = input("enter a year ") 

#storing value of year in year1
year1 = year
count = 0

#checking if entered value is of 4 digits or not
while (year>0):
	year = year/10
	count += 1

if count == 4:
	check = leap_year(year1)


else:
	print("please enter four digit number")


