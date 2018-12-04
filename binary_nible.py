#defining a function to convert decimal into binary number
def tobinary(n):

    #taking an empty list to hold values of binary number
    lst = []
    while(n > 0):

        dig = n % 2
        lst.append(dig)
        n = n // 2

     #reversing our list to get right output
    lst.reverse()
    return (lst)

#defining a function to convert binary number into decimal
def todecimal(a):
    a.reverse()
    d = 0
    for j in range(0, len(a)):
        d = d + a[j] * pow(2, j)

    return d

#taking user input
num = int(input("Enter a number : "))
#first converting it into binary number
bin1 = tobinary(num)
for i in bin1:
    print(i, end = "")


#reversing our binary number and converting it into decimal number
bin1.reverse()
dec1 = todecimal(bin1)

print("\n new number after reversing the binary number ",dec1)

#checking if new number is power of 2
for i in range(dec1):
    pass
if 2**i == dec1:
    print("{} it is power of 2".format(dec1))
else:
    print("{} it is not power of 2".format(dec1))

