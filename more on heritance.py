class Animal:
    alive = True
    moving = True
    eating = True
    healthy = True

    def running(self):
        print("THE ANIMAL IS VERY FAST")

    def cumming(self):
        print("IT USES ITS EYES")
class Rabit(Animal):
    def speed(self):
        print("its very fast ")   
class Fish(Animal):
    def home(self):
        print("it lives in water") 
class Pigoen(Animal):
    def movement(self):
        print("it fly's")    


Rabit1 = Rabit()
Rabit1.running()
Rabit1.cumming()
Rabit1.speed()
print(Rabit1.eating)

Fish1 = Fish()
Fish1.cumming()
Fish1.running()
print(Fish1.healthy)
