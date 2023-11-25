class Prey:
    def flee(self):
        print("It runs away always")

class Predetor:
    def attack(self):
        print("It attacks the prey")


class Rabitz(Prey):

    pass
class Lion(Predetor):
    pass

class Fish(Predetor,Prey):
    pass



Fish3 = Fish()
Fish3.flee()
Fish3.attack()

Lion2 = Lion()
Lion2.attack()

Rabitz5 = Rabitz()
Rabitz5.flee()