import time
print(time.ctime(0))  #epoch= when computer thinks time began (reference point)
print(time.time())    #returns current seconds since epoch
print(time.ctime(time.time())) #prints current date and time
time_object = time.localtime()
local_time = time.strftime("%B %d %Y %H:%M:%S")
print(local_time)
time_string = "16 april 2003"
time_ex = time.strptime(time_string,"%d %B %Y")
print(time_ex)
#(year, month, day, hours, mins, secs, #day of the week, #day of the year, dst(0 or -1))
time_tuple = (2021, 11, 15, 21, 31, 20, 0, 0, 0)
time_readable = time.asctime(time_tuple) #allows us to print the given time in tuple in a readable form
time_readable_in_sec = time.mktime(time_tuple) #gives total seconds since epoch till the time in the tuple
print(time_readable)
print(time_readable_in_sec)
