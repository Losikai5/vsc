class carz:
    wheels = 4
    def __init__(self,make,color,year,mode):
        self.make = make
        self.color = color
        self.year = year
        self.mode = mode


    def driving(self):
        print("its self driving")