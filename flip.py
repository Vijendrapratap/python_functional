#importing random module to get random output

import random

#creating a function coin_toss

def coin_toss(number):

#initializing some values of heads and tails

	head = 0
	tail = 0

#looping over our input to check what output we get
	
	for i in range(number):
		
		#randint will give int output from range 0 - 1
		flip = random.randint(0, 1)

		if (flip == 0):
			print("it is HEADS ")
			
			#increasing value of head by 1 if we get head as a output
			head = head + 1

		else:
			print("it is TAILS ")

			#increasing value of head by 1 if we get head as a output
			tail = tail + 1


#calculating percentage of heads and tails

	per_of_head = ((head/float(number)) * 100)
	print("percentage of head is :",per_of_head)

	per_of_tail = ((tail/float(number)) * 100)
	print("percentage of tail is :",per_of_tail)

#taking input from user
num = input("please enter a number")

#calling our function to perform its task
result = coin_toss(num)
