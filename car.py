class Car:
    def __init__(self,modle,year,color):
        self.molde  = modle
        self.year = year
        self.color = color

    def drive(self):
        print("THIS "+self.molde+" IS DRIVING") 
    def stop(self):
        print("THIS  "+self.molde+"  HAS STOPPED")  


CAR1 = Car("TOYOTA",2001,"RED")
print(CAR1.molde)
print(CAR1.color)
print(CAR1.year)
CAR1.drive()
CAR1.stop()