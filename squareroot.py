
#defining a function for square root with newtons method
def newtonSqrt(n):

    #taking a approx value of root
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)  #improving approx value with better value

    while better != approx:             #keep on updating approx value until it is equal to better value
        approx = better
        better = 0.5 * (approx + n/approx)
    return approx


#taking user input to find root of number
nmb = int(input("Enter a number : "))
root = newtonSqrt(nmb)
print("Root of {} is {}".format(nmb, root))