class duck:
    def walk(self):
        print("it moving")
    def talk(self):
        print("its speaking")
class chicken:
    def walk(self):
        print("it legging")
    def talk(self):
        print("its clittering")          


class person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("CAUGHT YOU")

DUCK = duck()
CHICKEN  = chicken()
PERSON = person()
PERSON.catch(CHICKEN) 