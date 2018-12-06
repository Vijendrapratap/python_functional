

#difining a binary function
def binarySearch (lst, l, r, w): 

	#sorting our list as we always need a sorted list
	lst.sort()
	
	 
	if r >= l: 

		#finding mid index of our list
		mid = (r + l)//2


		if lst[mid] == w: 
			return mid 
		
		#if our word lies between mid point and lower bond we use recursive function and also change the index of range
		elif lst[mid] > w: 
			return binarySearch(lst, l, mid-1, w) 


		#if our word lies between mid point and range we use recursive function and also change the index of lower bond
		else: 
			return binarySearch(lst, mid+1, r, w) 

	else: 
	 
		return -1


lst = ["a", "quick", "brown","fox", "jumps", "over", "the", "lazy", "dog"] 
find_word = input("Enter the word you wanna search : ")

# Function call 
result = binarySearch(lst, 0, len(lst)-1, find_word) 

if result != -1: 
	print("Element is present at index ", result)
else: 
	print("Element is not present in list")

