
#creating a class for checking our days of week
class DayOfWeek():
    def __init__(self,day, month, year):
        self.day = day
        self.month = month
        self.year = year

#defining a method to calculate our day
    def calendar(self,day, month, year):
        y = year - (14 - month)/12                    #applying Gregorian method of calculation
        x = y + y/4 - y/100 + y/400
        m = month + 12*(14 - month)/12 - 2
        d = round((day + x + 31*month/12)%7, 0)              #getting day in terms of number

        return d

#setting days of week for different output values
    def week(self, date):
        if date == 0:
            print("Day is Monday")
        elif date == 1:
            print("Day is Tuesday")
        elif date == 2:
            print("Day is Wednesday")
        elif date == 3:
            print("Day is Thursday")
        elif date == 4:
            print("Day is Friday")
        elif date == 5:
            print("Day is Saturday")
        elif date == 6:
            print("Day is Sunday")
        else:
            print("invalid input")


#taking user input for finding days
day = int(input("Enter date : "))
month = int(input("Enter months : "))
year = int(input("Enter year : "))

DOW = DayOfWeek(day, month, year)

#calling methods of class

result = DOW.calendar(day, month, year)
dayofweek = DOW.week(result)
