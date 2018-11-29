
#creating a function for summation of harmonic progression
def harmonic(n):

	if (n <= 0):
		return 0 
	else:
		
		#using recusrsion to send values to function again
		return ((1/float(n)) + harmonic(n-1))
		
#taking user input
number = int(input("enter a number : "))

#calling function
k = harmonic(number)
	
print("Harmonic sum is : {}".format(k))






