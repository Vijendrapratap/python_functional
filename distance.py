
#importing math module to perform mathematical operations
import math

#defining function to calculate distance
def distance(x,y):

	#applying Euclid formula for distance calculation
	dist = math.sqrt(x*x + y*y)
	
	return dist

#taking user input for co-ordinates of x and y

x = input("Enter co-ordinate of x : ")
y = input("Enter co-ordinate of y : ")

dist = distance(x,y)

print "distance of co-ordinates from origin is : ",dist
