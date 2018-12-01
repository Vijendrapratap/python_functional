
#defining a function to get prime numbers in range of 1000
def prime(n):

	#taking a empty list to store all prime numbers in range
    lst = []


    for a in range(n):
        for i in range(2,a):

	#checking conditions for prime number 
	#if it is divisible by any nunber other than 1 and itself then it is not a prime number
            if(a%i == 0):
                break
        else:
		
		#updating list with the prime numbers
        	lst.append(a)
    return(lst)

#calling function
t = prime(1001)
print("{} these are the prime numbers in given range".format(t))
