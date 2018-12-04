#creating a class of temperature
class Temperature():
    def __init__(self, temp):
        self.temp = temp

    #first method to convert from fahrenheit to celsius
    def incelsius(self, temp):
        tempc = (temp - 32)*(5/float(9))
        return tempc

    #second method to convert from celsius to fahrenheit
    def infahrenheit(self, temp):
        tempf = (temp *(9/float(5))) + 32
        return tempf


#taking user input
temp = float(input("Enter temperature : "))
unit = input("If it is in Celsius enter c or C  and if it is in Fahrenheit enter f or F ")

#creating object for class
T = Temperature(temp)

#checking our input and printing our result
if (unit == "c") or (unit == "C"):
    result = T.infahrenheit(temp)
    print(result)

elif (unit == "f") or (unit == "F"):
    result = T.incelsius(temp)
    print(result)

else:
    print("Please enter a valid input")
