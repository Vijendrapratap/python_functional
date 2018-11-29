
#importing random module for random output
import random

#defining function
def coupon(n):

	#initializing values 
	count = 0
	l = set()

	#looping over to get random output until length of set is less than or equal to our required output
	while (len(l) <= n):

		#also adding values from random output to our set
		l.add(random.randint(1, n+10))

		#increasing count to get how many chances we take to get desired output
		count += 1

	return l, count	
		
	
#taking user input 
no_of_codes = input("how many distinct coupon codes you want : ")
codes,times = coupon(no_of_codes)

#display output
print("here are the unique set of codes : {} , and it takes {} chances to get unique code".format(codes,times))
