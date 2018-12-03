
#defining a sorting function
def bubble_sort(lst):

	#iterating through list
	for i in range(len(lst)):
		#iterating through every element
		for j in range(len(lst)-1):

			# not in order
			if lst[j] > lst[j+1]:
				#swap
				lst[j],lst[j+1] = lst[j+1],lst[j]


	return(lst)


#taking user input
list1 = [114,234,17,298,453,965,723,192]
sort_lst = bubble_sort(list1)
print(sort_lst)
