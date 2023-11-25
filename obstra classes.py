from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class motorcycle(vehicle):
    def go(self):
        print("START MOVING")
    def stop(self):
        print("STOP MOVING")    
class car(vehicle):
    def go(self):
        print("STARTING GOING")
    def stop(self):
        print("STOP MOVING")    

#vehicle1 = vehicle()
motorcycle1 = motorcycle()
CAR = car()

#vehicle1.go()
#vehicle.stop()
motorcycle1.go()
motorcycle1.stop()
CAR.go()
CAR.stop()