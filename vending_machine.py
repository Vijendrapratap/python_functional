#defining a function taking input of integer as change
def vendingmachine(change):

    #we have a list of notes stored in vending machine
    lst = [1000, 500, 100, 50, 10, 5, 2, 1]

    #empty list to store notes
    list1 = []
    for i in range(len(lst)):
        while change >= 0:
            if change < lst[i] :
                break
            else:
                #substracting money from change and again checking until change is 0
                change = change - lst[i]
                list1.append(lst[i])
                vendingmachine(change)
    return list1


#user input
nmb1 = int(input("Enter product price : "))
nmb2 = int(input("Money put in vending machine : "))
deff = nmb2 - nmb1


if deff > 0:
    result = vendingmachine(deff)
    print(result)
    print("You receive {} notes".format(len(result)))
elif deff < 0:
    print("Please pay full amount")
else:
    print("Thank you")
