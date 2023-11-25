class car():
    def turn_on(self):
        print("START THE ENGINE")
        return self
    def move(self):
        print("THE WHEELS START MOVING")
        return self
    def stop(self):
        print("THE ENGINE GOES OFF")
        return self

car1 = car()
car1.turn_on()\
.move()\
.stop()
print("CODING IS FUN")                