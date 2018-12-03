#defining a function to factorize give number
def factorize(x):

    #creating an empty list to hold factors and also temp variable to hold number
    prime_fact = []
    temp = x
    
    #creating a function to know prime numbers within the range
    def prime(n):

	#creating an empty list to hold all prime numbers within range
        lst = []
       
	#checking for prime numbers 
        for a in range(2,n):
            for i in range(2,a):
                if(a%i == 0):
                    break
              
            else:
                lst.append(a)
                  
        return(lst)

	
    prime_lst = prime(x)

    #iterating within elements of list
    for i in (prime_lst):

	#iterating till square root of the given elements
        while(i*i <= temp):

	    #if divisible by prime number then store that prime value and also update value of dividend with quotient
            if(x%i == 0):
                x = x/i
                prime_fact.append(i)

            else:
               i += 1


        return(prime_fact)


#taking user input to know its prime factors
value = input("Eneter a number ")
result = factorize(value)
print(result)
