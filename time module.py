import time
#print(time.ctime(0))
#print(time.time())
#print(time.ctime(time.time()))
Time_given = time.localtime()
time_object = time.strftime("%B %Y %dth %H: %M : %S",Time_given )
print(time_object)
time_string = "17th November 2023"
time_giv = time.strptime(time_string , "%dth %B %Y")
print(time_giv)