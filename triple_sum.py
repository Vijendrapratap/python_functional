def triple_sum(lst, n): 
  
 	for i in range(0, n): 
      
		for j in range(i+1, n): 
          
			for k in range(j+1, n): 
				pass
              
	if (lst[i] + lst[j] + lst[k] == 0): 
		print(lst[i], lst[j], lst[k]) 
	
                   
	else:
		print(" not exist ") 
 

  
lst = []
number = input("How many elements you wanna add : ")
for i in range(number):
	elements = input("Please enter your elements : ")
	lst.append(elements)
	print(lst) 
n = len(lst) 
triple_sum(lst, n) 
