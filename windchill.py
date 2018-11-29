
#definig a function to calculate windchill temp
def windchill(v,t):
	 
	w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*(v**0.16)

	#returning value 
	return w


#taking user input

temp = input("Enter temperature in farenheit less than 50f : ")
velocity = input("Enter velocity of air in between 3-120 m/h : ")

#applying condition according to our formula demands

if (velocity >= 3) and (velocity <= 120) and (temp <= 50):

	wind_chill = windchill(velocity, temp)

	print("Effective temperature will be {} farenheit".format(wind_chill))

else:
	print("Entered values are not in range of formula")
