#importing complex mathematics module

import cmath

#defining a function to calculate roots of quadratic equation
def quadratic(a, b, c):
	delta = (b*b) - 4*a*c
	

	#using sqrt function from cmath module to get square root of numbers
	root1 = (-b + cmath.sqrt(delta))/2*a
	root2 = (-b - cmath.sqrt(delta))/2*a 

	return root1, root2

print("equation must be in form of ax^2 + bx + c = 0")

#taking user input 

cof_x = input("enter cofficient of x : ")
cof_y = input("enter cofficient of y : ")
constant = input("enter value of constant :  ")

r1, r2 = quadratic(cof_x, cof_y, constant)

print"roots of the equations are", r1, r2
