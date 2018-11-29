#importing time module for accessing current time

import time

#user input to start the clock

start = raw_input("please enter to start your clock")

#start_time store the time of starting

start_time = time.time()
print(start_time)

#user input to stop the clock

end = raw_input("press any key to stop your clock")

#end_time store the time of stopping

end_time = time.time()
print(end_time)

#diff will give the difference between end time and start time 

diff = end_time - start_time

print("time difference is : ",diff)
