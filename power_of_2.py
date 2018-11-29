
#defining a function for giving output as power of 2
def power(n):
	
	#checking our conditions if the input value is in range
 	if (n >= 0) and (n <= 31):
		for i in range(1, n+1):
			print(2**i)

	elif (n > 31):
		print("out of memory")

	else:
		print("Enter a positive value")

#getting user input

t = input("enter a number")
k = power(t)
		
