import re


mob = input("ENTER YOUR MOB NUMBER")
print(mob)

if re.search(r'^(0,+91)?[1-9]\d{9}$',mob):
    print("it is a valid number")
elif re.search(r"^[1-9]{3}-\d{3}-\d{4}$",mob) :
    print("it is a valid number")
elif re.search(r"^([1-9]{3})(\d{3})(\d{4})$",mob) :
    print("it is a valid number")
    
    
else : 
    print ("Invalid Number")  
  

