import threading
import time
def eating():
    time.sleep(3)
    print("am eating for pliz")
def reading():
    time.sleep(4)
    print("am reading my books slowly")  
def going():
    time.sleep(5)
    print("am walking to xul")
x = threading.Thread(target=eating,args=())
x.start()
y = threading.Thread(target=reading,args=())
y.start()
z = threading.Thread(target=going,args=())
z.start()



#eating()
#reading()
##going()          
print(threading.active_count())
print(threading.enumerate())