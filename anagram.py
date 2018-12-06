#importing collections module 
import collections

#defining function that takes input of two strings
def isanagram(n1, n2):

	#initializing two empty lists
	l1 = []
	l2 = []

	#appending elements of strings in a list
	for i in n1:
		l1.append(i)
	for j in n2:
		l2.append(j)

	#by Counter method we could check if the lists are equal , means they have same number of elements as well as elements are also same
 
	if (collections.Counter(l1) == collections.Counter(l2)):
		print("yes they are anagram ")

	else:
		print("nope! they are not anagram")


if __name__ == '__main__':
	#user input for string
	name1 = input("Enter a string : ")
	name2 = input("Enter another string : ")

	#calling our function
	t = isanagram(name1, name2)
