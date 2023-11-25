class animal:
      def eat(self):
        print("i can eat nawe")
class Dog(animal):
    def bark(self):
        print("i can bark") 


class cat(animal):
    def sound(self):
        print('i can mwewo')


dog1 = Dog()
dog1.bark()
dog1.eat()


cat1 =  cat()
cat1.sound()
cat1.eat()