class Car:
    color = None
def change_color(self,color):
    self.color = color
class bike:
    color = None  
car1 = Car()
car2 = Car()
car3 = Car()
bike1 = bike()
print(car1.color)
print(car2.color) 
print(car3.color)  

change_color(car1,'blue')
print(car1.color)
change_color(car2,'black')
print(car2.color)
change_color(car3,'white')
print(car3.color)
change_color(bike1,'orange')
print(bike1.color)
