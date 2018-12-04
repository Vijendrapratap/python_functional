#creating a class for payments
class Payment():

    def __init__(self, principle, rate, year):
        self.principle = principle
        self.rate = rate
        self.year = year

    #defining a method for calculation of monthly payment
    def monthlypayment(self, principle, rate, year):
        n = 12 * year
        r = self.rate/(12 * 100)
        p = principle * r
        temp = 1 - (1 + r)**(-n)
        payinter = p/float(temp)     #applying formula
        return payinter


#taking user input
amount = float(input("Enter principle value : "))
rate = float(input("Enter rate : "))
time = float(input("Enter year : "))

pay = Payment(amount, rate, time)

monthlypay = pay.monthlypayment(amount, rate, time)
print("you have to make monthly payment of ",monthlypay)