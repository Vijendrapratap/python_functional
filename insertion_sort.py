
#defining a sorting function
def insertion_sort(lst):

	#iterating over lst
	for i in lst:
	    j = lst.index(i)

	    #i is not the first element
	    while j>0:

		#not in order
		if lst[j-1] > lst[j]:

		    #swap
		    lst[j-1],lst[j] = lst[j],lst[j-1]
		else:
		    #in order
		    break
		j = j-1
	
	return lst


#taking user input
a = [616, 519, 113, 915, 210, 812, 174]
sorted_lst = insertion_sort(a)
print(sorted_lst)
