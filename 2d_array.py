
#taking user input to enter number of rows and colomns
m = input("Enter number of rows")
n = input("Enter number of columns")


#creating a empty list
l = []


#adding another list to the existing list making it 2d
for i in range(m):
	l.append([])

#now adding j number of colomns to all the i number of rows and initializing them with value 0
for i in range(m):
	for j in range(n):
		l[i].append(j)
		l[i][j] == 0


#now entering elements to the matrix 	
for i in range(m):
	for j in range(n):
		print("rows : ", i+1 ,"colomns : ", j+1)

		l[i][j] = int(input())

#printing result
print(l)


